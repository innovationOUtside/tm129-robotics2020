---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,.md//md
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
---

<!-- #region -->
# 4 Recognising patterns on the fly



To be really useful a robot needs to recognise things as it goes along, or ‘on the fly’. In this notebook, you will train a neural network to use a simple MLP classifier to try to identify different shapes on the background. The training samples themselves, images *and* training labels, will be captured by the robot from the simulator background.

We will use the two light sensors to collect the data used to train the network:

- one light sensor will capture the shape image data;
- one light sensor will capture the training class data.

We will contrive things somewhat to collect the data at specific locations on the background.

Before continuing, ensure the simulator is loaded and available:
<!-- #endregion -->


```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds
%load_ext nbev3devsim
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

The `image_data left` invocation in the program downloaded to the simulator also logs a copy of the left sensor reading data as the last item (with index `-1`) in the `roboSim.image_data` list. We can preview that data as an image in the following way:

```python
from nn_tools.sensor_data import generate_image
index = -1

generate_image(roboSim.image_data(), index,
               crop=(3, 3, 17, 17),
               resize=(28, 28))
```

```python
from nn_tools.sensor_data import generate_image

index = -1

img = generate_image(roboSim.image_data, index)
img
```

If you don't see a figure image displayed, check that the robot is placed over a figure by reviewing the sensor array display in the simulator. If the image is there, rerun the previous code cell to see if the data is now available. If it isn't, rerun the data collecting magic cell, wait a view seconds, and then try to view the zoomed image display.


We can also use the `sensor_data.zoom_img()` function to zoom the display of an image generated from the sensor data grabbed into the notebook. The axes co-ordinates show the size, in pixels, of the image.

```python
from nn_tools.sensor_data import zoom_img

zoom_img(img)
```

The original sensor data is actually provided as a three channel data set, with the value for each pixel encoded as the three RGB (red, green, blue) channel values.

We can simplify the representation of the data by transforming the image to a black and white image, using a default (or explicity set) threshold value to decide whether a pixel should be represented as a black or white value.

```python
from nn_tools.sensor_data import generate_bw_image

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
from nn_tools.sensor_data import df_from_image

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
from tqdm.notebook import trange
from nbev3devsim.load_nbev3devwidget import tqdma

import time

roboSim.clear_datalog()

# x-coordinate for centreline of first shape
_x_init = 600

# Distance between shapes
_x_gap = 80

# Number of shapes
_n_shapes = 8

# y-coordinate for centreline of shapes
_y = 700

# Load in the required background
%sim_magic -b Simple_Shapes

# Generate x coordinate for each shape in turn
for _x in trange(_x_init, _x_init+(_n_shapes*_x_gap), _x_gap):
    
    # Jump to shape and run program to collect data
    %sim_magic -x $_x -y $_y -R
    
    # Wait a short period to allow time for
    # the program to run and capture the sensor data,
    # and for the data to be passed from the simulator
    # to the notebook Python environment
    time.sleep(1)

```

We should now be able to access multiple image samples via `roboSim.image_data()`, which returns a dataframe containing as many rows as images we scanned:

```python
image_data_df = roboSim.image_data()
image_data_df
```

One thing we can do to simplify the original sensor data is to convert the RGB sensor image with three colour channels for each pixel to a simpler black and white image where there is a single channel taking only two values: 0 for black, and 255 for white. 

```python
from nn_tools.sensor_data import generate_image
index = 3

zoom_img( generate_image(roboSim.image_data, index) )
```

```python
from nn_tools.sensor_data import generate_bw_image

zoom_img( generate_bw_image(roboSim.image_data, index))
```

We can then index into the data frame and render the `vals` data as an image for a specified row:

```python
from nn_tools.sensor_data import sensor_image_focus

zoom_img( sensor_image_focus(generate_image(roboSim.image_data, index)) )
```

So we have a focused image; to train on that, we also to grab the test pattern. If we print the message `"image_data both"` we can collect data from both the left and the right light sensors.

```python
%%sim_magic_preloaded -b Simple_Shapes -R -x 840 -y 700 -O

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is a command invocation rather than a print statement
print("image_data both")
```

We can then preview the last two rows of the dataframe to see the left and right logged sensor values:

```python
image_data_df = roboSim.image_data()
image_data_df[-2:]
```

```python
# training - not much data but train on it
```

```python
# testing -static
```

```python
# testing - dynamic?
```

The `nn_tools.sensor_data.get_sensor_image_pair` takes the original log data and grabs left and right sensor values based on the index of the left sensor value. (If no index is provided, the last two readings in the data log are inspected.)

The resulting images are converted to greyscale images and cropped to the central focus area of each sensor.

```python
from nn_tools.sensor_data import get_sensor_image_pair

