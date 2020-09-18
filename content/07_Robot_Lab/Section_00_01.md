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

# 1 Introduction


In the previous session, you had an opportunity to experiment hands-on with some neural networks. You may have finished that lab session wondering how neural networks can be built into real robots, particularly low-cost robots rather than expensive cutting-edge robots found only in research labs. In this session, you will find out.

The robot simulator we're using was originally designed to simulate the behaviour of a Lego Mindstorms EV3 controlled robot. The EV3 brick is excellent for introductory robotics, but it has limitations: it has a limited amount of memory, and it only supports integer arithmetic. This makes it impractical to train anything other than a small neural network on a Lego EV3 robot, although we may be able to use pre-trained models to perform "on-device" classification tasks.

In general, we are often faced with the problem that we may want to run powerful programs on low-cost hardware that really isn't up to the job. Upgrading a robot with a more powerful processor might not be a solution because it adds cost and may demand extra electrical power. In turn, this might require a larger battery, which adds more weight. Which means you need more powerful electrical motors to move the robot, a bigger power supply to drive the motors, and more weight. You can probably see where this argument leads?!

A possible alternative is to think about a *multi-agent* systems approach, using a low-cost robot as a mobile agent to gather data and send that back to a powerful computer for processing. In a simple case we might have two agents: a Lego mobile robot and a personal computer (PC). We let the Lego robot do what it does best – move around while logging data – and then send the data back to the PC for processing. The PC processes the data using a trained neural network, or perhaps a complex rule based system, and sends back a message to the robot giving an appropriate response.

In this session, we will explore various ways in which our simulated robot can "offload" a task such as a recognition task to an external service operating elsewhere.

*ROS*, the *Robot Operating System*, provides one possible architecture for implementing such systems. In a ROS environment, separate *nodes* publish details of one or more *services* they can perform along with *topics* that act act as the nodes address that other nodes can subscribe. Nodes then pass messages between each other in order to perform a particular task. The ROS architecture is rather elaborate for our needs, however, so we shall use a much simpler and more direct approach.

The approach we will use, although much simpler approach than the full ROS architecture, will also be based on a message passing approach. To begin with, we will train a simple MLP network using the MNIST digits data in the Python environment attached to the notebook. We will then log image sensor data from the simulated robot and copy it into the notebook data log. From the data in the data log, we will then see if the MLP can recognise the digits.

After testing this approach, we will then explore a simple message passing protocol where the simulated robot sends a message to the Python environment containing the image sensor data, the data is run through the MLP, and the classification response is sent back to the simulated robot.

## Using the trained MLP to categorise data logged from the simulator

The *MNIST_Digits* simulator background includes various digit images from the MNIST dataset, arranged in a grid.

Alongside each digit is a grey square, where the grey level is used to encode the actual label associated with the image. (You can see how the background was created in the `Background Image Generator.ipynb` notebook.)

Let's start by loading in the simulator:

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

In order to collect the sensor image data, if the print message starts with `image_data` then the left channel image is sent to the data log.

The `-R` switch in magic at the start of the following code cell will run the program in the simulator once it has been downloaded.  

```python
%%sim_magic_preloaded -b MNIST_Digits -O -R -x 400 -y 50

# how do we log the raw light sensor data to the datalog?


# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)


#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is a command invocation rather than a print statement
print("image_data left")
# The command is responded to by
# the "Image data logged..." message display
```

As we're going to be collecting data from the simulator into the notebook Python enviornment, we should take the precaution of clearing the datalog before we start using it:

```python
roboSim.clear_datalog()
```

We can then run the data collection routine by calling a simple line magic that teleports the robot to a specific location and runs the data collection program (`-R`):

```python
%sim_magic -R -x 400 -y 850
```

We need to wait a few moments for the program to execute and the data to be sent to the notebook Python environment. Then we should be able to see the data via the `roboSim.image_data` list:

```python
from nn_tools.sensor_data import generate_image, zoom_img
index = -1 # Get the last image in the dataframe

img = generate_image(roboSim.image_data, index)
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


If we are to try to recognise this image using our pretrained MLP, we need to pay careful attention to the format of the image as well as the dimensions of the collected images.

Let's start by casting the image to a single band greyscale image:

```python
img = img.convert('L')
img.getbands()
```

The images we trained the network on were size 28 x 28 pixels. The raw images retrieved from the simulator sensor are slightly smaller, coming in at 20 x 20 pixels.

```python
img.size
```

The collected image also represents square profile around the "circular" sensor view. We might thus reasonably decide that we are going to focus our attention on the 15 x 15 square area in the centre of the collected image, with top left pixel `(3, 3)` and bottom right pixel `(18, 18)`.

```python
zoom_img(img)
```

One of the advantages of using the Python `PIL` package is that a range of *methods* (that is, *functions*) are defined on each image object that allow us to manipulate it *as an image*. (We can then also access the data defining the transformed image *as data* if we need it in that format.)

We can preview the area in our sampled image by cropping the image to the area of interest:

```python
cropped_image = img.crop((3, 3, 18, 18));
                       
