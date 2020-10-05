---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

?? lot of optional?

### Creating synthetic data — translating an original image

We have already seen how we can get rid of the "background" columns and rows around the outside of an image using the `nn_tools.sensor_data.trim_image()` function:

```python
# Pass the parameter show=False to hide the display
# of the untrimmed and trimmed dataframes
trimmed_image_df = trim_image( test_image, background=0)
```

We can also convert this dataframe back to an image:

```python
from nn_tools.sensor_data import image_from_df

cropped_image = image_from_df(trimmed_image_df)
zoom_img( cropped_image )

cropped_image.size
```

If we create a blank image of size 28 x 28 pixels with a grey background, we can paste a copy of our cropped image into it. The `nn_tools.sensor_data.jiggle()` function implements this approach. It will accept an image and then return randomly translated version of it.

Run the following cell several times to see the effect of the `jiggle()` function on a test image.

```python
from nn_tools.sensor_data import jiggle

jiggled_image =  jiggle(test_image)
zoom_img(jiggled_image)

# Show size
jiggled_image.size
```

Another way of transforming the cropped images is to magnify it back to the original image size. (The rescaling employs a digital filter that is used to interpolate new pixel values in the scaled image based on the pixel values in the cropped image. As such, it may introduce digital artefacts of its own into the scaled image.)

```python
from nn_tools.sensor_data import crop_and_zoom_to_fit

crop_zoomed_image = crop_and_zoom_to_fit(test_image)

zoom_img( crop_zoomed_image )

# Show size
crop_zoomed_image.size
```

<!-- #region -->
To simplify the process of applying these transformations to an a test image, we can call the `predict_and_report_from_image()` with the `jiggled=True` and `cropzoom=True` parameters:

```python
# Test a jiggled version of the provided image
predict_and_report_from_image(MLP, test_image, test_label,
                              jiggled=True, quiet=False)

# Test a cropped and then zoomed version of the provided image
predict_and_report_from_image(MLP,
                              test_image, test_label,
                              cropzoom=True, quiet=False)
```

You can also pass the `zoomview=True` parameter to view the image at a larger scale.
<!-- #endregion -->

<!-- #region activity=true -->
## Activity — translating the digit within the image frame

Explore how the `sensor_data.jiggle()` function works in practice. Run the following cell multiple times, observing what happens in each case, to see how the a differently translated versions of the image are returned each time the function is called. Is there much variation in how the digit is centered in the image frame?
<!-- #endregion -->

```python activity=true
from nn_tools.sensor_data import jiggle

# Setting quiet=False displays the original input image
# as well as returning the jiggled image as cell output
zoom_img( jiggle(image_image, quiet=False) )
```

<!-- #region student=true -->
*Record any notes or observations here.*
<!-- #endregion -->

<!-- #region activity=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true -->
The `jiggle` function slightly translates the image to the left, right, and up and down within the image area. However, it nevers seems to be translated so far that bits of it get cut off.
<!-- #endregion -->

<!-- #region activity=true -->
## Activity — Testing the MLP against translated digit images

Now let's see how well our trained MLP responds to translated versions of the original training images.

Start by testing the network against one of the original images:
<!-- #endregion -->

```python activity=true
from nn_tools.network_views import predict_and_report_from_image

test_image, test_label = get_random_image()

predict_and_report_from_image(MLP, test_image,
                              test_label, quiet=False, confidence=True)
```

<!-- #region activity=true -->
How does the trained MLP fare if we translate the image? Run the following cell several times and see if the MLP continues to classify the digit correctly.
<!-- #endregion -->

```python activity=true
predict_and_report_from_image(MLP, test_image, test_label,
                              jiggled=True, quiet=False, confidence=True)
```

<!-- #region student=true -->
*Record your observations about how well the MLP performs against the translated images here. Why you think the network is performing the way it does?*
<!-- #endregion -->

<!-- #region activity=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true -->
When I tested the network against the translated / jiggled images, I found that it wasn't very reliable at classifying them.

Although the digits are the same size as the original digits, the original MLP has no real sense of how the pixels representing the digits relate to each other according to their *relative* location*.

