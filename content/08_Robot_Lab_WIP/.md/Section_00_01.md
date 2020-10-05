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

# 1 Introduction


In the previous session, you had an opportunity to experiment hands-on with some neural networks. You may have finished that lab session wondering how neural networks can be built into real robots, particularly low-cost robots rather than expensive cutting-edge robots found only in research labs. In this session, you will find out.

The robot simulator we're using was originally designed to simulate the behaviour of a Lego Mindstorms EV3 controlled robot. The EV3 brick is excellent for introductory robotics, but it has limitations: it has a limited amount of memory, and it only supports integer arithmetic. This makes it impractical to train anything other than a small neural network on a Lego EV3 robot, although we may be able to use pre-trained models to perform "on-device" classification tasks.

In general, we are often faced with the problem that we may want to run powerful programs on low-cost hardware that really isn't up to the job. Upgrading a robot with a more powerful processor might not be a solution because it adds cost and may demand extra electrical power. In turn, this might require a larger battery, which adds more weight. Which means you need more powerful electrical motors to move the robot, a bigger power supply to drive the motors, and more weight. You can probably see where this argument leads?!

A possible alternative is to think about a *multi-agent* systems approach, using a low-cost robot as a mobile agent to gather data and send that back to a powerful computer for processing. In a simple case we might have two agents: a Lego mobile robot and a personal computer (PC). We let the Lego robot do what it does best – move around while logging data – and then send the data back to the PC for processing. The PC processes the data using a trained neural network, or perhaps a complex rule based system, and sends back a message to the robot giving an appropriate response.

In this session, we will explore various ways in which our simulated robot can "offload" a task such as a recognition task to an external service operating elsewhere.

*ROS*, the *Robot Operating System*, provides one possible architecture for implementing such systems. In a ROS environment, separate *nodes* publish details of one or more *services* they can perform along with *topics* that act act as the nodes address that other nodes can subscribe. Nodes then pass messages between each other in order to perform a particular task. The ROS architecture is rather elaborate for our needs, however, so we shall use a much simpler and more direct approach.

The approach we will use, although much simpler approach than the full ROS architecture, will also be based on a message passing approach. To begin with, we will train a simple MLP network using the MNIST digits data in the Python environment attached to the notebook. We will then log image sensor data from the simulated robot and copy it into the notebook data log. From the data in the data log, we will then see if the MLP can recognise the digits.

After testing this approach, we will then explore a simple message passing protocol where the simulated robot sends a message to the Python environment containing the image sensor data, the data is run through the MLP, and the classification response is sent back to the simulated robot.

<!-- #region -->
## Using a pre-trained MLP to categorise light sensor array data logged from the simulator

The *MNIST_Digits* simulator background includes various digit images from the MNIST dataset, arranged in a grid.

Alongside each digit is a grey square, where the grey level is used to encode the actual label associated with the image. (You can see how the background was created in the `Background Image Generator.ipynb` notebook.)

In this notebook, you will use the light sensor as a simple low resolution camera, working with the pixel array data rather then the single value reflected light value.

*Note that this functionionality is not supported by the real Lego light sensor.*


## TO DO - should we have a figure showing pushing the data?

Let's start by loading in the simulator:
<!-- #endregion -->

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

```python
%sim_magic -x 350
```

In order to collect the sensor image data, if the simulated robot program `print()` message starts with the word `image_data`, then we can send light sensor array data from the left, right or both light sensorts to a data log in the noteobok Python environment.

The `-R` switch in magic at the start of the following code cell will run the program in the simulator once it has been downloaded.  

```python
%%sim_magic_preloaded -b MNIST_Digits -O -R -x 400 -y 50

# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is a command invocation rather than a print statement
print("image_data left")
# The command is responded to by
# the "Image data logged..." message display
```

As we're going to be collecting data from the simulator into the notebook Python enviornment, we should take the precaution of clearing the notebook datalog before we start using it:

```python
roboSim.clear_datalog()
```

We can then run the data collection routine by calling a simple line magic that teleports the robot to a specific location, runs the data collection program (`-R`) and pushes the light sensor array data to the notebook Python environment:

```python
%sim_magic -R -x 400 -y 850

# Wait a moment to give data time to synchronise
import time
time.sleep(1)
```

We need to wait a few moments for the program to execute and the data to be sent to the notebook Python environment.

