---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

# 5 Simulating raising and lowering the light sensor


The *Sensor_Diameter_Test* background contains two sets of horizontal parallel lines and two sets of parallel vertical lines. The first group of lines are coloured black and have increasing thickness going down and across the page. The second group of lines also increase in thickness and are colored red.

We will use these different lines as a test bed for evaluating how different ‘height settings’ of the downward-facing light sensor affect its performance.


We will be investigating the data in the notebook, so before we get started, let’s just check the datalog is empty.


Run the following code cell to open the *Sensor_Diameter_Test* background in the simulator and place the robot at location `(420, 915)` and orientation `90`:

```python
%%sim_magic -b Sensor_Diameter_Test -x 420 -y 915 -a 90
# Set up the environment
```

You should see the robot is positioned with its sensors over crossing points of some black lines; a blue circle is also visible in view in each sensor display, which makes the lines look like cross hairs.

Click on the *Configure Robot* button. In the `sensor2` setting, set the `diameter` to 30 and click *Apply*. (If the robot is relocated, then click the *Move* button to move it back to the original location.)

The sensor diameter corresponds to the width of view of the sensor, which we are using to model the height of the sensor: if the sensor has a fixed diameter, then if we lift it up it will see more of the background. 

Increasing the diameter models the effect of raising the senor, and so the display for sensor&nbsp;2 appears to ‘zoom out’, and the circle looks smaller.

(Think what happens if you shine a torch against a wall. If you are far from the wall, then you may see a large blurry pool of light on the wall; as you walk towards the wall, the patch of light reduces in diameter and has sharper edges.)

You might also notice that the circle on the robot that identifies the sensor has also got larger.

If you change the `sensor2` diameter value to 10 and apply it, then you’ll notice the sensor as depicted on the robot gets smaller as we model the effect of the lowering the sensor and zooming in on the target.


<!-- #region activity=true -->
### Activity – Exploring the effect of raising and lowering the sensor

Set the value for the `sensor1` diameter to 30, and apply it, and leave the `sensor2` diameter value at 10. This will give the robot an eccentric set up, where one light sensor is mounted high and the other is mounted low.

The aim of this activity is to log the light sensor values as the robot drives across the test lines and see how the recorded data values compare. 

Display the the light sensor values directly in the simulator chart display (click *Show chart* then tick *Left light* and *Right light*), or grab the data values into the notebook datalog and view them in the notebook. If you analyse the values in the notebook, then you should make sure you clear the datalog before collecting any data from the simulator:
<!-- #endregion -->

```python activity=true
# Clear the datalog
roboSim.clear_datalog()
```

<!-- #region activity=true -->
Create your own program to drive the robot horizontally across the vertical bars, logging data from both light sensors as it does so. Drive the robot at least over all the black lines. Experiment with setting different speeds for the robot as it crosses the lines to see what effect, if any, that has on the readings you obtain.

The following code cell correctly configures the robot’s initial starting point as `(200, 645)` and orientation as `0`. Additionally, you can pass in `-r Sensor_Diameter_Config` if you want to set the sensor diameters automatically. <font color='red'>JD: I don't think -r Sensor_Diameter_Config is working for me (both diameters are (re)set to 20)...</font>
<!-- #endregion -->

```python student=true
%%sim_magic_preloaded -b Sensor_Diameter_Test -x 200 -y 645 -a 0
# YOUR CODE HERE

```

<!-- #region student=true -->
*Add your observations about the results, including the effect of the speed of the robot on the sensor values recorded. How might this effect the degree to which you can effectively control the robot?*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to view my program and sampled data.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
As well as viewing the data live by enabling the chart display and selecting the *Left light* and *Right light* traces, I’m also going to grab data into the datalog and then analyse it; so I’ll start by clearing the datalog.
<!-- #endregion -->

```python activity=true hidden=true
roboSim.clear_datalog()
```

<!-- #region activity=true hidden=true -->
For my program, I’m just going to drive the robot forwards, albeit relatively slowly, logging the data in an infinite while loop. As a stopping condition, I’ll break out of the while loop if I explicitly see red.

Note that in my stopping condition test, I have grabbed the sensor reading into a variable `sample` and then checked its components. If I test `colorRight.rgb[0]` and then `colorRight.rgb[1]` then there’s always a chance the `colorRight.rgb` value will have been updated between testing the first component and the second.
<!-- #endregion -->

