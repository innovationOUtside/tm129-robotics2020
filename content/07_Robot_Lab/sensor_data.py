from PIL import Image
import numpy as np

import pandas as pd


def style_df(df, colorTheme='Blues'):
    """Return a styled dataframe (not a dataframe...)."""
    return df.style.background_gradient(cmap=colorTheme)

def process_robot_image_data(data):
    """Process the robot image data and return a dataframe."""

    df = pd.DataFrame(columns=['side', 'vals', 'clock'])
    for r in data:
        _r = r.split()
        if len(_r)==3:
            tmp=_r[1].split(',')
            k=4
            del tmp[k-1::k]
            df = pd.concat([df, pd.DataFrame([{'side':_r[0],
                                              'vals': ','.join(tmp),
                                              'clock':_r[2]}])])
    df.reset_index(drop=True,inplace=True)
    return df

def image_data_to_array(image_data, index=0, size=(20, 20, 3)):
    """Convert the image data string to a numpy array."""
    image_array = np.array(image_data).reshape(size[0], size[1], size[2]).astype(np.uint8)
    return image_array


def array_from_image(img, size=(28, 28)):
    """Get array from image."""
    _array = np.array(image_data_from_image(img)).astype(np.uint8)
    # Reshape as a 28x28 array
    image_array = _array.reshape(size[0], size[1])
    return image_array


def image_from_array(image_array, mode='L'):
    """Generate an image from an array."""
    return Image.fromarray(image_array).convert(mode)


def image_data_from_image(img):
    """Get image data from image."""
    return img.getdata()


def df_from_image(img, show=True, colorTheme='Blues'):
    """Return a dataframe from image data."""
    img_df = pd.DataFrame(np.reshape(list(img.getdata()), img.size))
    if show:
        display(style_df(img_df))
    return img_df

#bw_df = df_from_image(img)


def image_from_df(df):
    """Return an image from a dataframe."""
    return image_from_array( df.values.astype(np.uint8) )


# was: image_data_to_array
def raw_image_data_to_array(tmp, index=0, size=(20, 20, 3), col='vals'):
    """Convert the image data string to a numpy array."""
    
    if isinstance(tmp, pd.DataFrame):
        if 'vals' in tmp.columns:
            if index >= tmp.shape[0]:
                print(f"There are only {tmp.shape[0]} samples in the dataset.")
                return 

            # TO DO: we need to better detect the image size: (x, y, depth)
            tmp = tmp.iloc[index][col].split(',')
        else:
            print(f"An unrecognised dataframe was provided (no {col} column?).")
            return 

    #return np.array(tmp).reshape(size[0], size[1], size[2]).astype(np.uint8)
    return image_data_to_array(tmp, index, size)


    
def collected_image(df, index=0, size=(20, 20, 3)):
    """Render collected data as an image.
    """

    if isinstance(df, list):
        # try this...
        df = process_robot_image_data(df)
        
    vv = raw_image_data_to_array(df, index, size)
    
    #This is assuming a depth of 3
    vvi = Image.fromarray(vv, 'RGB')
    return vvi

def generate_image(image_data, index=0, size=(20, 20, 3)):
    """Generate image from each row of dataframe."""
    image_data_df = process_robot_image_data(image_data)

    return collected_image(image_data_df, index, size)


def generate_bw_image(image_data, index=0, size=(20, 20, 3), thresh = 200):
    """Generate dataframe with black and white image data."""
    
    img = generate_image(image_data, index, size)
    
    #convert('1') converts to black and white;
    # use a custom threshold via:
    # https://stackoverflow.com/a/50090612/454773
    
    fn = lambda x : 255 if x > thresh else 0

    bw = img.convert('L').point(fn, mode='1')

    return bw

#img = generate_bw_image(roboSim.image_data)


# Create signature from row
#Streak code cribbed from:
# https://joshdevlin.com/blog/calculate-streaks-in-pandas/
def generate_signature_from_series(s, fill=255):
    """
    Create a signature for the data based on:
     - the initial value in a row
     - the longest run of black pixels
     - the longest run of white pixels
     - the number of transitions / edges
    """
    
    data = pd.DataFrame(s)
    data.columns = ['v']
    data['start'] = data['v'].ne(data['v'].shift(fill_value=fill))
    data['_id'] = data['start'].cumsum()
    data['counter'] = data.groupby('_id').cumcount() + 1
    data['end'] = data['v'].ne(data['v'].shift(-1))
    
    transitions = data['end'].sum()
    longest_white = data[data['end'] & data['v']]['counter'].max()
    longest_black = data[data['end'] & ~data['v']]['counter'].max()
    
    longest_white = 0 if pd.isnull(longest_white) else longest_white
    longest_black = 0 if pd.isnull(longest_black) else longest_black
    
    initial_value = s.iloc[0]
    return transitions, initial_value, longest_white, longest_black



