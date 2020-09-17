# +
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

from sklearn.preprocessing import normalize

import pandas as pd

# -

def reshape_data(img, n_images=3000, size=(28, 28)):
    # Turn the image data into a multidimensional array
    # of 3000 separate 28 x 28 arrays
    images_array = np.array(img).reshape(n_images, size[0], size[1])

    flat_images = np.array(img).reshape(n_images, size[0]*size[1])
    
    normalised_flat_images = normalize(flat_images, norm='max', axis=1)
    
    return images_array, flat_images, normalised_flat_images


# +
# TO DO - this doesn't work for arbitrary sized networks...

def preview_weights(MLP, size=(28, 28)):
    #Create a grid of image axes
    fig, axes = plt.subplots(8, 5)

    # Get the axes in the form of a list
    axes_list = axes.ravel()

    # Find the global min / max value to ensure all weights are shown on the same scale
    vmin, vmax = MLP.coefs_[0].min(), MLP.coefs_[0].max()

    #Iterate through MLP node weights, plotting each set in its own figure
    for coef, ax in zip(MLP.coefs_[0].T, axes_list):
        weights_NxM_array = coef.reshape(size[0], size[1])
        #We can display the weight array as a matrix in a new figure window.
        ax.matshow(weights_NxM_array, cmap=plt.cm.gray, vmin=.5 * vmin,
                   vmax=.5 * vmax)

        # Remove axis tick marks for a cleaner display
        ax.set_xticks(())
        ax.set_yticks(())

    plt.show()


# +
# TO DO - this doesn't work for arbitrary sized networks...

def multiply_image_by_weights(MLP, img, labels, image_number=0, normalised=False):
    """Function to display an input image and multiply it by node weights."""
    
    def multiplied_plot(images):
        fig, axes = plt.subplots(8, 5)
        # use global min / max to ensure all weights are shown on the same scale
        vmin, vmax = MLP.coefs_[0].min(), MLP.coefs_[0].max()
        for coef, ax in zip(MLP.coefs_[0].T, axes.ravel()):
            # Multiply input by weight
            coef = np.multiply(coef, images[image_number])
            ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
                       vmax=.5 * vmax)
            ax.set_xticks(())
            ax.set_yticks(())

        plt.show()
    
    images_array, flat_images, normalised_flat_images = reshape_data(img)

    displayImageLabelPairFromArray(images_array, labels, image_number)
    if normalised:
        multiplied_plot(normalised_flat_images)
    else:
        multiplied_plot(flat_images)


# -

def displayImageLabelPairFromArray(images_array, labels, index):
    """Display the image and label for a MNIST digit by index value."""
    # The display() function is provided "for free" within Jupyter notebooks
    display( Image.fromarray(images_array[index]), labels[index])


def _test_display(MLP, sample, label):
    """Test an input on a classifier and display the result"""
    display(f'Expected label: {label}')
    display(f'Input image {Image.fromarray(sample)}')
    display(pd.DataFrame(MLP.predict_proba([sample])).T.plot(kind='bar'))


def test_display(MLP, img, label):
    """Test an image against a pretrained classifier and display the result"""
    flat_image = array_from_image(img).reshape(1, img.size[0]*img.size[1])
    normalised_flat_image = normalize(flat_image, norm='max', axis=1)
    
    # Get the prediction for likelihood of class membership as a dataframe
    _df = pd.DataFrame(MLP.predict_proba(normalised_flat_image)).T
    
    #Plot the class predictions as a bar chart
    _df.plot(kind='bar', legend=False, title="Confidence score for each class")
    
    # Report the actual and predicted class labels
    print(f'Actual label: {label}')
    print(f'Predicted label: {MLP.predict(normalised_flat_image)[0]}')
    
    # Display the sample as an image
    display(img)


# +
from sensor_data import array_from_image


def class_predict_from_image(MLP, img, quiet=True):
    """Class prediction from an image."""
    flat_image = array_from_image(img).reshape(1, img.size[0]*img.size[1])

    # We can normalise the values so they fall in the range 0..1
    normalised_flat_image = normalize(flat_image, norm='max', axis=1)
    
    if not quiet:
        display(img)

    return MLP.predict(normalised_flat_image)[0]


# +
from sensor_data import jiggle, crop_and_zoom_to_fit

def predict_and_report_from_image(MLP, img, label,
                                  jiggled=False, cropzoom=False,
                                  quiet=False):
    """Predict the class and report on its correctness."""
    if jiggled:
        img = jiggle(img)
    if cropzoom:
        img = crop_and_zoom_to_fit(img)

    prediction = class_predict_from_image(MLP, img, quiet=quiet)

    print(f"MLP predicts {prediction} compared to label {label}; classification is {prediction == label}")
