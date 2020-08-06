---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# 1 Introduction


In the previous session, you had an opportunity to experiment hands-on with some neural networks. You may have finished that lab session wondering how neural networks can be built into real robots, particularly low-cost robots rather than expensive cutting-edge robots found only in research labs. In this session, you will find out.

The robot simulator we're using was originally designed to simulate the behaviour of a Lego Mindstorms EV3 controlled robot. The EV3 brick is excellent for introductory robotics, but it has limitations: it has a limited amount of memory, and it only supports integer arithmetic. This makes it impractical to train anything other than a small neural network on a Lego EV3 robot, although we may be able to use pre-trained models to perform "on-device" classification tasks. In general, we are often faced with the problem that we may want to run powerful programs on low-cost hardware that really isn't up to the job. Upgrading a robot with a more powerful processor might not be a solution because it adds cost and may demand extra electrical power. In turn, this might require a larger battery, which adds more weight. Which means you need more powerful electrical motors to move the robot, a bigger power supply to drive the motors, and more weight. You can probably see where this argument leads?!

A possible alternative is to think about a *multi-agent* systems approach, using a low-cost robot as a mobile agent to gather data and send that back to a powerful computer for processing. In a simple case we might have two agents: a Lego mobile robot and a personal computer (PC). We let the Lego robot do what it does best – move around while logging data – and then send the data back to the PC for processing. The PC processes the data using a trained neural network, or perhaps a complex rule based system, and sends back a message to the robot giving an appropriate response.

In this session, we will explore various ways in which our simulated robot can "offload" a task such as a recognition task to an external service operating elsewhere.

*ROS*, the *Robot Operating System*, provides one possible architecture for implementing such systems. In a ROS environment, separate *nodes* publish details of one or more *services* they can perform along with *topics* that act act as the nodes address that other nodes can subscribe. Nodes then pass messages between each other in order to perform a particular task. The ROS architecture is rather elaborate for our needs, however, so we shall use a much simpler and more direct approach.

In this session, we will use a slightly simpler approach, although one still based on message passing. To begin with, we will train a simple MLP network using the MNIST digits data in the Python environment attached to the notebook. We will then log image sensor data from the simulated robot and copy it into the notebook data log. From the data in the data log, we will then see if the MLP can recognise the digits.

After testing this approach, we will then explore a simple message passing protocol where the simulated robot sends a message to the Python environment containing the image sensor data, the data is run through the MLP, and the classification response is sent back to the simulated robot.


## Extracting MNIST Training Images From an Image Data File

The MNIST training data used by the various browser based neural network tools we have been using is itself stored in image files, with each row of the image file containing the 28 x 28 x 1 = 784 pixel values that represent each 28 x 28 pixel training image.

This is what one of the training data image files looks like:

![](mnist_batch_0.png)

At first glance, it doesn't look like a lot of handwritten digits, does it?

So let's investigate it a little bit more.

When displayed as an image, the image is 784 pixels wide and 3000 pixels high, which we can see from the size of the image if we load it in to Python as an image object:

```python
from PIL import Image

#Load in the image data file
img = Image.open('mnist_batch_0.png')

#If the image is a colour image, we can use various tools
#to convert it to a greyscale image
#.convert("L")

# Display the size of the image as (rows, columns)
img.size
```

This image itself contains 3000 lines of MNIST image data, corresponding to 3000 digit images. The 784 columns represent a linearised version of the $28 \times 28 = 784$ values that represent the values of each pixel in each `28x28` handwritten digit image:

```python
# If we convert the image data to a one dimensional array (i.e. a list of values)
# the first 784 elements will represent the contents of the first row
# That is, a linear representation of the the first 28x28 pixel sized handwritten digit image
print(list(img.getdata())[:784])
```

We can inspect the image object to see how the data has been encoded:

```python
img.getbands()
```