Note that this is a different approach to the one we used in an earlier notebook where we *pulled* a copy of the simple sensor datalog *from the simulator* into the notebook.

In the current example, the simulator is *pushing* the light sensor array data to the notebook each time the robot sends a particular message to the simulator output window.

With the data pushed from the simulator to the notebook Python environment, we should be able to see a dataframe containing the retrieved data:

```python
roboSim.image_data()
```

### Previewing the sampled sensor array

The data representing the image is a long list of RGB (red green, blue) valaues. We can generate an image from a the a specific row of the dataframe, given it the row index:

```python
from nn_tools.sensor_data import generate_image, zoom_img
index = -1 # Get the last image in the dataframe

img = generate_image(roboSim.image_data(), index, mode='rgb')
zoom_img(img)
```

<!-- #region tags=["alert-warning"] -->
If you don't see a figure image displayed, check that the robot is placed over a figure by reviewing the sensor array display in the simulator. If the image is there, rerun the previous code cell to see if the data is now available. If it isn't, rerun the data collecting magic cell, wait a view seconds, and then try to view the zoomed image display.
<!-- #endregion -->

We can check the color depth of the image by calling the `.getbands()` method on it:

```python
img.getbands()
```

As we might expect from the robot color sensor, this is a tri-band, RGB image.

Alternatively, we can generate an image directly as a greyscale image, either by setting the mode explicity or by omitting it (`mode=greyscale` is the default setting):

```python
img = generate_image(roboSim.image_data(), index)
zoom_img(img)

img.getbands()
```

The images we trained the network on were size 28 x 28 pixels. The raw images retrieved from the simulator sensor are slightly smaller, coming in at 20 x 20 pixels.

```python
img.size
```

The collected image also represents square profile around the "circular" sensor view. We might thus reasonably decide that we are going to focus our attention on the 14 x 14 square area in the centre of the collected image, with top left pixel `(3, 3)`.

```python
zoom_img(img)
```

One of the advantages of using the Python `PIL` package is that a range of *methods* (that is, *functions*) are defined on each image object that allow us to manipulate it *as an image*. (We can then also access the data defining the transformed image *as data* if we need it in that format.)

We can preview the area in our sampled image by cropping the image to the area of interest:

```python
img = generate_image(roboSim.image_data(), index,
                    crop=(3, 3, 17, 17))

display(img.size)
zoom_img( img )
```

In order to present this image as a test image to the trained MLP, we need to resize it so that it is the same size as the original training images (28 x 28 pixels).

We can do this by passing the desired size via the `resize` parameter, setting it either to a specified size, such as `resize=(28, 28)` (that is, 28 x 28 pixels) or back to the original, uncropped image size (`resize=('auto')`): 

```python
img = generate_image(roboSim.image_data(), index,
                    crop=(3, 3, 17, 17),
                    resize = (28, 28))

zoom_img( img )
```

### Collecting some sample images

The handwritten digit image centre locations on the *MINIST_Digits* simulator background can be found at the following locations:

- along rows `100` pixels apart, starting at `x=100` and ending at `x=2000`;
- along columns `100` pixels apart, starting at `y=50` and ending at `y=1050`.

We can collect the samples up a column by using line magic to teleport the simulated robot to each new location in turn and automatically run the program to log the sensor data.

To start, let's just check we can generate the required *y* values:

```python
# Generate a list of integers with desired range and gap
min_value = 50
max_value = 1050
step = 100

list(range(min_value, max_value+1, step))
```

Using this as a pattern, we can now create a simple script to clear the datalog, then iterate throug the desired *y* locations, using line magic to locate the robot at each step and run the already downloaded image sampling program.

To access the value of the iterated *y* value in the magic, we need to prefix it with a `$` when we refer to it. Note that we also use the `tqdm.notebook.trange` argument to define the range: this enhance the range iterator to provide an interactive progress bar that allows us to follw the progress of the iterator.

```python
# Provide a progress bar when iterating through the range
from tqdm.notebook import trange

# We need to add a short delay between iterations to give
# the data time to synchronise
import time

# Clear the datalog so we know it's empty
roboSim.clear_datalog()

for _y in trange(min_value, max_value+1, step):
    %sim_magic -R -x 100 -y $_y
    # Give the data time to synchronise
    time.sleep(1)
```

We can view the collected samples via a *pandas* dataframe:

```python
image_data_df = roboSim.image_data()
image_data_df
```