## Zoomed image display

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

def zoom_img(img, size=(5, 5), grid=True):
    """Zoom the display of the sensor captured image."""
    plt.figure(figsize = size)

    #plt.axis('off')
    
    #
    
    if grid:
        plt.grid()
        plt.xticks(range(0, img.size[0]+1))
        plt.yticks(range(0, img.size[1]+1))
    else:
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
  
    plt.imshow(np.asarray(img.convert('RGB')),
               extent=(0, img.size[0], img.size[1], 0));
    
    
    

# Focus on image
# The following routines willdrop all background rows/columns
# from left/right/upper/lower edge of dataframe

#https://stackoverflow.com/a/54405767/454773
def background_column(s, background=255):
    """Report wether all values in a column are the same."""
    a = s.to_numpy()
    return (a[0] == a).all() and a[0] == background

def clear_columns(df, reverse=False, transpose=False, background=255):
    """Clear edge columns / rows in dataframe
    where all values the same."""
    
    if transpose:
        df = df.T
    
    if reverse:
        df = df.loc[:, ::-1].copy()
    
    for c in df:
        if background_column(df[c], background):
            df.drop(columns=[c], inplace=True)
        else:
            break

    if reverse:
        df = df.loc[:, ::-1]
        
    if transpose:
        df = df.T

    return df

    
#bw_df = pd.DataFrame(np.reshape(list(bw.getdata()), (20,20)))
def trim_image(bw_df, background=255, reindex=False, retimage=False,
               show=True, colorTheme='Blues'):
    """Take an image dataframe and trim its edges."""
    if isinstance(bw_df, Image.Image):
        bw_df = df_from_image(bw_df)
 
    bw_dfx = clear_columns(bw_df, False, False, background=background)
    bw_dfx = clear_columns(bw_dfx, False, True, background=background)
    bw_dfx = clear_columns(bw_dfx, True, False, background=background)
    bw_dfx = clear_columns(bw_dfx, True, True, background=background)
                          
        
    if reindex:
        bw_dfx.reset_index(drop=True, inplace=True)
        bw_dfx.columns = list(range(bw_dfx.shape[1]))
    
    if retimage:
        # This assumes a grayscale image at least
        vv = raw_image_data_to_array(df, index, df.shape)
        vvi = Image.fromarray(vv, 'L')
    
    if show:
        display(style_df(bw_dfx, colorTheme))
    
    return bw_dfx

#trim_image( df_from_image (img))


def crop_and_zoom_to_fit(img, background=0, scale=1):
    """Crop an image then zoom back to fit the original image size."""
    _trimmed_image_df = trim_image( df_from_image(img), background=background, show=False)
    _cropped_image = image_from_df(_trimmed_image_df)
    
    # TO DO - allow a scale function that scales up and down within the image frame
    # TO DO - scaling <1.0 should scale then paste the image into the centre of the full size frame
    _resized_image = _cropped_image.resize(img.size, Image.LANCZOS)
    return _resized_image


import random

def jiggle(img, background=0, quiet=True):
    """Jiggle the image a bit so it's not quite centred."""
    _image_size = img.size
    if not quiet:
        display(img)
    
    _trimmed_image_df = trim_image( df_from_image(img, show=False), background=0, show=False)
    _cropped_image = image_from_df(_trimmed_image_df)
    (_xt, _yt) = _cropped_image.size
    
    _image_mode = 'L' #greyscale image mode
    _shift_image = Image.new(_image_mode, _image_size, background)

    # Set an offset for where to paste the image
    # The limit of the jiggling depends on the size of the cropped image
    _x = random.randint(0, _image_size[0]-_xt )
    _y = random.randint(0, _image_size[1]-_yt )
    _xy_offset = (_x, _y)

    _shift_image.paste(_cropped_image, _xy_offset) 
    
    return _shift_image


    if img.size!=(_x, _y):
        if not quiet:
            print("Resizing")
        img = img.resize((_x, _y), Image.LANCZOS)
    
    return img

#jiggle(img, quiet=False)