# +
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

from sklearn.preprocessing import normalize

import pandas as pd

# -

def reshape_data(img):
    # Turn the image data into a multidimensional array
    # of 3000 separate 28 x 28 arrays
    images_array = np.array(img).reshape(3000, 28, 28)

    flat_images = np.array(img).reshape(3000, 28*28)
    
    normalised_flat_images = normalize(flat_images, norm='max', axis=1)
    
    return images_array, flat_images, normalised_flat_images


def preview_weights(MLP, ):
    #Create a grid of image axes
    fig, axes = plt.subplots(8, 5)

    # Get the axes in the form of a list
    axes_list = axes.ravel()

    # Find the global min / max value to ensure all weights are shown on the same scale
    vmin, vmax = MLP.coefs_[0].min(), MLP.coefs_[0].max()

    #Iterate through MLP node weights, plotting each set in its own figure
    for coef, ax in zip(MLP.coefs_[0].T, axes_list):
        weights_28x28_array = coef.reshape(28, 28)
        #We can display the weight array as a matrix in a new figure window.
        ax.matshow(weights_28x28_array, cmap=plt.cm.gray, vmin=.5 * vmin,
                   vmax=.5 * vmax)

        # Remove axis tick marks for a cleaner display
        ax.set_xticks(())
        ax.set_yticks(())

    plt.show()


# +
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


def test_display(MLP, sample, label):
    """Test an input on a classifier and display the result"""
    display(f'Expected label: {label}')
    display(f'Input image {Image.fromarray(sample)}')
    display(pd.DataFrame(MLP.predict_proba([sample])).T.plot(kind='bar'))