We can preview a specified row of the dataframe as zoomed in image:

```python
# Preview the last image in the dataframe
index = -1

zoom_img( generate_image(image_data_df, index) )
```

We can also convert the image to a black and white image by setting pixels above a specified threshold value to white (`255`), otherwise coloring the pixel black (`0`).

Run the following code cell to create a simple interactive application to explore this behaviour.

Experiment with using the *index* slide to select the image and the *threshold* slider to set the threshold value. 

Press the *Run Interact* button to see the effect of creating the black and white version of the selected image using the specified threshold value.

The *crop* checkbox allows you to just focus on the central area of the image; the *original* checkbox lets

```python
from nn_tools.sensor_data import generate_bw_image
from ipywidgets import interact_manual

@interact_manual(threshold=(0, 255),
                 index=(0, len(image_data_df)-1))
def bw_preview(index=0, threshold=200, crop=False):
    # Optionally crop to the centre of the image
    _crop = (3, 3, 17, 17) if crop else None
    _original_img = generate_image(image_data_df, index) 
    _demo_img = generate_bw_image(image_data_df, index,
                                  threshold=threshold,
                                  crop=_crop)
    zoom_img( _original_img)
    zoom_img( _demo_img )

    # Uncomment the following line to view the actual size images
    #display(_original_img, _demo_img)
```

## Loading in a previously save MLP model

Rather than train a new model, we can load in an MLP we have trained previously. Remember, when using a neural network model, we need to make sure that we know how many inputs it expects, which in our case matches the size of presented images.

You can either use the pretrained model that is provided in the same directory as this notebook (`mlp_mnist.joblib`), or use your own model created in an earlier notebook.

```python
# Load model
from joblib import load

MLP = load('mlp_mnist14x14.joblib')
```

```python
# Network inputs, hidden later sizes
MLP.n_features_in_,  MLP.n_layers_, MLP.n_outputs_, MLP.hidden_layer_sizes
#dir(MLP)
```

```python
MLP2 = load('mlp_mnist28x28.joblib')
import math
MLP2.n_features_in_, int(math.sqrt(MLP2.n_features_in_)), MLP2.n_layers_, MLP2.n_outputs_, MLP2.hidden_layer_sizes
#dir(MLP)
```

### Using the pre-trained classifier to recognise sampled images

What happens if we now try to recognise images sampled from the simulator light sensor array using our previously trained MLP classifier?

```python
# Get a random image index value
index = random.randint(0, len(image_data_df)-1)
        
# Generate the test image as a black and white image
test_image = generate_bw_image(image_data_df, index,
                               threshold=127,
                               crop=(3, 3, 17, 17))

# Display a zoomed version of the test image
zoom_img(test_image)

# Print the class prediction report
image_class_predictor(MLP, test_image);
```

How well did the classifier perform?

<!-- #region student=true -->
*Make your own notes and observations about the MLP's performance here. If anything strikes you as unusual, why do you think the MLP is performing the way it is?*
<!-- #endregion -->

We can create a simple interactive application to test the other images more easily:

```python
from nn_tools.network_views import image_class_predictor

@interact_manual(threshold=(0, 255),
                 index=(0, len(image_data_df)-1))
def test_image(index=0, threshold=200, show_image=False):
    # Create the test image
    test_image = generate_bw_image(image_data_df, index, 
                                   threshold=threshold,
                                   crop=(3, 3, 17, 17))
    
    # Generate class prediction chart
    image_class_predictor(MLP, test_image)
    
    if show_image:
        zoom_img(test_image)

```

In general, how well does the classifier appear to perform?

<!-- #region student=true -->
*Record your own notes and observations about the behaviour and performance of the MLP here.*
<!-- #endregion -->

<!-- #region activity=true -->
## Activity — Collecting image sample data at a specific location

Write a simple line magic command to collect the image data for the handwritten digit centred on the location `(600, 750)`.

Note that you may need to wait a short time between running the data collection program and trung to view it.

Display a zoomed version of the image in the notebook. By observation, what digit does it represent?

Using the `image_class_predictor()` function, how does the trained MLP classify the image? Does this match your observation?

Increase the light sensor noise in the simulator to its maximum value and collect and test the data again. How well does the network perform this time?
<!-- #endregion -->

```python student=true
# Your image sampling code here

```

```python student=true
# Your image viewing code here

```

