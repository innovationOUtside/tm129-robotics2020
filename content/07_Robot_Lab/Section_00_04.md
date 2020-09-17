<!-- #region -->
# 4 Recognising patterns on the fly



To be really useful a robot needs to recognise things as it goes along, or ‘on the fly’. In this notebook, you will train a neural network to use a simple MLP classifier to try to identify different shapes on the background.

We will use the two light sensors to collect the data used to train the network:

- one light sensor will capture the shape image data;
- one light sensor will capture the training class data.

We will contrive things somewhat to collect the data at specific locations on the background.

Before continuing, ensure the simulator is loaded and available:
<!-- #endregion -->


```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds
%load_ext nbev3devsim
%load_ext nbtutor
```

The background image *Simple_Shapes* contains several shapes arranged in a line, including a square, a circle, four equilateral triangles (arrow heads) with different orientations, a diamond and a rectangle.

Just below each shape is a grey square, whose fill colour is used to distinguish between the different shapes.

```python
%sim_magic -b Simple_Shapes -x 600 -y 700
```

## Training pass 1

In this inital training pass, we we configure our program to try to identify when it sees a clear training class pattern. The training class patterns are grey squares where the grey colour is use to represent one of eight (8) different training classes.

The left light sensor will be used to sample the shape image data and the right light sensor will be used to collect the simpler grey classification group pattern.

As we are going to be pulling data into the notebook Python environment from the simulator, ensure the local notebook datalog is cleared:

```python
roboSim.clear_datalog()
```

We can now start to collect data from the robot's left light sensor. The `-R` switch runs the programme once it has been downloaded to the simulator:

```python
%%sim_magic_preloaded -b Simple_Shapes -R -x 840 -y 700 -O

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is a command invocation rather than a print statement
print("image_data left")
```

The `image_data left` invocation in the program downloaded to the simulator also logs a copy of the left sensor reading data as the first item (with index `0`) in the `roboSim.image_data` list. We can preview that data as an image in the following way:

```python
from sensor_data import generate_image

index = 0

img = generate_image(roboSim.image_data, index)
img
```

We can also use the `sensor_data.zoom_img()` function to zoom the display of an image generated from the sensor data grabbed into the notebook. The axes co-ordinates show the size, in pixels, of the image.

```python
from sensor_data import zoom_img

zoom_img(img)
```

The original sensor data is actually provided as a three channel data set, with the value for each pixel encoded as the three RGB (red, green, blue) channel values.

We can simplify the representation of the data by transforming the image to a black and white image, using a default (or explicity set) threshold value to decide whether a pixel should be represented as a black or white value.

```python
from sensor_data import generate_bw_image

bw_img = generate_bw_image(roboSim.image_data, index)
zoom_img(bw_img)
```

We can run the same program again from a simple line magic that is used to situate the robot at a specific location and then run the program to collect the sensor data.

```python
_x = 680

%sim_magic -x $_x -y 700 -R
```

We can review also the data that defines this transformed image as a *pandas* dataframe using the `df_from_image()` function.

*By default, the dataframe returning functions will preview the dataframe with colour highlight; pass the attribure `show=False` to disable this view.*

```python
from sensor_data import df_from_image

_ = df_from_image(bw_img)
```

## Collecting Data Samples

Let's start by seeing if we can collect image data samples for each of the shapes.


- 600 400 square
- 680 400 circle
- 760 400 equitri1
- 840 400 equitri2
- 920 400 equitri3
- 1000 400 equitri4
- 1080 400 rect
- 1160 400 diamond1

```python
import time

roboSim.clear_datalog()

# x-corodinate for centreline of first shape
_x_init = 600

# Distance between shapes
_x_gap = 80

# Number of shapes
_n_shapes = 8

# y-coordinate for centreline of shapes
_y = 700

# Generate x coordinate for each shape in turn
for _x in range(_x_init, _x_init+(_n_shapes*_x_gap), _x_gap):
    
    # Jump to shape and run program to collect data
    %sim_magic -b Simple_Shapes -x $_x -y $_y -R
    
    # Wait a short period to allow time for
    # the program to run and capture the sensor data,
    # and for the data to be passed from the simulator
    # to the notebook Pyhton environment
    time.sleep(1)

```

We should now be able to access multiple image samples via `roboSim.image_data`. The `process_robot_image_data()` allows us to view this data as a dataframe containing as many rows as images we scanned:

```python
from sensor_data import process_robot_image_data

image_data_df = process_robot_image_data(roboSim.image_data)
image_data_df
```

One thing we can do to simplify the original sensor data is to convert the RGB sensor image with three colour channels for each pixel to a simpler black and white image where there is a single channel taking only two values: 0 for black, and 255 for white. 

```python
from sensor_data import collected_image

index = 4

collected_image(image_data_df, index)
```

We can then index into the data frame and render the `vals` data as an image for a specified row:

```python
%%sim_magic_preloaded -b Simple_Shapes -x 700 -y 716 -O
tank_drive.on(SpeedPercent(10), SpeedPercent(10))
while True:
    sample = colorRight.reflected_light_intensity_pc
    #print(sample)
    if sample>12 and sample<13:
        print('here...')
```