In this case, from the [documentation](https://pillow.readthedocs.io/en/4.1.x/handbook/concepts.html#modes), we see that mode `L` corresponds to a black and white image encoded with 8-bit pixels, defining each pixel as an integer with one of $2^8$ values, which is to say, an integer in the range `0..255` as can be seen from the preview of the first row of the image data.

What happens if we take one of these rows of data, cast it into its own 28x28 array, and render it as an image?

```python
import numpy as np

# Turn the image data into a multidimensional array
# of 3000 separate 28 x 28 arrays
images_array = np.array(img).reshape(3000, 28, 28)

#Get the first item, that is, the first 28x28 image data array
image_array = images_array[0]

# And convert it to an image
image_image = Image.fromarray(image_array)

# Then display it
image_image
```

To recap, the original *mnist_batch_0.png* file, which just happened to be an image file and could be viewed as such, was actually being used as a convenenient way of transporting 3000 rows of data. In turn, each row of data could itself be transformed into a square data array that could be then be rendered as a distinct handwritten digit image.


### Training a Simple MLP on the MNIST Image Data

Although MLP classifiers can struggle with large images, the 28x28 pixel image size used for the MNIST images is not too large to train an MLP on, although it does require an input layer containing 784 neurons, one for each pixel.

To train the MLP, we need to present labeled images that identify the category (that is, the digit) that each image represents.

The training labels are provided in a separate file which we can load in as follows:

```python
import json

# The labels.txt file contains 3000 digit labels in the same order as the image data file
with open('labels.txt', 'r') as f:
    labels=json.load(f)

# Show the length of the label array and the value of the digit
len(labels), labels[0]
```

Remembering that "code is a tool for building tools", we can create a simple Python function to display a handwritten image from the MNIST dataset, along with its label. The function accepts a single integer that is used as the index number for the image we want to display:

```python
def displayImageLabelPair(index):
    """Display the image and label for a MNIST digit by index value."""
    # The display() function is provided "for free" within Jupyter notebooks
    display(Image.fromarray(images_array[index]), labels[index])
```

We can then call the function as follows:

```python
displayImageLabelPair(176)
```

We can now train a simple MLP from the MNIST data and the training labels.

The SckitLearn `MLPClassifier` can automatically identify the number of nodes required for the input and output layers, so all we need to provide is the hiddent layer(s) definition.

For starters, let's see if we can make so with a single layer containing 50 hidden neurons:

```python
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(40), max_iter=30,
                    verbose=True,
                    #for reproducibility, set the random state
                    #random_state=1,
                   )
```

We need to present the data as a list (that is, as a one-dimensional linear array) of 784 values, each in the normalised range 0..1, rather than the 0..255 range they are currently in.

The data is currently in a `numpy` array containing 3000 square arrays, one per image:

```python
type(images_array), images_array.shape
```

We can apply a special method to the square arrays to "flatten" them to a one dimentional list: 

```python
from sklearn.preprocessing import normalize

flat_images = np.array(img).reshape(3000, 28*28)

normalised_flat_images = normalize(flat_images, norm='max', axis=0)
```

When training the network, we can use the first 2,900 images as a training set and hold back 100 images to use as a "previously unseen" image test set.

```python
mlp.fit(normalised_flat_images[:2900], labels[:2900])
```

With the network trained, we can check how well it performs on the training set using the classification report and cofusion matrix:

```python
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

predictions = mlp.predict(normalised_flat_images[:2900])

print(classification_report(labels[:2900], predictions))
print(confusion_matrix(labels[:2900], predictions))
```

If the network doesn't work perfectly in the recognition task against the data it is trained with, can you tune the network parameters and retrain the netwrok to improve its performance?

As well as testing the network against data it has already seen, we can also test it against images we held back and that it hasn't seen before. Once again, we can review the effectiveness of the netwrok by means of the classification report and confusion matrix:

```python
predictions = mlp.predict(normalised_flat_images[2900:])

print(classification_report(labels[2900:], predictions))
print(confusion_matrix(labels[2900:], predictions))
```

We can summarise the performance using the MLP `.score()` function:

```python
print("Training set score: {}".format(mlp.score(normalised_flat_images[:2900], labels[:2900])))
print("Test set score: {}".format(mlp.score(normalised_flat_images[2900:], labels[2900:])))
```

Once again, can you improve performance against these unseen items by tweaking the network parameters and retraining it?

Finally, in passing, we can plot the 28x28 incoming weights into the hidden layer neurons in a 28x28 grid to see how they filter the input values. You will notice that to human eyes at least, none of the input neurons has weights 

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(8, 5)
# use global min / max to ensure all weights are shown on the same scale
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
               vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```

```python
what if we mutliply the weights by the inputs?
```

```python
what if we mutliply the weights by the inputs
```

```python
mlp.coefs_[0].T.shape
```

```python
fig, axes = plt.subplots(8, 5)
# use global min / max to ensure all weights are shown on the same scale
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    # Mutliply inpyt by weight
    #coef=np.multiply(coef,flat_images[2])
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
               vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```

## `gradio` ??

```python
#!pip install gradio
# There are a lot of dependencies; try installing without deps
# and see if the minimal UI works.
```

## Using the MLP to Categorise Data Logged from the Simulator

The ??? background 

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

```python
roboSim.clear_datalog()
```

```python
%%sim_magic_preloaded -b MNIST_Digits

# how do we log the raw light sensor data to the datalog?


# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)


#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

print("image_data left")
```

```python
%%sim_magic_preloaded

# how do we log the raw light sensor data to the datalog?


# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

#Check the light sensor reading
while True:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity_pc
    # and display it
    if sensor_value < 50:
        print("image_data left")
```

```python

data = roboSim.image_data
data[0]
```

```python
import pandas as pd
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
df
```

```python
from PIL import Image
import numpy as np
tmp=df.iloc[14]['vals'].split(',')
#k=4
#del tmp[k-1::k]

vv = np.array(tmp).reshape(20, 20, 3).astype(np.uint8)
vvi = Image.fromarray(vv, 'RGB')
vvi
```

```python
#vvx = vvi.crop((3, 3, 17, 17)) 
vvx =vvi.resize((28, 28), Image.LANCZOS)
vvx
```

```python
from IPython.display import Image as I
from PIL import Image, ImageDraw
from numpy.random import randint


filename='_number_sheet.png'

mode = 'RGB'
size = (2362, 1143)
color = 'white'


img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)
img_cnt = len(images_array)