```python activity=true hidden=true
%%sim_magic_preloaded -b Sensor_Diameter_Test -x 200 -y 645 -a 0 -r Sensor_Diameter_Config
colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

#Start off with a slowish speed of 20
speed = 20

tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))

while True:
    #Stopping condition on red line
    sample = colorRight.rgb
    if (sample[0]==255 and sample[1]<255):
        break
    
    intensity_left = colorLeft.reflected_light_intensity_pc
    intensity_right = colorRight.reflected_light_intensity_pc
    
    print('Light_left: ' + str(intensity_left))
    print('Light_right: ' + str(intensity_right))

    

```

<font color='red'>JD: Something odd happens when I run this. The robot's movement across the screen lags behind the light sensor readings, so it correctly stops when the light sensors see red, but the actual robot never reaches the red line on the background (it stops over the white, despite the sensors showing the thing red line).</font>

<!-- #region activity=true hidden=true -->
I can use the following code to grab the datalog into a dataframe:
<!-- #endregion -->

```python activity=true hidden=true
#Get the data
data = roboSim.results_log

#View as a dataframe
df = eds.get_dataframe_from_datalog(data)
df['time'] = df['index'].dt.total_seconds()
#Preview the data
df.head()
```

<!-- #region activity=true hidden=true -->
Using `seaborn` to display a line chart of the results, I can see that the traces from each sensor seem to differ:
<!-- #endregion -->

```python activity=true hidden=true
import seaborn as sns; sns.set()
ax = sns.lineplot(x="time",
                  y="value",
                  hue='variable',
                  style="variable",
                  markers=True, dashes=False,
                  data=df);

# Limit the x axis range ro get a better view of the chart
ax.set_xlim(1, 6);
```

<!-- #region activity=true hidden=true -->
In particular:

- the left-hand light sensor (`sensor1`, large diameter, raised high) has ‘smeared’ values and does not register very low values for the black lines
- the right-hand light sensor (`sensor2`, small diameter, closer to the background) has much ‘spikier’ values and does report much lower sensor readings when crossing the black lines.

If I speed up the robot, then the right-hand light sensor, which has a small diameter and is close to the ground, may miss the narrower black line altogether as it drives over the it.
<!-- #endregion -->

## 5.1 Trading off physical settings and code settings

In a real physical robot, we may be able to tune elements of the physical set-up, as well as the code, to get the robot to perform as we require.

As designers and engineers, it may often be the case that a problem that is hard to solve in one domain – for example, in the creation of a computer control program – can be simplified by making changes to the physical robot.

On the other hand, we may be able to accommodate fiddly aspects of a robot’s physical set-up by simple software fixes.

We can model a similar sort of interaction in the simulator by varying elements of the robot configuration as well as program parameters.

<!-- #region activity=true -->
### Open challenge – Exploring the effect of the light sensor diameter on the line-following behaviour

Using the `Lollipop` background and the program you previously created to complete the associated challenge, modify the light sensor setting of the sensor you have used in your program and re-run it.

Does increasing or decreasing the diameter of the sensor affect the performance of the program?

Are there any changes you can make in the program to compensate for changes in the robot’s physical sensor configuration?
<!-- #endregion -->

```python student=true
%%sim_magic_preloaded --background Lollipop

# YOUR CODE HERE
```

<!-- #region student=true -->
*Your notes and observations here.*
<!-- #endregion -->

<!-- #region activity=true -->
### Open challenge – Making this robot control strategy faster

Can you tune the robot’s physical set-up to allow you to write a program that allows the robot to more quickly complete the *Lollipop* challenge?
<!-- #endregion -->

<!-- #region activity=true -->
### Optional investigatory activity – The effect of simulated noise sensors of various diameters
<!-- #endregion -->

<!-- #region activity=true -->
You have already seen how sensor noise may affect the performance of a sensor and the performance of a software control program.

If you are curious, spend ten or fifteen minutes exploring how the different levels of sensor noise affect the ranges and ‘stability’ of readings you can get for sensors of different diameters or simulated heights above the background.
<!-- #endregion -->

## Summary

In this notebook, you have experimented with setting the diameter of the light sensor to model raising it or lowering it and changing its field of view over the background area.

You have seen how this physical setting may influence the performance of the sensor and the ability of the robot to perceive things in its environment that are used to determine the way the robot is controlled. 

You may also have explored how this setting affects the sensitivity of the sensor relative to a particular level of noise.
