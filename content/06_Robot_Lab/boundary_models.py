# +
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.neural_network import MLPClassifier

from PIL import Image
import tempfile
import os

from tqdm.notebook import tqdm

import IPython.display


# -

def plot_boundaries(model, df, response=False, Xdata='Input', ydata='Fruit', ymap=None):
    
    classes = np.unique(df[ydata])
    
    if ymap is None:
        ymap = {'Strawberry': 'red', 'Pear': 'green', 'Orange': 'black', 'Banana': 'magenta'}

    fig, ax = plt.subplots()
    plt.style.use('ggplot')
    #Via https://towardsdatascience.com/easily-visualize-scikit-learn-models-decision-boundaries-dd0fb3747508
    #Plot the decision boundaries of a classification model.

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].    


    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = 0, 10
    y_min, y_max = 0, 5

    # Meshgrid creation
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh using the model.
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])    

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    # Predictions to obtain the classification results
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # Plotting
    contour_colours = ['red', 'green', 'blue', 'orange', 'pink', 'magenta', 'cyan']
    ax.contourf(xx, yy, Z, colors= contour_colours[:len(classes)], alpha=0.2)


    for f in df[ydata]:
        tmp = pd.DataFrame(df[Xdata].to_list(), columns=['x', 'y'])
        ax.scatter(tmp['x'], tmp['y'], s=100,
                    c =df[ydata].map(ymap),
                    marker='*', 
                    alpha=0.8)
    plt.xlabel("x",fontsize=15)
    plt.ylabel("y",fontsize=15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14);

    if response:
        return fig, ax


def mlp_boundary_animate(df, Xdata='Input', ydata='FruitNum',
                         size=(6, 6), iterations=1000, every=100, fname='animation.gif', show=True):
    model = MLPClassifier(hidden_layer_sizes=size)

    num_iterations = iterations

    # Get a list of all the classes
    classes = np.unique(df[ydata])

    with tempfile.TemporaryDirectory() as tmpdirname:
        for i in tqdm(range(num_iterations)):
            # In the partial_fit(), we need to declare up front what all the possible classes are
            # This is because we could present different training classes at each step
            model.partial_fit(df[Xdata].to_list(), df[ydata], classes)

            # for every 100 iterations, display the result
            # A simple way to do this is to divide the iteration count by 100
            #  and see if there's a remainder...
            if (i==0) or ((i+1) % every == 0):
                predictions = model.predict(df[Xdata].to_list())

                # Generate the boundary plot
                fig, ax = plot_boundaries(model, df, True)
                plt.savefig(os.path.join(tmpdirname, f'frame_{i}.png'))
                # Prevent the repeated display of the figure at the end
                plt.close(fig)

        ims = []
        for i in range(num_iterations):
            if (i==0) or ((i+1) % every == 0):
                im = Image.open(os.path.join(tmpdirname, f'frame_{i}.png'))
                ims.append(im)

    im.save(fname, save_all=True, append_images=ims, loop=0)
    
    if show:
        display(IPython.display.Image(fname))

    return model