for i in range(20):
    for j in range(20):
        _img = randint(img_cnt)
        arr = images_array[_img]
        img_N = Image.fromarray(arr.reshape(28, 28), 'L')
        img_Ns = img_N.resize((14, 14), Image.LANCZOS)
        img.paste(img_Ns, (100+i*100, 50+j*100))
        #draw.text((100+i*100, 40+j*100), str(z[_img]), fill=(0,0,0))
        
        # We can draw a square with grey scale values that encode the training set value
        _x, _y = (100+i*100, 40+j*100)
        h = labels[_img] * 25
        draw.rectangle([(_x+38, _y+7), (_x+58, _y+30)], fill=(h,h,h))


img.save(filename)
I(filename)
```

```python
#https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html
import warnings

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier
```

```python
print(__doc__)

# Load data from https://www.openml.org/d/554

#So is X an array of pixels and y an array of labels
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X = X / 255.

# rescale the data, use the traditional train/test split
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]
```

```python
len(X), len(y)
```

![A diagram showing a robot and computer connected by a double ended arrow labelled ‘messages between the agents’.](../tm129-19J-images/tm129_rob_p9_f002.jpg)


Figure 1.1 The robot and the PC as a simple example of a two-agent system


The combination of just two agents like this creates a powerful example of a multi-agent system in which the performance of the agents is enhanced due to their interaction.

Communication between the agents is very important. The Lego RCX and PC can communicate with each other using infrared messages, similar to those sent by a TV remote control. An exchange of messages needs to be governed by a *protocol* that defines what the messages mean, and how the agents should take turns in sending and receiving. It should also handle cases where messages get lost, since no communication channel is fully reliable. For example, infrared messages could be lost if the robot wanders out of range or just faces the wrong way. We will consider a simple protocol in this session.

As always, in this session you will be working with Simon, our simulated autonomous robot, rather than a real mobile robot. Our two agents will therefore be Simon and RobotLab itself. Rather confusingly, both the simulation of Simon and RobotLab will be running on the same computer, so you will have to take it on trust that they are effectively independent and only communicate with the simple messages I explain below. There is no cheating, no hidden channel of communication!

In Robot Lab Session 8 you will experiment using the neural network on the PC to classify data on fruit, gathered by Simon. You will also experiment by training your own network to be used remotely by the robot.
<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Tip-->
Before running any of the programs in this session we recommend that you first switch off the ‘trace’ function. Do this with the `Run | Trace` menu item.<div style="background:lightblue"><p>Keyboard: Alt, R, A</p></div> (You will need to remember to do this each time you open a new program.) With the trace on, RobotLab will highlight the current statement, but this can be distracting with the long programs used here.
</div>


## Multi agent


Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 

The original RobotLab activities include examples of round-tripping, with the simulated robot passing state out to a remote application, which then returned a response to the simulated robot. I'm pretty sure we can do the same, either with a predefined application or a user defined function. The latter would be best because then we could have an activity to write a helper application in notebook python that is called on by the simulated robot.

At the moment, I have managed to send a message to Py from the simulator via messages sent to the simulator output window. There is a callback that sends messages back from Py to the sim output window, but as yet the robot py code running in the simulator is oblivious to returned messages. (I need half a day, perhaps, a day, to actually get code into the simulator so the programme code can access it.)

The following recipe shows how to overwrite the default collaborative `responder()` function with a custom one.

```python
#Get the simulator
from nbev3devsim import ev3devsim_nb as eds
%load_ext nbev3devsim