display(cropped_image.size)
zoom_img(cropped_image)
```

In order to present this image as a test image to the trained MLP, we need to resize it so that it is the same size as the training images:

```python
resized_cropped_image = cropped_image.resize((28, 28), Image.LANCZOS)
zoom_img(resized_cropped_image)
```

```python
image_class_predictor(MLP, resized_cropped_image);
```

```python
The `sensor_data.sensor_image_focus()` function will take an image, crop it to the central area, a
```

We can view the collected samples via a *pandas* dataframe:

```python
from nn_tools.sensor_data import process_robot_image_data

image_data_df = process_robot_image_data(roboSim.image_data)
image_data_df
```

The handwritten digit image centre locations on the *MINIST_Digits* simulator background can be found:

- along rows `100` pixels apart, starting at `x=100` and ending at `x=2000`;
- along columns `100` pixels apart, starting at `y=50` and ending at `y=1050`.

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
dataX = process_robot_image_data()
dataX
```

```python
test_collected_imageX = collected_image(dataX, -)
image_class_predictor(MPL, test_collected_imageX)
```

Scaling filter so we have all sorts of other possible sources of confusion stepping in.


Predictions seem to be very very sensitive the central location of the digit? A single pixel change in direction around (426, 155) can result in completely different classifications.

<!-- #region -->
## Testing the network on newly created images

To recap, we have trained our MLP on the 28x28 original pixel values used to represent each handwritten digit image and tested the trained network against some test images we held back from the original training set.



**how did it do on simulator? Can we break things further?**

But how robust is our network when it comes to classifying images that were perhaps not in the original dataset at all?

For example, will the network still recognise an image if we slightly recenter it in original image frame?
<!-- #endregion -->

### Creating synthetic data — translating an original image

We have already seen how we can get rid of the "background" columns and rows around the outside of an image using the `sensor_data.trim_image()` function.

For example, given the following raw image viewed as a dataframe:

```python
image_df = df_from_image(image_image)
```

we can trim it to size:

```python
trimmed_image_df = trim_image( image_df, background=0)
```

We can also convert this dataframe back to an image:

```python
from nn_tools.sensor_data import image_from_df

cropped_image = image_from_df(trimmed_image_df)
zoom_img( cropped_image )
```

We have already mentioned how the PIL Python package provides many useful tools for dealing with images as native images.

For example, as well as being able to crop images, if we create a blank image of size 28x28 pixels with a grey background, we can paste a copy of our cropped image into it.

```python
_grey_background = 200

_image_size = (28, 28)
_image_mode = 'L' #greyscale image mode

shift_image = Image.new(_image_mode, _image_size, _grey_background)

# Set an offset for where to paste the image
_xy_offset = (2, 6)

shift_image.paste(cropped_image, _xy_offset) 
zoom_img(shift_image)
```

Alternatively, we might zoom the cropped image back to the original image size. (The `Image.LANCZOS` setting defines a filter that is used to interpolate new pixel values in the scaled image based on the pixel values in the cropped image. As such, it may introduce digital artefacts of its own into the scaled image.)

```python
resized_image = cropped_image.resize(image_image.size, Image.LANCZOS)

display( resized_image.size)
zoom_img(resized_image)
```

The `nn_tools.sensor_data.crop_and_zoom_to_fit()` function does this in one step:

```python
from nn_tools.sensor_data import crop_and_zoom_to_fit

zoom_img( crop_and_zoom_to_fit(image_image) )
```

<!-- #region tags=["alert-success"] -->
Note that other image handling tools are available to us within the `PIL` package that allow us to perform other "native" image manipulating functions, such as cropping an image:

```python
# Define the limits of the crop operation

# Cut 6 pixel columns on lefthand edge
x0 = 6
# Cut 10 pixel columns on righthand edge
x1 = image_image.size[1] -10

# Leave the rows alone
y0 = 0
y1 = image_image.size[1]

crop_image = image_image.crop((x0, y0, x1, y1))
zoom_img(crop_image)
```
<!-- #endregion -->

To simplify creating translated images, the `sensor_data.jiggle()` function will accept an image and then return randomly translated version of it.

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
                              test_label, quiet=False)
```

<!-- #region activity=true -->
How does the trained MLP fare if we translate the image? Run the following cell several times and see if the MLP continues to classify the digit correctly. 
<!-- #endregion -->

```python activity=true
predict_and_report_from_image(MLP, test_image, test_label,
                              jiggled=True, quiet=False)
```

<!-- #region student=true -->
*Record your observations about how well the MLP performs against the translated images here. Why you think the network is performing the way it does?*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
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
                              cropzoom=True, quiet=False)
```

