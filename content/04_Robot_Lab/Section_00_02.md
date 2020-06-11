# 2 Line followers

In this section you will investigate how a robot can be made to follow a desired path as it navigates its environment.

When humans navigate around a house or a supermarket, most use the information provided by their eyes to control their movements. Many simple robots do not have complex vision systems like this and have to rely on much simpler sensors. One of the most commonly used methods for navigation by robots with simple light sensors is to follow a line.

The idea behind *line following* is that the environment has been adapted by the creation of a marked path that the robot can follow. For example, it could be a black line on a white background, or a wire embedded in the floor creating a magnetic field.

You will experiment with a number of robot navigation systems using the following strategy. In the first instance, instead of trying to follow a black line on a white background, we will instead follow the *edge* of a line that represents the sharp transition between black and white (or dark and light).

The basic idea is that, as the robot moves forwards, the light sensor tells it if it should move towards the edge or away from it. For example, if the light sensor picks up a light background, the robot needs to turn (say to the right) until it detects the dark line. Once the light sensor detects it is over the dark line, the robot should start moving forwards whislt also turning back to the left to find the edge of the line again. In this way, the robot would "edge" forwards as it follows the *right hand* edge of the black line.

The behaviour of the sensors and the interpretation of the data they provide is very important when creating line-following robots and we will look at these aspects in some detail.

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

## 2.1 Challenge: Writing an edge-follower program


The challenge is to write a RoboLab program to make the robot follow the line until it reaches the red bar. Make sure you still have the *Lollipop* background loaded in to the simulator. Before you can do the programming you will need to collect some data to calibrate the sensor responses to the various colours.

One approach to keeping the robot on track is to get it to read the light sensor. If the light sensor shows grey, the robot needs to turn back towards the edge of the line, that is, turn to its right. If it shows black then the robot is already over the black line and needs to turn back to the left to find the edge again.

(TO DO - FIX - The following image is rotated 90 degrees counter-clockwise compared to the bacground in the simulator.)

![The image used as a background for the line-follower program. This has a grey background on which is a lollipop shape, drawn hanging downward as a black outline. The robot starts at the stick, must follow the line across the screen to the left, around the head of the lollipop and back up the stick. The start/end is marked by a transverse broad red line; a transverse yellow line occurs mid way along the straight path. The yellow line is drawn behind the black lollipop so the black line is unbroken at this point; the red line is drawn across the end of the black line.](../images/tm129_rob_p6_f006.jpg)


The challenge is complicated by the presence of a yellow line, which the robot must ignore. 

### Calibrating the Required Sensor Readings

You first need to record the light sensor readings associated with each of the coloured bands on the chart, as well as for the black line and the grey background.

The backgound colours are represented as 3-tuple RGB (red-green-blue values). Each component is in the range 0..255 with a higher value showing an increased intensity of that component. A pure red color is 

### Activity

explore colors

```python
from PIL import Image, ImageDraw
Image.new('RGB', (50, 50), (0,255,0))
```

### Taking readings

The `reflected light` reading in the simulator is actually recorded as the value of the first RGB component, which is to say, the *red* component.

[TO DO - would the max value across all three channels make more sense? Or the median? Or the mean?] 

Drag the robot around the screen, dropping it so the left light sensor is directly over the area you want to record the sensor reading for. When you drop the robot, the light sensor reading should be updated in the simulator "Sensor readings" area.

 light sensorWhen the blue light sensor on Simon’s ‘nose’ is placed over an object, the control panel shows the light sensor reading for that object. Colours are made up of different amounts of red, blue and green. The simulator adds the red, green and blue values, and takes an average (i.e. it divides the total by three). For example, ‘yellow’ has red = 100%, green = 100%, and blue = 0%, so Simon sees this colour as 200/3 = 66 as a whole number (the simulator ‘rounds down’). Drag Simon over the background image and fill in a table like Table 2.1.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 2.1 Light sensor readings</caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan="">
grey:
</td>
<td class="highlight_" rowspan="" colspan="">
______ %
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
yellow:
</td>
<td class="highlight_" rowspan="" colspan="">
______ %
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
red:
</td>
<td class="highlight_" rowspan="" colspan="">
______ %
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
black:
</td>
<td class="highlight_" rowspan="" colspan="">
______ %
</td>
</tr>
</tbody>
</table>

Spend five to ten minutes writing a program to get Simon to navigate from its starting position along the black line and to stop at the red bar. Good luck!

Open `Line_follower` to see my version of the program code.


## Testing the Line Follower Against Other Lines

Use the `Line_Following_Test` background:

```python
%%sim_magic_preloaded -b Line_Following_Test

#Default programme from ev3devsim
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_4)
ultrasonic = UltrasonicSensor(INPUT_1)

GAIN = 0.5

while True:
    print('Gyro: ' + str(gyro.angle_and_rate))
    print('Ultrasonic: ' + str(ultrasonic.distance_centimeters))
    error = colorLeft.reflected_light_intensity - colorRight.reflected_light_intensity
    correction = error * GAIN
    steering_drive.on(correction, 20)
```

```python

```