# The sample we want from the logged image data
_index = 10

left_img, right_img = get_sensor_image_pair(roboSim.image_data, _index)

display(left_img, right_img)

```

The right sensor gives a uniform greyscale value. We can take the most common value (the *mode*) and use that to identify the class of the image.

```python
import numpy as np

np.mode(right_img.getdata())
```

We can use the following mapping to decode the actual shape from the training signal:

```python
shape_map = {'shape': value}
```

Generate training patterns:

```python
# training set
```

```python

```

```python
# train netwrok
```

```python
# test network
```

```python
# train on random images or random test track...
```

```python

```

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

![figure ../tm129-19J-images/tm129_rob_p9_f010.jpg](../tm129-19J-images/tm129_rob_p9_f010.jpg)


Figure 4.2 Two sets of scan lines of different lengths


A diagram showing sets of scan lines on a rectangle and diamond block. There are about four scan lines over the rectangle, appearing as arcs across it, all of equal length. The diamond has about six scan lines which are short at the point of the diamond, becomes much longer across the middle, and then become shorter towards the end of the diamond.

My data for the shapes in Figure 4.1 are given in Table 4.1.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 4.1 Scan data for shapes 1–4</caption>
<tbody>
<tr>
<th>
Shape
</th>
<th></th>
<th>
First circuit
</th>
<th>
Second circuit
</th>
<th>
Third circuit
</th>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">1</td>
<td class="highlight_" rowspan="" colspan=""> ![narrow rectangle](../tm129-19J-images/tm129_rob_p9_f011.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
7, 12, 13, 12, 13, 20, 0, 3
</td>
<td class="highlight_" rowspan="" colspan="">
9, 13, 14, 13, 12, 12, 3, 3
</td>
<td class="highlight_" rowspan="" colspan="">
8, 12, 12, 12, 12, 12, 3, 3
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">2</td>
<td class="highlight_" rowspan="" colspan=""> ![diamond](../tm129-19J-images/tm129_rob_p9_f012.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
4, 7, 11, 14, 17, 20, 14, 9
</td>
<td class="highlight_" rowspan="" colspan="">
3, 6, 8, 13, 16, 19, 13, 8
</td>
<td class="highlight_" rowspan="" colspan="">
3, 7, 10, 13, 16, 19, 13, 9
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">3</td>
<td class="highlight_" rowspan="" colspan=""> ![broad rectangle](../tm129-19J-images/tm129_rob_p9_f013.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
10, 20, 19, 19, 20, 3, 3, 3
</td>
<td class="highlight_" rowspan="" colspan="">
8, 17, 18, 17, 17, 3, 3, 3
</td>
<td class="highlight_" rowspan="" colspan="">
10, 17, 17, 16, 17, 3, 3, 3
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">4</td>
<td class="highlight_" rowspan="" colspan=""> ![circle](../tm129-19J-images/tm129_rob_p9_f014.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
5, 13, 19, 22, 21, 13, 3, 3
</td>
<td class="highlight_" rowspan="" colspan="">
6, 12, 17, 20, 18, 4, 3, 3
</td>
<td class="highlight_" rowspan="" colspan="">
4, 11, 17, 19, 19, 11, 3, 3
</td>
</tr>
</tbody>
</table>

Simon uses a neural network that I trained using these data. Once it has collected the scan data, it goes through the protocol in Figure 3.2, to receive the class code. When I trained the network I gave it class codes 1, 2, 3 and 4 for the shapes, using the numbering in Figure 4.1.

When the network sends back the recognition codes, it uses the ASCII values shown in Table 3.1: 49 (for 1), 50 (for 2), 51 (for 3), and 52 (for 4).


## 4.1 Activity — collecting scan data


Figure 4.3 shows a new set of blocks. In this activity you will collect data that will be used to train a neural network. Open the `Get_block_data` program. When you run this program it detects a shape and logs data for it.


![figure ../tm129-19J-images/tm129_rob_p9_f016.jpg](../tm129-19J-images/tm129_rob_p9_f016.jpg)


Figure 4.3 A set of blocks ready for collecting scan data


The background image for ‘Get block data’. This is a red track as before but with different black blocks as follows: 

1.  triangle (point towards Simon)

2.  very narrow rectangle, about twice the width of the track

3.  oval

4.  black line no wider than the track.

Position Simon as shown in Figure 4.3 and run the program. When Simon has moved across shape number 5 it will stop. Open the Data log window.

Click on the Upload  ![inlinefigure ../tm129-19J-images/tm129_rob_p9_f018.jpg](../tm129-19J-images/tm129_rob_p9_f018.jpg)  toolbar button or choose `Connect | Upload data log` to upload the data log<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, C, U</p></div> and then click on the `Data` tab so that you can see the logged data, as shown in Figure 4.4.


![figure ../tm129-19J-images/tm129_rob_p9_f019.png](../tm129-19J-images/tm129_rob_p9_f019.png)


Figure 4.4 Logged data for shape number 5


The Data log table view with the following values: 
<table xmlns:str="http://exslt.org/strings">
<caption></caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan=""> n </td>
<td class="highlight_" rowspan="" colspan=""> value </td>
<td class="highlight_" rowspan="" colspan=""> source </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 1 </td>
<td class="highlight_" rowspan="" colspan=""> 2 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 2 </td>
<td class="highlight_" rowspan="" colspan=""> 7 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> 9 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 4 </td>
<td class="highlight_" rowspan="" colspan=""> 13 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 5 </td>
<td class="highlight_" rowspan="" colspan=""> 16 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 6 </td>
<td class="highlight_" rowspan="" colspan=""> 21 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 7 </td>
<td class="highlight_" rowspan="" colspan=""> 25 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 8 </td>
<td class="highlight_" rowspan="" colspan=""> 6 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 9 </td>
<td class="highlight_" rowspan="" colspan=""> 0 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 10 </td>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 11 </td>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 12 </td>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 13 </td>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 14 </td>
<td class="highlight_" rowspan="" colspan=""> 3 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan=""> 15 </td>
<td class="highlight_" rowspan="" colspan=""> 23 </td>
<td class="highlight_" rowspan="" colspan=""> unknown </td>
</tr>
</tbody>
</table>

The program usually logs more than the eight measurements needed for the neural network. Small shapes may not require eight measurements, in which case the last measurements recorded are about 3 – corresponding to the red line.

Position Simon in front of each of the remaining three shapes to log data for them. I have done the first set of measurements for each shape in Table 4.2. Complete the table with two more sets of measurements for each shape.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 4.2 Scan data for shapes 5–8</caption>
<tbody>
<tr>
<th>
Shape
</th>
<th></th>
<th>
First circuit
</th>
<th>
Second circuit
</th>
<th>
Third circuit
</th>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">5</td>
<td class="highlight_" rowspan="" colspan=""> ![triangle](../tm129-19J-images/tm129_rob_p9_f020.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
2, 7, 9, 13, 16, 21, 25, 5
</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">6</td>
<td class="highlight_" rowspan="" colspan=""> ![narrow rectangle](../tm129-19J-images/tm129_rob_p9_f021.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
4, 6, 5, 5, 5, 5, 5, 5
</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">7</td>
<td class="highlight_" rowspan="" colspan=""> ![oval](../tm129-19J-images/tm129_rob_p9_f022.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
4, 11, 16, 21, 23, 23, 21, 13
</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">8</td>
<td class="highlight_" rowspan="" colspan=""> ![line](../tm129-19J-images/tm129_rob_p9_f023.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
4, 3, 4, 3, 3, 3, 3, 2
</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
</tbody>
</table>

```python
import pandas as pd