Instead, it is looking for pixels that overlap the pixels representing the digit that were presented in the original training set. If we translate the digit in the image frame, it may end up overlapping the pixels associated with the original location of another digit more than it overlaps the pixels associated with its own originally located image.
<!-- #endregion -->

<!-- #region activity=true -->
## Activity — rescaling the digit within the image frame

How well does the trained MLP work if we rescale the image by crop it and then zooming it to fit the original image size?
<!-- #endregion -->

```python activity=true
predict_and_report_from_image(MLP,
                              test_image, test_label,
                              cropzoom=True, quiet=False, confidence=True)
```

<!-- #region student=true -->
*Record your observations about how well the MLP performs against the translated images here. Why you think the network is performing the way it does?*
<!-- #endregion -->

<!-- #region activity=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true -->
When I tested the network against the resized images, I found that it wasn't very reliable at classifying them.

The original MLP has no real sense of how images are scaled across the presented image frame: it is looking for pixels that overlap the pixels representing the digit that were presented in the original training set.
<!-- #endregion -->

```python
# TO DO how poor is it?
```

```python
test_and_report_random_images(MLP, get_random_image, num_samples=100, jiggled=False, cropzoomed=False)
```

## Training the network on transformed images

The MNIST images we have been provided with each have dimensions of 28 x 28 pixels. If we want to try to classify a handwritten digit image using the MLP trained against these MNIST images, we need to resize the image to the same size.

In a later notebook, you will be using an MLP to try to classify handwritten digit images scanned in from the simulator. These image scans have size 14 x 14 pixels. If we were to resize those collected images and then present them to our network, the scaling up of the image may introduce digital artefacts that affect the classification.

So instead, lets take the opportunity now to create an MLP trained on resized hand written images, scaled down to a size of 14 x 14 pixels. This will further review the process of how we train an MLP.

To being with, lets create a set of test images. The test images will be created using the following pipeline

- generate an image from the image array data
- resize image from 28 x 28 pixels down to 14 x 14 pixels
- convert the resized image to a black and white image using a specified threshold


```python
# Create a test data set made of resized images
# Images are resized to 14 x 14
bw_resized_image_array_list = []

resize_dimensions = (14, 14)
bw_threshold = 100

# Use all the images in the original images_array
for i in tqdm(images_array):
    # Generate image
    _image_from_array = Image.fromarray(i)
    # Resize image
    _resized_image = _image_from_array.resize(resize_dimensions, Image.LANCZOS)
    # Convert to black and white
    bw_resized_image = make_image_black_and_white(_resized_image, threshold=bw_threshold)
    # Add to list
    bw_resized_image_array_list.append(array_from_image(bw_resized_image, size=resize_dimensions))

# Convert the list of training image arrays to an array
training_arrays = np.array(bw_resized_image_array_list).reshape(len(images_array), 
                                                                resize_dimensions[0]*resize_dimensions[1])

# Normalise the training data
normalised_training_arrays = normalize(training_arrays, norm='max', axis=0)
```

Now create the initial network architecture. We have simplified the data both by reducing the dimensions the images (and hence the number of input nodes required) and also moved away from a discrete grey scale image representation to a binary black and white image representation.

So let's use a simpler network.

Let's try with just a single layer of 10 neurons to start with.

```python
hidden_layer_sizes = (10)
max_iterations = 150

MLP2 = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iterations,
                    verbose=True,
                    # For reproducibility, set the inital random state to a specified seed value
                    #random_state=1,
                   )
```

```python
MLP2.fit(normalised_training_arrays[:train_limit], labels[:train_limit])
```

```python
# How well did the network perform on the training samples
test_and_report_images(MLP2, normalised_training_arrays[:train_limit], labels[:train_limit])
```

```python
# How well did the network perform on the test samples
test_and_report_images(MLP2, normalised_training_arrays[train_limit:], labels[train_limit:])
```

```python
# Save the network
dump(MLP2, 'mlp_mnist14x14.joblib') 
```

