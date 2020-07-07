import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_boundaries(model, df):
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
    plt.contourf(xx, yy, Z, colors= ['red', 'green', 'blue', 'orange'], alpha=0.2)


    for f in df["Fruit"]:
        tmp = pd.DataFrame(df["Input"].to_list(), columns=['x', 'y'])
        plt.scatter(tmp['x'], tmp['y'], s=100,
                    c =df['Fruit'].map({'Strawberry': 'red', 'Pear': 'green', 'Orange': 'black', 'Banana': 'magenta'}),
                    marker='*', 
                    alpha=0.8)
    plt.xlabel("x",fontsize=15)
    plt.ylabel("y",fontsize=15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14);