df = pd.DataFrame([['Pear', [5.2, 3.1]], ['Pear', [6.3, 2.4]],
                   ['Pear', [6.7, 1.8]], ['Pear', [5.3, 2.9]],
                   ['Banana', [8.5, 1.9]], ['Banana', [8.3, 1.6]],
                   ['Banana', [9.7, 2.0]], ['Banana', [7.5, 1.7]],
                   ['Strawberry', [2.1, 1.4]], ['Strawberry', [2.8, 1.8]],
                   ['Strawberry', [2.0, 1.8]], ['Strawberry', [2.2, 2.0]],
                   ['Orange', [4.7, 4.5]], ['Orange', [4.6, 4.2]],
                   ['Orange', [4.6, 4.1]], ['Orange', [4.0, 3.7]]
                  ],
                 columns = ['Fruit', 'Input'])

#Preview the first six rows
df.head(6)
```

```python
from sklearn.neural_network import MLPClassifier

fruit = MLPClassifier(hidden_layer_sizes=(6, 6), max_iter=20)
```

```python
# Fit the model
fruit.fit(df['Input'].to_list(), df['Fruit'])

#Check the prediction for each input
predictions = fruit.predict(df['Input'].to_list())
predictions
```

```python
from sklearn.metrics import classification_report

# The zero_division parameter suppresses a divide by zero warning when using zeroed parameters
print(classification_report(df['Fruit'], predictions, zero_division=False))
```

```python
from sklearn.metrics import confusion_matrix