```python
# Train the network
test_limit = 200
train_limit = len(normalised_training_arrays) - test_limit

from ipywidgets import interact_manual
MLP2 = None

@interact_manual(iterations=(100, 2000, 100),
          h1=(0, 10, 1), h2=(0, 10, 1))
def trainer(iterations=100, h1=6, h2=6):
    global MLP2
    MLP2 = MLPClassifier(hidden_layer_sizes=(h1, h2),
                          max_iter=iterations)
    
    # Fit the model
    MLP2.fit(normalised_training_arrays[:train_limit], labels[:train_limit])
    
    print("Training set score: {}".format(MLP2.score(normalised_training_arrays[:train_limit], labels[:train_limit])))
    print("Test set score: {}".format(MLP2.score(normalised_training_arrays[train_limit:], labels[train_limit:])))
    
    #Check the prediction for each input
    predictions = MLP2.predict((normalised_training_arrays[train_limit:]))

    print("Test set reports")
    print(classification_report(labels[train_limit:], predictions))
    print(confusion_matrix(labels[train_limit:], predictions))
```

```python
import math
def test_and_report_images(MLP, test_images, test_labels, 
                           jiggled=False, cropzoomed=False):
    """Test and report on pre-trained MLP using a provided set of test images."""
    flat_image = np.array(test_images).reshape(len(test_images), test_images[0].size)

    # Normalise the values in the list
    # to bring them into the range 0..1
    normalised_flat_images = normalize(flat_image, norm='max')
    predictions = MLP.predict(normalised_flat_images)

    print("Classification report:\n",
          classification_report(test_labels, predictions))
    print("\n\nConfusion matrix:\n",
          confusion_matrix(test_labels, predictions))

    print("Training set score: {}".format(MLP.score(normalised_flat_images, test_labels)))
    print("Test set score: {}".format(MLP.score(normalised_flat_images, test_labels)))


def test_and_report_random_images(MLP, randfunc, num_samples=100, 
                                  jiggled=False, cropzoomed=False):
    """Test and report on pre-trained MLP using specified number of random images."""

    test_list, test_labels = generate_N_random_samples(randfunc=randfunc, num_samples=num_samples )
    test_and_report_images(MLP, test_list, test_labels, jiggled, cropzoomed)

```

```python
resized_images = []
for i in tqdm(images_array):
    resized_images.append(array_from_image(make_image_black_and_white(Image.fromarray(i).resize((20, 20), Image.LANCZOS), threshold=100), (20, 20)))

```

```python
# Test the network
test_and_report_images(MLP2, resized_images[train_limit:], labels[train_limit:])
```

## Optional Activity — Improving the performance of the network

__If the network doesn't work perfectly in the recognition task against the data it is trained with, try tuning the network parameters and retraining the network to see if you can improve its performance.__

Once again, can you improve performance against these unseen items by tweaking the network parameters and retraining it?

```python

```

```python
<div class="girk">
#TO DO -  single function to train MLP.
# Didn't I have a widget thing for this in week 6?

from ipywidgets import interact

fruit = None

@interact(iterations=(100, 3000, 100),
          h1=(0, 10, 1), h2=(0, 10, 1))
def trainer(iterations=2000, h1=6, h2=6):
    global fruit
    fruit = MLPClassifier(hidden_layer_sizes=(h1, h2),
                          max_iter=iterations)
    
    # Fit the model
    fruit.fit(df['Input'].to_list(), df['Fruit'])
    
    #Check the prediction for each input
    predictions = fruit.predict(df['Input'].to_list())

    print(classification_report(df['Fruit'], predictions))
    print(confusion_matrix(df['Fruit'], predictions))</div><i class="fa fa-lightbulb-o "></i>
```

## Trying to improve the performance of our MLP

You may have noticed that the trained MLP did not perform particularly well when presented with the translated or resized images.

Can we perhaps improve matters by increasing the size of our training dataset and 

Given our original training images, we can derive a set of additional training images that add further variation to the training set by translating and resizing 


## Parameter sweeps - to do but not in this module

```python
# Increase size of test array
for i in range(len(images_array)):
    _image_array = images_array[i]
    # And convert it to an image
    _image_image = Image.fromarray(_image_array.astype(np.uint8))
    
    # Jiggle - randomly translate the image inside the image frame
    _image_image = jiggle(_image_image)
    
    #Convert back to data
    _image_array = np.array(_image_image.getdata()).astype(np.uint8)
    _image_array = _image_array.reshape(28, 28)
    
    images_array = np.append(images_array, [_image_array], 0)
    labels.append(labels[i])
```