<!-- #region student=true -->
*From your own observation, record which digit is represented by the image here.*
<!-- #endregion -->

```python student=true
# How does the trained MLP classify the image?

```

<!-- #region student=true -->
*How well does the prediction match your observation? Is the MLP confident in its prediction?*
<!-- #endregion -->

<!-- #region student=true -->
Increase the level of light sensor noise to it's maximum value and rerun the experiment:
<!-- #endregion -->

```python student=true
# Collect data with noise

```

```python student=true
# Preview image with noise

```

```python student=true
# Classify image with noise

```

<!-- #region student=true -->
*Your notes and observations on how well the network performed the classfication task in the presece of sensor noise.*
<!-- #endregion -->

<!-- #region activity=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true -->
We can collect the image data by calling the `%sim_magic` with the `-R` switch so that it runs the current program directly. We also need to set the location using the `-x` and `-y` parameters.
<!-- #endregion -->

```python activity=true
%sim_magic -R -x 600 -y 750
```

<!-- #region activity=true -->
To view the result, we can zoom the display of the last collected image in the notebook synched datalog.
<!-- #endregion -->

```python activity=true
index = -1 # Get data for the last image
my_img = generate_image(roboSim.image_data, -1)
zoom_img(my_img)
```

<!-- #region activity=true -->
By my observation, the digit represented by the image at the specified location is a figure `0`.

The trained MLP classifies the object as follows:
<!-- #endregion -->

```python
image_class_predictor(MLP, my_img)
```

###### Th matches my prediction

```python
## Activity — 
```

## Collecting digit image and class data from the simulator

If you look carefully at the *MNIST_Digits* background in the simulator, you will see that 

```python
%%sim_magic_preloaded -b MNIST_Digits -O -R -A -x 400 -y 50

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is a command invocation rather than a print statement
print("image_data both")
```

```python
from nn_tools.sensor_data import get_sensor_image_pair

# The sample we want from the logged image data
_index = 10

left_img, right_img = get_sensor_image_pair(roboSim.image_data, _index)

display(left_img, right_img)
```

## Activity — Collecting image sample data from the *MNIST_Digits* background

In this activity, you will need to collect sample data from the simulator to test the ability of the network to correctly identify 



#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*


## Activity

Briefly describe how you would train a network using this data in the form of a set of placeholder comments that might comment the steps an appropriate program would take. *You do not need to actually train the network, or write the code to train the network.*


#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*

```python
%%sim_magic -R
print("image_data left")
```

```python
dataX = roboSim.image_data()
dataX
```

```python
test_collected_imageX = collected_image(dataX, -)
image_class_predictor(MPL, test_collected_imageX)
```

Scaling filter so we have all sorts of other possible sources of confusion stepping in.


Predictions seem to be very very sensitive the central location of the digit? A single pixel change in direction around (426, 155) can result in completely different classifications.

## `gradio` ??

```python
#!pip install gradio
# There are a lot of dependencies; try installing without deps
# and see if the minimal UI works.
```

TO DO - could we train the data with some "jiggle" to the image, adding in black background for off-margin?

```python

```

```python
image_data_flat = np.array(image_data_df.iloc[0]['vals'].split(',')).astype(np.uint8)
len(image_data_flat), image_data_flat

```

```python
MLP.predict([list(resize_collected_image2.getdata())])[0]
```

```python
np.array(image_data_df.loc[0,'vals'].split)
```


## Trying to get a convolutional neural network (CNN) running

Although training a convolutional neural netwrok can take quite a lot of time, and a *lot* of computational effort, off-the-shelf pretrained models are also increasingly available. However, whilst this means you may be able to get started on a recognition task without the requirement to build your own model, *caveat emptor*: buyer beware. When you use a petrained model, you may not what data it ws trained against (and what biases it may include because of that), and you may not know what weaknesses there may be in the model.