print(confusion_matrix(df['Fruit'], predictions))
```

```python
from ipywidgets import interact

fruit = None

@interact(iterations=(100, 3000, 100), h1=(0, 10, 1), h2=(0, 10, 1))
def trainer(iterations=2000, h1=6, h2=6):
    global fruit
    fruit = MLPClassifier(hidden_layer_sizes=(h1, h2), max_iter=iterations)
    
    # Fit the model
    fruit.fit(df['Input'].to_list(), df['Fruit'])
    
    #Check the prediction for each input
    predictions = fruit.predict(df['Input'].to_list())

    print(classification_report(df['Fruit'], predictions))
    print(confusion_matrix(df['Fruit'], predictions))
```

## 4.2 Activity — training a neural network with the shape data


Start the `Neural network editor`. Click on `File | New Network`. Clear the `For existing data` check box. Change the number of inputs to 8, the number of outputs to 8, and set the number of neurons for the `1st hidden` and `2nd hidden` layers to 10 each, as shown in Figure 4.5(a). Then click `OK`. A warning box will be shown (Figure 4.5(b)); click `OK` to confirm that you are replacing previous training data.


![figure ../tm129-19J-images/tm129_rob_p8_f04_05a.png](../tm129-19J-images/tm129_rob_p8_f04_05a.png)


Figure 4.5 (a) `New Network` dialog box; (b) warning box


(a) A screen dump of the New network dialog. This has two panels and OK and Cancel buttons. The top panel has a prompt: ‘Number of nodes in each layer (0 if layer does not exist)’. This is followed by four labelled input fields: ‘Output layer’, ‘2nd hidden’, ‘1st hidden’ and ‘Input layer’. The lower panel has check boxes as follows: ‘For existing data’, ‘Scanner data’ and subsidiary to that ‘Use transitions’. 

(b) A warning alert box which reads: ‘The current training data will be removed! Do you want to proceed?’ followed by OK and Cancel buttons.

Use the outputs and labels in Table 4.3 together with the input data from Table 4.2 for your 12 data items. Remember to include spaces, not commas, when entering the data.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 4.3 Outputs for shapes 5–8</caption>
<tbody>
<tr>
<th>
Shape
</th>
<th></th>
<th>
Outputs
</th>
<th>
Item label
</th>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">5</td>
<td class="highlight_" rowspan="" colspan=""> ![triangle](../tm129-19J-images/tm129_rob_p9_f020.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
0, 0, 0, 0, 1, 0, 0, 0
</td>
<td class="highlight_" rowspan="" colspan="">
5
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">6</td>
<td class="highlight_" rowspan="" colspan=""> ![narrow rectangle](../tm129-19J-images/tm129_rob_p9_f021.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
0, 0, 0, 0, 0, 1, 0, 0
</td>
<td class="highlight_" rowspan="" colspan="">
6
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">7</td>
<td class="highlight_" rowspan="" colspan=""> ![oval](../tm129-19J-images/tm129_rob_p9_f022.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
0, 0, 0, 0, 0, 0, 1, 0
</td>
<td class="highlight_" rowspan="" colspan="">
7
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">8</td>
<td class="highlight_" rowspan="" colspan=""> ![line](../tm129-19J-images/tm129_rob_p9_f023.jpg) </td>
<td class="highlight_" rowspan="" colspan="">
0, 0, 0, 0, 0, 0, 0, 1
</td>
<td class="highlight_" rowspan="" colspan="">
8
</td>
</tr>
</tbody>
</table>

When you have entered your data, save the network with the name `my_net` in the `week-8` folder by clicking on `File | Save As …`. (The neural network editor will add the extension `nnd` to make the complete filename `my_net.nnd`.)

My data appeared as follows, but yours will be different:


![figure ../tm129-19J-images/tm129_rob_p9_f027.jpg](../tm129-19J-images/tm129_rob_p9_f027.jpg)

Sample training data from the Neural network editor list. 

 Tr 1:     2 7 9 13 16 21 25 5 » 0 0 0 0 1 0 0 0 ‘5’ 

 Tr 2:     4 6 5 5 5 5 5 5 » 0 0 0 0 0 1 0 0 ‘6’ 

 Tr 3:     4 11 16 21 23 23 21 13 » 0 0 0 0 0 0 1 0 ‘7’ 

 Tr 4:     4 3 4 3 3 3 3 2 » 0 0 0 0 0 0 0 1 ‘8’ 

 Tr 5:     2 6 8 11 15 21 24 6 » 0 0 0 0 1 0 0 0 ‘5’ 

 Tr 6:     4 6 5 5 5 5 5 5 » 0 0 0 0 0 1 0 0 ‘6’ 

 Tr 7:     4 12 17 21 23 22 19 3 » 0 0 0 0 0 0 1 0 ‘7’ 

 Tr 8:     2 3 3 3 3 3 3 3 » 0 0 0 0 0 0 0 1 ‘8’ 

 Tr 9:     3 6 9 13 17 21 25 4 » 0 0 0 0 1 0 0 0 ‘5’ 

 Tr 10:   4 6 5 5 5 5 5 5 » 0 0 0 0 0 1 0 0 ‘6’ 

 Tr 11:   3 13 18 22 23 23 19 1 » 0 0 0 0 0 0 1 0 ‘7’ 

 Tr 12:   3 3 3 3 3 3 3 3 » 0 0 0 0 0 0 0 1 ‘8’ 

Click on `Seed and Scale` and then `Cycle Until`. Your network should train, with all the training items correctly classified.

To save your trained neural network, click on `File | Save`. The trained network can now be used to classify new unseen data. This network will be used in the next activity. Make sure it has the name `my_net.nnd`, otherwise the next activity will not work properly.


## Preprocessing the Image Data

One of the problems with using the actual pixel data in a simple MLP is that the network can find it hard to recognise images from the actual raw pixel data: shapes may vary very slightly in size, orientation or framing within the sensor view area (eg they may be shifted to the left or right side of the sensor view, or the top or the bottom of it). These slight changes may cause large changes in the raw pixel values.

So can we use feature engineering to try to help improve matters? For example, might we represent the sensor data in some other way, and then train the MLP on the new representation with improved performance?

You may recall the fruit recognition activity from an earlier notebook. In that case, the various fruits were recognised based on physical properties of the each fruit in the form of the dimensions of the bounding box drawn around each one, rather than the actual picture of the fruit. The features used for training and recall in that case were thus the bounding box dimensions.

So can we perform a similar sort of re-presentation of the originally captured shape image data to create a derived set of features agains which we can train our MLP? 


## Activity — Using bounding box features for shape images 

Will the bounding box approach used to represent the fruit image data generate features that will allow us to distinguish between the shape images?

Running the following code cell will convert the raw data associated with an image to a data frame, and then prune the rows and columns the edges that only contain white space.

The dimensions of the dataframe, which is to say, the `.shape` of the dataframe, given as the 2-tuple `(rows, columns)`, corresponds to the bounding box of the shape. 

```python
from nn_tools.sensor_data import trim_image