```python
len(labels), len(images_array)
```
## Feature engineering

When presenting a raw image to a neural network, for example as a list of N x M values, one for each pixel in the image, each value represents a distinct *feature* that the network may use to help it generate a particular classification.

*Feature engineering* is the name give to the process of deriving new features from the original raw data set that can used to either complement the original data set, or be presented to the network for training, and recall, instead of the original data. The aim of using derived features, rather than the original pixel features, is to try to improve the performance of the network.

<!-- #region -->
## Creating alternative features

TO DO - convert the greyscale image to black and white


Using the dimensions of the bounding box for each shape does not appear to provide a set of features that we can use to train a neural network on to distinguish between the shapes. We have already simplified the image data from the original RGB encoded values to a single black/white colour channel, essentially just one bit per pixel. But what other features might we identify, or even create, from the original data?

One thing we might do is count the number of transitions from black to white or white to black along each row in the dataframe.

I have created a simple function, `generate_signature()` that can be used to generate a "signature" for various sorts of input: a single image, a dataframe representing a single image, or a `numpy` array representing an images.

The signature comprises sets four values, one set per row of the image, image dataframe, or image array:

- the number of black to white and white to black *transitions* in the row (that is, the number of *edges* in the row);
- the value of the *initial* pixel in the row;
- a count of the longest run of *white* pixels in the row (that is, the width of the broadest white band in the row);
- a count of the longest run of *black* pixels in the row (that is, the width of the broadest black band in the row).
<!-- #endregion -->

```python
from nn_tools.sensor_data import make_image_black_and_white

test_image, test_label = get_random_image()

bw_img = make_image_black_and_white(test_image, thresh=200)

#The image mode 1 shows it's a black and white image
# Although if we inspect the data we see the pixel values
# are 0 and 255 rather than 0 and 1
bw_img.mode
```

```python
# TO DO - can we apply this to a single row? Example

# TO DO activity - apply to each row and comment 
```

We can create the signature for each row as follows (add the parameter `normalise=0` to normalise the values down the feature columns).

```python
from nn_tools.sensor_data import generate_signature

sig_df = generate_signature(bw_img, normalise=0)
sig_df
```

We can now use this data as the training data...

Linearise  set `linear=True`)

```python
sig_df.values.ravel()
```

```python
from nn_tools.sensor_data import generate_signature_from_series 
def generate_signature(img, thresh=200, normalise=None, linear=False, segment=False):
    """Generate signature from image."""
    if isinstance(img, Image.Image):
        bw_img = make_image_black_and_white(img, thresh=thresh)
        _rows, _cols = bw_img.size
        _array = np.array(list(bw_img.getdata())).reshape(_rows, _cols)
        _df = pd.DataFrame(_array)
    elif isinstance(img, pd.DataFrame):
        _df = img
    else:
        # if  array
        _df = pd.DataFrame(img)
        
    if segment:
        _df.drop(_df.index[[4, 5, 6,  9, 10, 11,  18, 19, 20, 24, 25, 26]], inplace=True)
    _signatures = _df.apply(generate_signature_from_series, axis=1)
    _df = pd.DataFrame(list(_signatures))
    #Normalise down columns
    if normalise is not None:
        # if normalise=0 normalise down cols (features) rows
        # if 1, normalise across rows
        # We would expect to pass 0 here to nornalise features
        if normalise:
            _df = _df.T
        _array = _df.values # Returns an array
        min_max_scaler = preprocessing.MinMaxScaler()
        scaled = min_max_scaler.fit_transform(_array)
        _df = pd.DataFrame(scaled)
        if normalise:
            _df = _df.T
    if linear:
        return _df.values.ravel()
    return _df
```

The processing of the signatures takes some time to run (the code is far from optimal!), so we shall try to train the MLP using a collection of just 500 image signatures.

```python
from tqdm.notebook import tqdm
import pandas as pd

idfx=[]
for i in tqdm(images_array[:500]):
    #idfx.append(pd.DataFrame(i))
    idfx.append(array_from_image(crop_and_zoom_to_fit(Image.fromarray(i))))

idsx = []
for i in tqdm(idfx[:500]):
    idsx.append(generate_signature(i, linear=True))

```