<!-- #region tags=["alert-warning"] -->
As with any area of IT, privacy and security concerns must always be taken into account. With the increasing number of neural networks being deployed, they are starting to become attractive to attackers, although we will not be considering such matters in this module (for an example of related concerns, see *Biggio, B. and Roli, F., 2018. Wild patterns: Ten years after the rise of adversarial machine learning. Pattern Recognition, 84, pp.317-331* [[PDF](https://arxiv.org/pdf/1712.03141.pdf)]).

However, you should be aware when using third party models that they may incorporate risks and threats when you come to use them. For example, __risks__ associated with *bias* in the training data used to train the network, or in its final trained performance; or __threats__ in terms of incorporating patterns that are deliberately misidentifed compared to how you might ordinarily expect them to be identified.
<!-- #endregion -->

The following example uses a pretrained convolutional neural network model implemented as a TensorFlow Lite model. [*TensorFlow Lite*](https://www.tensorflow.org/lite/) is a framework developed to support the deployment of TensorFlow Model on internet of things (IoT) devices. As such, the models are optimised to be as small as possible and to be evaluated as computationally quickly and efficiently as possible.

```python

```

```python
from nn_tools.network_views import cnn_load
from nn_tools.network_views import cnn_get_details
from nn_tools.network_views import cnn_test_with_image
from nn_tools.network_views import cnn_rank_results

cnn = cnn_load(fpath='./mnist.tflite',
               fpath_labels='./mnist_tflite_labels.txt')
```

```python
cnn_get_details(cnn)
```

```python
from nn_tools.sensor_data import jiggle

index = 3
cnn_test_image = generate_image(image_data_df, index, crop=(3, 3, 17, 17)).resize((28, 28))
cnn_test_image2 = jiggle(cnn_test_image)

display(cnn_test_image, cnn_test_image2)
```

```python
# Pass retval=True to return the results values
# pass rank=N to print top N ranked results
cnn_test_with_image(cnn, cnn_test_image2, retval=True)
```

```python
# test 20x20 MLP2
image_class_predictor(MLP2, cnn_test_image2);
```

## Logging lots of data


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
tmp=df.iloc[14]['vals'].split(',')
#k=4
#del tmp[k-1::k]

vv = np.array(tmp).reshape(20, 20, 3).astype(np.uint8)
vvi = Image.fromarray(vv, 'RGB')
vvi
```

```python
#vvx = vvi.crop((3, 3, 19, 19)) 
vvx =vvi.resize((28, 28), Image.LANCZOS)
vvx
```

### Communicating between sim and robot


![A diagram showing a robot and computer connected by a double ended arrow labelled ‘messages between the agents’.](../tm129-19J-images/tm129_rob_p9_f002.jpg)


Figure 1.1 The robot and the PC as a simple example of a two-agent system


The combination of just two agents like this creates a powerful example of a multi-agent system in which the performance of the agents is enhanced due to their interaction.

Communication between the agents is very important. The Lego RCX and PC can communicate with each other using infrared messages, similar to those sent by a TV remote control. An exchange of messages needs to be governed by a *protocol* that defines what the messages mean, and how the agents should take turns in sending and receiving. It should also handle cases where messages get lost, since no communication channel is fully reliable. For example, infrared messages could be lost if the robot wanders out of range or just faces the wrong way. We will consider a simple protocol in this session.

As always, in this session you will be working with Simon, our simulated autonomous robot, rather than a real mobile robot. Our two agents will therefore be Simon and RoboLab itself. Rather confusingly, both the simulation of Simon and RoboLab will be running on the same computer, so you will have to take it on trust that they are effectively independent and only communicate with the simple messages I explain below. There is no cheating, no hidden channel of communication!

In Robot Lab Session 8 you will experiment using the neural network on the PC to classify data on fruit, gathered by Simon. You will also experiment by training your own network to be used remotely by the robot.
<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Tip-->
Before running any of the programs in this session we recommend that you first switch off the ‘trace’ function. Do this with the `Run | Trace` menu item.<div style="background:lightblue"><p>Keyboard: Alt, R, A</p></div> (You will need to remember to do this each time you open a new program.) With the trace on, RoboLab will highlight the current statement, but this can be distracting with the long programs used here.
</div>


## Multi agent


Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 

The original RoboLab activities include examples of round-tripping, with the simulated robot passing state out to a remote application, which then returned a response to the simulated robot. I'm pretty sure we can do the same, either with a predefined application or a user defined function. The latter would be best because then we could have an activity to write a helper application in notebook python that is called on by the simulated robot.

At the moment, I have managed to send a message to Py from the simulator via messages sent to the simulator output window. There is a callback that sends messages back from Py to the sim output window, but as yet the robot py code running in the simulator is oblivious to returned messages. (I need half a day, perhaps, a day, to actually get code into the simulator so the program code can access it.)

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