```

```python
# The responder callback function is called from the simulator code
# whenever something is written to the output window.
# see studio.js
class CollabSim(eds.Ev3DevWidget):
     def responder(self, obj):
        """ Callback function that tries to respond to widget."""
        # obj is the message sent from the simulator
        # we don't seem to see anything in obj?
        #Generate a response
        response = f'pingpongBONG {str(obj)}'
        #Send the response back to the simulator
        #At the moment, this is simply echoed in the simulator output window
        self.set_element("response", response)

# We now create an instance of the simulator with the custom collaborative callback function
roboSim = CollabSim()
```

```python
## seems like we need a handshake at first?
# First message doesn't get through?
roboSim.set_element("response", '')

display(roboSim)
roboSim.element.dialog()


roboSim.js_init("""
element.dialog({ "title" : "Robot Simulator" }).dialogExtend({
        "maximizable" : true,
        "dblclick" : "maximize",
        "icons" : { "maximize" : "ui-icon-arrow-4-diag" }});
""")
```

```python
%%sim_magic
print('helloasassddsa')
print('hello')
import time
for i in ['a','b','c']:
    time.sleep(0.02)
    print(i)
    print(i)
    time.sleep(0.02)
import ev3dev2_glue as glue


print('gs',glue.pyState())
time.sleep(1)
print('wtf?')
```

```python
#sim code - what does this do?

```

```python
%%sim_magic_preloaded
import time
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

gyro = GyroSensor(INPUT_4)


tank_drive.on(SpeedPercent(50), SpeedPercent(30))
time.sleep(0.1)

#print('left_motor_count'+tank_drive.left_motor.position_sp)
while int(tank_drive.right_motor.position)<1000:
    time.sleep(0.1)
    print('left_motor_count'+str(tank_drive.left_motor.position))
    print('right_motor_count'+str(tank_drive.right_motor.position))

```

```python

```