Can we identify when we have seen a grey training class square?

```python
# function to count what percentage of classificaiton group image pixels
# are non-background; if this is 0 (or < threshold) decide we have seen a thing
# and take the most common pixel value as the discriminator
```


## Feature Engineering

When presenting a raw image to a neural network, for example as a list of N x M values, one for each pixel in the image, each value represents a distinct *feature* that the network may use to help it generate a particular classification.

*Feature engineering* is the name give to the process of deriving new features from the original raw data set that can used to either complement the original data set, or be presented to the network for training, and recall, instead of the original data. The aim of using derived features, rather than the original pixel features, is to try to improve the performace of the network.


### Preprocessing the Image Data

One of the problems with using the actual pixel data in a simple MLP is that the network can find it hard to recognise images from the actual raw pixel data: shapes may vary very slightly in size, orientation or framing within the sensor view area (eg they may be shifted to the left or right side of the sensor view, or the top or the bottom of it). These slight changes may cause large changes in the raw pixel values.

So can we use feature engineering to try to help improve matters? For example, might we represent the sensor data in some other way, and then train the MLP on the new representation with improved performance?

You may recall the fruit recognition activity from an earlier notebook. In that case, the various fruits were recognised based on physical properties of the each fruit in the form of the dimensions of the bounding box drawn around each one, rather than the actual picture of the fruit. The features used for training and recall in that case were thus the bounding box dimensions.

So can we perform a similar sort of re-presentation of the originally captured shape image data to create a derived set of features agains which we can train our MLP? 


## Activity — Using bounding box features for shape images 

Will the bounding box approach used to represent the fruit image data generate features that will alow us to distinguish between the shape images?

Running the following code cell will convert the raw data associated with an image to a data frame, and then prune the rows and columns the edges that only contain white space.

The dimensions of the dataframe, which is to say, the `.shape` of the dataframe, given as the 2-tuple `(rows, columns)`, corresponds to the bounding box of the shape. 

```python
from sensor_data import trim_image

index = 4

img = generate_bw_image(roboSim.image_data, index)
display(img)


trimmed_df = trim_image( df_from_image(img, show=False), reindex=True)

# dataframe shape
trimmed_df.shape
```

Using the above code, or otherwise, find the shape of the bounding box for each shape as captured in the `roboSim.image_data` list.

You may find it useful to use the provided code as the basis of a simple function that will:

- take the index number for a particular image data scan;
- generate the image;
- find the size of the bounding box.

Then you can iterate through all the rows in the `roboSim.image_data` dataset, generate the corresponding image and its bounding box dimensions, and then display the image and the dimensions.

*Hint: you can use a `for` loop defined as `for i in range(len(roboSim.image_data)):` to iterate through each row of the data frame and generate an appropriate index number, `i`, for each row.*

Based on the shape dimensions alone, can you distinguish between the shapes?


#### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*


Let's start by creating a simple function inspired by the supplied code that will display an image and its bounding box dimensions:

```python
def find_bounding_box(data, index):
    """Find bounding box for an image based on its index."""
    
    img = generate_bw_image(data, index)
    trimmed_df = trim_image( df_from_image(img, show=False), reindex=True)

    # Show image and shape
    display(img, trimmed_df.shape)

find_bounding_box(roboSim.image_data, 2)
```

We can then call this function by iterating through each image data record in the `roboSim.image_data` dataset:

```python
for i in range(len(roboSim.image_data)):
    find_bounding_box(roboSim.image_data, i)
```

Inspecting the results from my run (yours may be slightly different), several of the shapes appear to share the same bounding box dimensions:

- the circle and square both have bounding box dimensions `(15, 15)`;
- two of the arrows / equilateral triangles share the same dimesions (`(15, 13)`).

Only the rectange is clearly separated from the other shapes on the basis of its bounding box dimensions.


## Creating alternative features

Using the dimensions of the bounding box for each shape does not appear to provide a set of features that we can use to train a neural network on to distinguish between the shapes. We have already simplified the image data from the original RGB encoded values to a single black/white colour channel, essentially just one bit per pixel. But what other features might we identify, or even create, from the original data?

One thing we might do is count the number of transitions from black to white or white to black along each row in the dataframe.

I have created a simple function, `generate_signature_from_series()` that can be used to generate a "signature" for each row in the dataframe.

The signature comprises four values:

- the number of black to white and white to black *transitions* in the row (that is, the number of *edges* in the row);
- the value of the *initial* pixel in the row;
- a count of the longest run of *white* pixels in the row (that is, the width of the broadest white band in the row);
- a count of the longest run of *black* pixels in the row (that is, the width of the broadest black band in the row).

We can apply the function to each row as follows:

```python
from sensor_data import generate_signature_from_series

bw_df.apply(generate_signature_from_series, axis=1)
```

Although we have reduced the amount of numbers that represent each row from 20 separate pixel values to just 4 signature values, we arguably have a much more powerful representation of the image that captures much of the useful *information* in the image.

In particular, casting the image to a black and white image removes potential variation arising from noise caused by greyscale pixel values. Counting the number of edges is invariant if we shift the image slightly to the left or the right in the sensor view; the first pixel value in the row also provides information as to whether the first transition is from white to black or black to white.