index = 4

img = generate_bw_image(roboSim.image_data, index)
display(img)


trimmed_df = trim_image( df_from_image(img, show=False), reindex=True)

# dataframe shape
trimmed_df.shape
```

To try to provide a level of scale invariance, we should now scale the image to a known size. This will give us a signature with known number of features that we can use to train the network.

TO DO

```python
# TO DO
# resize to a standard size
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
- two of the arrows / equilateral triangles share the same dimensions (`(15, 13)`).

Only the rectange is clearly separated from the other shapes on the basis of its bounding box dimensions.


## Generating alternative training representations

In the previous notebook, feature engineering etc TO DO

```python
from nn_tools.sensor_data import generate_signature_from_series

bw_df.apply(generate_signature_from_series, axis=1)
```

## 4.3 Activity — running the simon–pc two-agent system


Open the `Classify_my_block_data` program. The configuration for this program assumes that the file `my_net.nnd` which you previously created is in the same folder; that is, `week-8`. The simulation window will show the objects in <a xmlns:str="http://exslt.org/strings" href="">Figure 4.3</a>. Place Simon in front of the triangular object, as shown in Figure 4.3, and run the program.

You should find that Simon scans the objects, stops, sends the data log to the PC, receives back a classification, recognises the object, and says the correct number, or says that the object was not recognised. If you run into problems, you can run the program using my trained neural network by running the `Classify_CT_block_data` program.