```python
# normal
training_arrays = np.array(images_array[:500]).reshape(500, 28*28)
normalised_training_arrays = normalize(training_arrays, norm='max', axis=0)

```

```python
# resized to 20 x 20
idfr=[]
for i in tqdm(images_array[:500]):
    idfr.append(array_from_image(Image.fromarray(i).resize((20, 20), Image.LANCZOS), size=(20,20)))
    
training_arrays = np.array(idfr).reshape(500, 20*20)
normalised_training_arrays = normalize(training_arrays, norm='max', axis=0)

```

```python
#cropped resized
training_arrays = np.array(idfx).reshape(len(idsx), 28*28)
normalised_training_arrays = normalize(training_arrays, norm='max', axis=0)
#normalised_training_arrays[0]
```

```python
flat_signatures = np.array(idsx).reshape(len(idsx), 28*4)#16*4)
normalised_training_arrays = normalize(flat_signatures, norm='max', axis=0)
normalised_training_arrays[0]
```

```python
# create network
hidden_layer_sizes = (40)
max_iterations = 2000

MLP2 = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iterations,
                    verbose=True,
                    # For reproducibility, set the inital random state to a specified seed value
                    #random_state=1,
                   )
```

```python
# train network
test_limit = 50
train_limit = len(normalised_training_arrays) - test_limit

# Train the MLP on a subset of the images

MLP2.fit(normalised_training_arrays[:train_limit], labels[:train_limit])
```

```python
import matplotlib.pyplot as plt

plt.plot(MLP.loss_curve_)
plt.title("Loss curve for MLP.")
```

```python
def class_predict_from_image(MLP, img, quiet=True, zoomview=False,
                             confidence=False, signature=False):
    """Class prediction from an image."""
    flat_image = array_from_image(img).reshape(1, img.size[0]*img.size[1])

    if signature:
        _signature = generate_signature(img, linear=True)
        flat_signature = np.array(_signature).reshape(1, img.size[0]*4)
        normalised_flat_image = normalize(flat_signature, norm='max', axis=1)
    else:
        # We can normalise the values so they fall in the range 0..1
        normalised_flat_image = normalize(flat_image, norm='max', axis=1)
    
    if not quiet:
        if zoomview:
            zoom_img(img)
        else:
            display(img)

    if confidence:
        prediction_class_chart(MLP, normalised_flat_image)

    return MLP.predict(normalised_flat_image)[0]


# +

def predict_and_report_from_image(MLP, img, label='',
                                  jiggled=False, cropzoom=False,
                                  quiet=False, zoomview=False,
                                  confidence=False,
                                  signature=False):
    """Predict the class and report on its correctness."""
    if jiggled:
        img = jiggle(img)
    if cropzoom:
        img = crop_and_zoom_to_fit(img)

    prediction = class_predict_from_image(MLP, img, quiet=quiet,
                                          zoomview=zoomview, confidence=confidence, signature=signature)

    if label:
        print(f"MLP predicts {prediction} compared to label {label}; classification is {prediction == label}")
    else:
         print(f"MLP predicts {prediction}")

```

```python
# test network on single image
test_image, test_label = get_random_image()
predict_and_report_from_image(MLP2, test_image, test_label,
                              jiggled=False, quiet=False, confidence=False, signature=True)
```

```python
# test network on single image signature

test_image, test_label = get_random_image()
predict_and_report_from_image(MLP2, test_image, test_label,
                              jiggled=False, quiet=False, confidence=False, signature=True)
```

```python
# full test

test_and_report_random_images(MLP2, get_random_image, num_samples=100, signature=True)
```

Although we have reduced the amount of numbers that represent each row from 20 separate pixel values to just 4 signature values, we arguably have a much more powerful representation of the image that captures much of the useful *information* in the image.

In particular, casting the image to a black and white image removes potential variation arising from noise caused by greyscale pixel values. Counting the number of edges is invariant if we shift the image slightly to the left or the right in the sensor view; the first pixel value in the row also provides information as to whether the first transition is from white to black or black to white.




# TO DO - retrain and then try again with translated and zoomed images

# What effect might you expect if  we cropped the training images and then resized them to a fixed size before finding their signature?

```python

```
