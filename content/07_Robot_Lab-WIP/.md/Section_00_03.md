---
jupyter:
  jupytext:
    formats: ipynb,.md//md
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

# 3. Training the MLP

In this notebook, you will be working with a very famous dataset known as the [MNIST database of handwritten images](http://yann.lecun.com/exdb/mnist/) (Modified National Institute of Standards and Technology database).

The complete dataset is composed of a training set of 60,000 example images, and a test set containing a further 10,000 examples. Each of the handwritten digit images have been "size-normalized" to the same image size. In addition, each sample digit has been centered within the fixed-size image.


## 3.1 Extracting MNIST training images from an image data file

The MNIST handwritten image dataset has been widely used for benchmarking the performance of different machine learning techniques, particularly in their early stages of development. It is also widely used for demonstration purposes, and you will meet several neural networks that were originally trained on the dataset in later notebooks.

In order to work with the dataset, we need to access it somehow. One common way of distributing the dataset is to encode all the handwritten digit image files, or batches or them, within another image file. In the example we will be working with, where each handwritten digit image is represented as a 28 x 28 pixel greyscale image, each row of the "distribution" image file contains the 28 x 28 x 1 = 784 pixel values that represent a single 28 x 28 pixel handwritten digit image.

This is what one of the distribution data image files looks like:

![](mnist_batch_0.png)

At first glance, it doesn't look like a lot of handwritten digits, does it?

So let's investigate that large image file a little bit more.

### 3.1.1 Importing the MNIST data image
When displayed as an image, the image is 784 pixels wide and 3000 pixels high, which we can see from the size of the image if we load it in to Python as an image object:

```python
from PIL import Image

#Load in the image data file
img = Image.open('mnist_batch_0.png')

#If the image is a colour image, we can use various tools
#to convert it to a greyscale image
#.convert("L")

# Display the size of the image as (rows, columns)
print(f'The image size, given as (columns, rows), is {img.size}.')
```

This image itself contains 3000 lines of MNIST image data, corresponding to 3000 separate handwritten digit images. The 784 columns in each row represent a linearised version of the $28 \times 28 = 784$ values that represent the values of each pixel in each `28 x 28` handwritten digit image.

We can preview what one of the rows looks like by running the following code cell:

```python
# If we convert the image data to a one dimensional array (i.e. a list of values)
# the first 784 elements will represent the contents of the first row
# That is, a linear representation of the the first 28 x 28 pixel sized handwritten digit image
print(list(img.getdata())[:784])
```

We can inspect the image object to see how the data has been encoded:

```python
img.getbands()
```

In this case, from the [`PIL` package documentation](https://pillow.readthedocs.io/en/4.1.x/handbook/concepts.html#modes), we see that mode `L` corresponds to a black and white image encoded with 8-bit pixels, defining each pixel as an integer with one of $2^8$ values, which is to say, an integer in the range `0..255`, as can be seen from the preview of the first row of the image data.


### 3.1.2 Extracting individual digit images

What happens if we take one of these rows of data, cast it into its own 28 x 28 array, and convert it to an image file format?

```python
import numpy as np

# Turn the image data into a multidimensional array
# of 3000 separate 28 x 28 arrays
images_array = np.array(img).reshape(3000, 28, 28)

#Get the third item (index value 2), that is, the third 28 x 28 image data array
image_array = images_array[2]

# And convert it to an image
image_image = Image.fromarray(image_array)

# Then display it
image_image
```

The `sensor_data.image_from_array()` function will also create the image for us using the same approach:

```python
from nn_tools.sensor_data import image_from_array

image_from_array(image_array)
```

We can zoom in on an image to look at it in more detail using the `nn_tools.sensor_data.zoom_img` function:

```python
from nn_tools.sensor_data import zoom_img

zoom_img(image_image)
```

We now see the handwritten digit not as series of numbers but as an actual image.


### 3.1.3 Viewing an individual digit image as data

We can also view the image data in a *pandas* dataframe, trimming the dataframe to remove background coloured edging.

*By default, the dataframe returning functions will preview the dataframe with colour highlight; pass the attribute `show=False` to disable this view.*

```python
from nn_tools.sensor_data import trim_image, df_from_image

trimmed_image = trim_image( df_from_image(image_image, show=False), background=0)
```

To recap, the original *mnist_batch_0.png* file, which just happened to be an image file and could be viewed as such, was actually being used as a convenient way of transporting 3000 rows of data. In turn, each row of data could itself be transformed into a square data array that could be then be rendered as a distinct handwritten digit image. The image itself, of course, is just numbers underneath...

### 3.1.4 So what?

At this point, you may be wondering what this has to do with training neural networks, let alone programming robots. What the example serves to demonstrate is that training a neural network on some test data may require a range of computer skills and knowledge to even get the data into a form where you can begin to make use of it.

Working with file formats and raw data representations often represents a large part of the workload associated with any data analysis, modelling, or classification task, and often requires significant computational data handling skills. Whilst we don't expect you to learn how to perform these data wrangling tasks yourself as part of this module, you should be aware then when you see recipes saying things like "*just load in the dataset...*", there may be quite a lot of work associated with that word, *just*.

*To learn more about working with data along the whole data pipeline, from data acquisition, to data cleaning, management, storage, analysis and presentation, consider taking the Open University module [__TM351 Data Management and Analysis__](http://www.open.ac.uk/courses/modules/tm351).*


## 3.2 Preparing the MNIST image training data

Although MLP classifiers can struggle with large images, the 28 x 28 pixel image size used for the MNIST images is not too large to train an MLP on, although it does require an input layer containing 784 neurons, one for each pixel.

To train the MLP on the linearised pixel values, we need to present labeled images that identify the category (that is, the digit) that each image represents.

The training labels are provided in a separate file which we can load in as follows:

```python
import json

# The labels.txt file contains 3000 digit labels in the same order as the image data file
with open('labels.txt', 'r') as f:
    labels=json.load(f)

# Show the length of the label array and the value of the first 10 digits
len(labels), labels[:10]
```

### 3.2.1 Grabbing random test images and their labels

Recalling the maxim that "code is a tool for building tools", we can define a function to retrieve a random image from the data set. The element of chance is provided by the Python `random` package. This package contains functions for creating a variety of different sorts of random numbers (floating point numbers, integers) within a specified range.

For example, we can create a random number in the range 0...3 using the `random.randint()` function, which takes lower and upper bounds on the range of integers to be returned as parameters:

```python
import random

random.randint(0, 100)
```

The following cell defines a function to retrieve a random image from the images array, or the image corresponding to the provided index value:

```python
def get_random_image(show=False, index=None):
    """Return a random image and label."""
    # Check that the length of the labels list
    # matches the length of the images array
    assert len(labels) == len(images_array)
    
    # If no index  value is provided,
    # generate a valid, random index value within the
    # bounds of the dataset array / list size
    if index is None:
        index = random.randint(0, len(images_array)-1)

    #Get the index'th item as a 28 x 28 image data array
    image_array = images_array[ index ]
    
    # Generate an image from the array
    image = Image.fromarray(image_array)

    # Get the corresponding label
    label = labels[index] 
    
    # If required, display the zoomed image
    if display:
        print(f"Image label: {label}")
        zoom_img(image)
        
    # Return the image,
    # along with the corresponding label
    return image, label
```

Run the following cell repeatedly to try the `get_random_image()` function out:

```python
(test_image, test_label) = get_random_image(show=True)
```

We also have access to the image and the label from the returned value assignment:

```python
print(f"Label: {test_label}")
zoom_img( test_image )
```

To access a particular image, such as the first image in the dataset, pass it's index:

```python
(test_image, test_label) = get_random_image(show=True, index=0)
```

## 3.3 Training a simple MLP on the MNIST image data

We can now train a simple MLP from the MNIST data and the training labels.

The *ScikitLearn* `MLPClassifier` can automatically identify from a training set the number of nodes required for the input and output layers, so all we need to provide is the hidden layer(s) definition.

### 3.3.1 Training the MLP

For starters, let's see if we can train the network to classify the images using a single layer containing 40 hidden neurons:

```python
from sklearn.neural_network import MLPClassifier

hidden_layer_sizes = (40)
max_iterations = 40

MLP = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iterations,
                    verbose=True,
                    # For reproducibility, set the inital random state to a specified seed value
                    #random_state=1,
                   )
```

We need to present the data as a list (that is, as a one-dimensional linear array) of 784 values, each in the normalised range 0..1, rather than the 0..255 range they are currently in.

The data is currently in a `numpy` array containing several thousand square arrays, one per image:

```python
type(images_array), images_array.shape
```

We can apply a special method to each of the square arrays to "flatten" each one to a separate one dimensional list. We can then normalise these values to get them into the value range 0..1: 

```python
from sklearn.preprocessing import normalize

# Get the dimensions of the images array as the number of images
# and each individual image array size
(array_n, array_x, array_y) = images_array.shape

# Create a list of "flat" images,
# where each image is represented as one dimensional list
# containing column*row individual pixel values
flat_images = images_array.reshape(array_n, array_x*array_y)

# We can normalise the values so they fall in the range 0..1
normalised_flat_images = normalize(flat_images, norm='max', axis=1)
```

When training the network, we can use the first 2,900 images as a training set and hold back 100 images to use as a "previously unseen" image test set.

```python
test_limit = 100
train_limit = len(normalised_flat_images) - test_limit

# Train the MLP on a subset of the images

MLP.fit(normalised_flat_images[:train_limit], labels[:train_limit])
```

<!-- #region tags=["alert-success"] -->
In defining the MLP originally, we specified a maximum number of training iterations, as well as the *verbose* reporting option. By default, a progress bar display is not available when training the MLP, but we can create one by defining a minimal MLP, training it on a single iteration to define the classes, and then training it across multiple iterations using the `.partial_fit()` method, which applies additional training iterations to the MLP.

This approach has been implemented as the function `network_views.progress_tracked_training()`:

```python
from nn_tools.network_views import progress_tracked_training

# Usage:
hidden_layer_sizes = (40)
max_iterations = 50

training_data = normalised_flat_images[:train_limit]
training_labels = labels[:train_limit]

# Create a new MLP
MLP = progress_tracked_training(training_data, training_labels,
                                hidden_layer_sizes=hidden_layer_sizes,
                                max_iterations=40)

# Top up an existing MLP
MLP = progress_tracked_training(training_data, training_labels,
                                MLP=MLP,
                                max_iterations=40)
```
<!-- #endregion -->

### 3.3.2 Testing the performance of the network

With the network trained, we can check how well it performs on the images in the training set using the classification report and confusion matrix:

```python
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

predictions = MLP.predict(normalised_flat_images[:train_limit])

print("Classification report:\n",
      classification_report(labels[:train_limit], predictions))
print("\n\nConfusion matrix:\n",
      confusion_matrix(labels[:train_limit], predictions))
```

If the *precision*, *recall* and *f1-score* values are close to 1, that's a good sign; and if large values predominate on the diagonal of the confusion matrix, that shows that most digits are identified correctly.

We can also test the trained MLP with a single image using a function of the following form:

```python
from nn_tools.sensor_data import array_from_image

def predict_from_image(MLP, image_and_class):
    """Test a trained MLP against a single image / class."""
    # Linearise the raw image data
    # as one dimensional list of values
    flat_image = array_from_image(image_image).reshape(1, image_image.size[0]*image_image.size[1])

    # Normalise the values in the list
    # to bring them into the range 0..1
    normalised_flat_image = normalize(flat_image, norm='max')

    # Display the image, along with prediction
    display(image_image, MLP.predict(normalised_flat_image))

```

Let's try it out:

```python
predict_from_image(MLP, image_image)
```

Or more conveniently, we can use the `nn_tools.network_views.predict_and_report_from_image()` function, in the following example testing against a randomly selected image and its classification label.

Omitting the test label will just return the prediction. A zoomed view of the sample image can be seen by setting `zoomview=True` when calling the function:

```python
from nn_tools.network_views import predict_and_report_from_image 

# Get a test image
(test_image, test_label) = get_random_image()
 
# And test the trained MLP against it
predict_and_report_from_image(MLP, test_image, test_label)
```

### 3.3.3 Probing the MLP's confidence in its predictions

Even though it may be hard for us to see from the network's weights exactly what is going on, the network appears to be doing its job in terms of classifying digits, at least when it comes to the sample images.

For example, by passing the `confidence=True` parameter to the `predict_and_report_from_image()` function, we can display a bar chart showing the confidence of the prediction for each class:

```python
predict_and_report_from_image(MLP, test_image, confidence=True)
```

### 3.3.4 Testing the MLP against multiple images

As well as testing the network against data it has already seen, we can also test it against images we held back and that it hasn't seen before. Once again, we can review the effectiveness of the network by means of the classification report and confusion matrix:

```python
predictions = MLP.predict(normalised_flat_images[train_limit:])

print(classification_report(labels[train_limit:], predictions))
print(confusion_matrix(labels[train_limit:], predictions))
```

We can summarise the performance using the MLP `.score()` function:

```python
print("Training set score: {}".format(MLP.score(normalised_flat_images[:train_limit], labels[:train_limit])))
print("Test set score: {}".format(MLP.score(normalised_flat_images[train_limit:], labels[train_limit:])))
```

*You will have an opportunity to explore other MLP configurations and training regimes later in this notebook to see if you can improve the performance of the network.*


### 3.3.5 Testing the MLP using multiple random images

The `nn_tools.network_views.test_and_report_random_images()` can be used to test the trained MLP against a specified number of samples, with samples picked by a specified function, such as our `get_random_image()` function:

```python
from nn_tools.network_views import test_and_report_random_images

test_and_report_random_images(MLP, get_random_image, num_samples=100)
```

## 3.6 Saving the MLP

We can persist the model by saving it to a file using a variant of the of Python `pickle` module, as described in the `scikit-learn` documentation](https://scikit-learn.org/stable/modules/model_persistence.html):


```python
from joblib import dump

dump(MLP, 'mlp_mnist_28x28.joblib') 
```

This is particularly important of we want to share the trained model, not least in situations where it may take some considerable time to train the model.

We can load it back in again in the following way:

```python
from joblib import load

MLP = load('mlp_mnist.joblib')

# Test that it still workks...
predict_and_report_from_image(MLP, test_image, test_label)
```

<!-- #region activity=true -->
## 3.7 Optional Activity — Visualising the trained MLP weights

*This is an experimental optional activity. It is still quite brittle. Click the arrow in the sidebar, or run this cell, to view the activity.*
<!-- #endregion -->

<!-- #region activity=true -->
In passing, we can plot the 28 x 28 incoming weights into the hidden layer neurons in a 28 x 28 grid to see how they filter the input values. The code is rather fiddly, so don't try to make too much sense of it. You will notice that to human eyes at least, none of the input neurons has weights that apparently encode directly for a particular handwritten integer (1, 2, 3 etc.).

Note that this only works at the moment for a single layer network with 40 hidden nodes.
<!-- #endregion -->

```python activity=true
from nn_tools.network_views import preview_weights

preview_weights(MLP)
```

<!-- #region activity=true -->
Things don't seem much clearer if we "present" a test image to the weights by multiplying each image pixel by its coreresponding input weight to each node:
<!-- #endregion -->

```python activity=true
from nn_tools.network_views import multiply_image_by_weights

image_number = 12 # References into the list of images contained in flat_images

# Use the actual image data
multiply_image_by_weights(MLP, img, labels, image_number)

# Use the normalised image data
multiply_image_by_weights(MLP, img, labels, image_number, normalised=True)
```

## 3.8 Summary


in the next -> Testing the network on newly created images

To recap, we have trained our MLP on the 28x28 original pixel values used to represent each handwritten digit image and tested the trained network against some test images we held back from the original training set.

But how robust is our network when it comes to classifying images that were perhaps not in the original dataset at all?

For example, will the network still recognise an image if we slightly recenter it in original image frame?