<!-- #region student=true -->
*Record your observations about how well the MLP performs against the translated images here. Why you think the network is performing the way it does?*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
When I tested the network against the resized images, I found that it wasn't very reliable at classifying them.

The original MLP has no real sense of how images are scaled across the presented image frame: it is looking for pixels that overlap the pixels representing the digit that were presented in the original training set.
<!-- #endregion -->

## Activity — Improving the performance of the network

__If the network doesn't work perfectly in the recognition task against the data it is trained with, try tuning the network parameters and retraining the network to see if you can improve its performance.__

Once again, can you improve performance against these unseen items by tweaking the network parameters and retraining it?

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
Security of models; not focus of this module but something to be aware of.
<!-- #endregion -->

```python
#https://www.tensorflow.org/lite/guide/python
#%pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_x86_64.whl
#https://github.com/frogermcs/MNIST-TFLite/blob/master/notebooks/mnist_model.tflite 
# downloaded mnist_model.tflite
import tflite_runtime.interpreter as tflite

interpreter = tflite.Interpreter(model_path='./mnist.tflite')

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# check the type of the input tensor
floating_model = input_details[0]['dtype'] == np.float32

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

input_details, output_details, height, width
```

```python
(tf_test_img, tf_test_label) = get_random_image()
test_img
```

```python
tf_test_img = tf_test_img.resize((width, height))
input_data = np.expand_dims(tf_test_img, axis=0)
if floating_model:
    input_data = (np.float32(input_data) - 127.5) / 127.5
```

```python
interpreter.set_tensor(input_details[0]['index'], input_data.reshape(input_details[0]['shape']))
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
results = np.squeeze(output_data)
results
```

```python
top_k = results.argsort()[-5:][::-1]

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
with open('mnist_tflite_labels.txt', 'r') as f:
    tf_labels = [line.strip() for line in f.readlines()]

#Plot the class predictions as a bar chart
pd.DataFrame(results).plot(kind='bar', legend=False,
                           title="Confidence score for each class")

for i in top_k:
    if floating_model:
        print('{:08.6f}: {}'.format(float(results[i]), tf_labels[i]))
    else:
        print('{:08.6f}: {}'.format(float(results[i] / 255.0), tf_labels[i]))
    
```


```python
#https://www.tensorflow.org/lite/guide/python
#%pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_x86_64.whl
#https://github.com/frogermcs/MNIST-TFLite/blob/master/notebooks/mnist_model.tflite 
# downloaded mnist_model.tflite
import tflite_runtime.interpreter as tflite

def cnn_load(fpath='./mnist.tflite',
             fpath_labels='./mnist_tflite_labels.txt'):
    """Load tensorflow lite model."""
    interpreter = tflite.Interpreter(model_path=fpath)

    interpreter.allocate_tensors()

    tf_labels = []
    if fpath_labels:
        with open(fpath_labels, 'r') as f:
            tf_labels = [line.strip() for line in f.readlines()]
        
    return (interpreter, tf_labels)

cnn = cnn_load()

def cnn_get_details(cnn):
    """Unpack details of tesnforflow-lite model."""
    (interpreter, tf_labels) = cnn
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # check the type of the input tensor
    floating_model = input_details[0]['dtype'] == np.float32

    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    return input_details, output_details, floating_model, height, width

#input_details, output_details, floating_model, height, width = cnn_get_details(cnn_interpreter)

def cnn_rank_results(results):
    """Display ordered list of top five cnn classification results."""
       
    top_k = results.argsort()[-5:][::-1]

    for i in top_k:
        if floating_model:
            print('{:08.6f}: {}'.format(float(results[i]), tf_labels[i]))
        else:
            print('{:08.6f}: {}'.format(float(results[i] / 255.0), tf_labels[i]))
    

def cnn_test_with_image(cnn, img, tf_labels='', retval=False):
    """Test an image against a pretrained tensorflow-lite CNN."""
    interpreter, _tf_labels = cnn
    if not tf_labels:
        tf_labels = _tf_labels
    
    display(img);

    input_details, output_details, floating_model, height, width = cnn_get_details(cnn)
    
    tf_test_img = img.resize((width, height))
    input_data = np.expand_dims(tf_test_img, axis=0)
    if floating_model:
        input_data = (np.float32(input_data) - 127.5) / 127.5
        
    interpreter.set_tensor(input_details[0]['index'],
                           input_data.reshape(input_details[0]['shape']))
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    results = np.squeeze(output_data)
 
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
    #Plot the class predictions as a bar chart
    if tf_labels and len(tf_labels)==len(results):
        results_df = pd.DataFrame(results, index=tf_labels)
    else:
        results_df = pd.DataFrame(results)

    results_df.plot(kind='bar', legend=False,
                    title="Confidence score for each class")
    if retval:
        return results

(test_img, test_label) = get_random_image()

cnn_test_with_image(cnn, test_img);

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

### Generate MNIST Output background

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
