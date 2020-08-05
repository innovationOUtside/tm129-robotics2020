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
<font color='red'>JD: Rename this notebook if the first two are merged.</font>

# 3 Emergent behaviour: Braitenberg’s vehicles


In Study week 2 you came across Valentino Braitenberg’s ideas on the behaviour of robots *emerging* from the way they are wired up. The figure belows shows two ways of connecting sensors to motors. In&nbsp;(a), the left sensor is connected to the left motor and the right sensor is connected to the right motor. In&nbsp;(b) these connections are reversed.


![Diagrams representing Braitenberg vehicles alongside simulated robots wired up in a similar fashion. A Braitenberg vehicle and our simulated robot are very similar: they have two wheels, one each side, and two light sensors, one on the left and one on the right of the front of the robot. A pair of Braitenberg vehicles are shown, one light avoiding and one light seeking. A light-avoiding vehicle has the left-hand light sensor connected to the left-hand motor and wheel, and the right-hand light sensor connected to the right-hand motor and wheel. A light-seeking vehicle has the left-hand light sensor connected to the right-hand motor and wheel, and the right-hand light sensor connected to the left-hand wheel. The simulated robots have wiring indicating identical connections. ](../images/tm129_rob_p4_f008.gif)


## 3.1 Activity: Testing Braitenberg’s vehicles


A ‘thought experiment’ suggests that the vehicle in figure&nbsp;(a) will move away from a light source. Similarly, another thought experiment suggests that the vehicle in figure&nbsp;(b) will move towards a light source. In the following activities you will test these predictions using an enivironment that models this set up, but uses downward-facing light sensors that take measurements from a ‘light gradient’ background, rather than forward-facing light sensors that look for a light source at ‘eye-level’ (that is, sensor-level!).


### Reconfiguring the robot

In order to detect different values from the light sensors on the right- and left-hand sides of the robot, we need to reconfigure the robot so that the sensors are placed further apart than they are in the default robot configuration.

In the simulator, select the *Radial_grey* background and tick the *Pen Down* checkbox.

You may notice that the simulator’s left and right light sensors appear to be further apart than they have been previously. This has been done via a change to the robot configuration setting that is applied automatically when the *Radial_grey* background is loaded.


#### Manually changing the robot configuration settings

You can manually increase the spacing between the sensors by:

- clicking the *Configure Robot* button in the simulator to open a window containing the robot configuration settings
- in the robot configuration settings window, scroll down to the `"sensor1"` parameters and change the `"x"` value from the default value of `-20` to the new value `-60`
- for `"sensor2"`, change the `"x"` value from its default value of `20` the new value `60`
- click the *Apply* button.

If you look at the robot in the simulator then you should notice that the two light sensors are now located nearer the sides of the robot and are no longer located close to the centreline.


#### Exploring the *Radial_grey* world

Run the following code cell to download the program to the simulator and then run it in the simulator. For now, don’t pay too much attention to the code: our initial focus is purely on what we can observe about the behaviour of the robot.

Observe what happens paying particularly close attention to the trajectory the robot follows.

Enter a new starting location in the simulator, changing the original Y&nbsp;value from `400` to the new value `600`. Click the *Move* button to move the robot to that location and run the simulator again. How does the robot move this time? 

```python
%%sim_magic_preloaded -b Radial_grey

def reflected_pc(reflected_val):
    """Return reflected value (range 0..255) as percentage."""
    return 100.*reflected_val / 255

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity>5) 
       and (colorRight.reflected_light_intensity)>5):
    
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    
    print(intensity_left, intensity_right)
    
    left_motor_speed = SpeedPercent(reflected_pc(intensity_left))
    right_motor_speed = SpeedPercent(reflected_pc(intensity_right))
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```
<font color='red'>JD: Here you use a function to convert light levels between 0 and 255 to a percentage (which I think some earlier programs were expecting)...</font>

With the robot starting just *below* the centerline on the radial grey background, you should notice that as it moves across the background it veers away from the light on a path that curves towards the bottom right of the simulator screen, steering to the right from the robot’s perspective. 

When the robot starts *above* the centerline, it veers away on the left-hand side of the central bright point (that is, the robot steers to its left).

If the robot starts on the centerline then it continues on a straight path.

<!-- #region -->
So how does the program work?

If you inspect it closely, you will see it is split into several parts.

The first part just clarifies the sensor configuration:

```python
colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
```

Then we have a `while...` loop that ensures the program keeps running until either the left or the right sensor value sees a particularly dark value:

```python
while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
```

Inside the `while...` block is the ‘intelligence’ of the program.


The values are displayed in the simulator output window using a `print()` statement, and are then used to set the motor speeds:

<font color='red'>JD: Not quite: in the code in the program above, `intensity_left` and `intensity_right` are first converted to percentages using the function `reflected_pc`...</font>

```python
    left_motor_speed = SpeedPercent(intensity_left)
    right_motor_speed = SpeedPercent(intensity_right)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
```

In this configuration:

- the percentage-scaled *left* sensor value determines the speed value applied to the *left* motor
- the percentage-scaled *right* sensor value sets the *right* motor speed.
<font color='red'>JD: I think the above bullet points should be the same (i.e. don't use 'determine' in one and 'sets' in the other as it makes it sound like something different happens each time (i.e. 'determines' works something out, whereas 'sets' just sets a value).</font>

The sensor value reports a higher reading the brighter the background. As the robot approaches the light source from below the centerline, the left sensor reads a higher value than the right sensor. As described by the program, the left motor thus turns more quickly than the right motor, and so the robot turns toward its right-hand side and veers away from the light source.
<!-- #endregion -->

### Crossing the wires

Now let’s see what happens if we run the following program which uses:

- the *left* light sensor to control the speed of the *right* motor
- the *right* light sensor to control the speed of the *left* motor.

Still using the *Radial_grey* background, clear the traces in the simulator.

Run the following code cell to download the program to the simulator and then run it in the simulator.

Move the robot to the starting location `X=100, Y=700` and run the program again.

How does the robot's behaviour with the "cross-wired" sensors and motors compare with the "direct", same-side wiring?

<font color='red'>JD: In the following, light sensor values are *not* converted to percentages. Any reason why not?</font>

```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity_pc>5) 
       and (colorRight.reflected_light_intensity_pc)>5):
    
    intensity_left = colorLeft.reflected_light_intensity_pc
    intensity_right = colorRight.reflected_light_intensity_pc
    
    print(intensity_left, intensity_right)
    
    left_motor_speed = SpeedPercent(intensity_right)
    right_motor_speed = SpeedPercent(intensity_left)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

When the program runs this time, the robot arcs *towards* the light: if it starts below the centreline, then the robot turns to its left and up towards the light; if it starts above the centreline, then the robot turns to its right, and curves down towards the light.


<!-- #region activity=true -->
#### Question

How is the robot’s behaviour explained by the program this time?
<!-- #endregion -->

<!-- #region student=true -->
*Double-click this cell to edit it and enter your explanation of why the robot behaves as it does.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The sensor values are mapped onto motor speeds with the following lines of code:

```python
    left_motor_speed = SpeedPercent(intensity_right)
    right_motor_speed = SpeedPercent(intensity_left)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
```
 
In this configuration, the percentage-scaled *right sensor* value determines the speed value applied to the *left motor*, and the percentage-scaled *left sensor* value sets the *right motor* speed. <font color='red'>JD: except that they are not *percentage-scaled* this time...</font>

As before, the sensor value reports a higher reading the brighter the background. As the robot approaches the light source from below the centreline, the left sensor reads a higher value than the right sensor. This results in the right-hand motor turning more quickly than the left motor. As a result, the robot turns toward its left-hand side and turns towards the light source.
<!-- #endregion -->

<!-- #region -->
### Looking at the data


To understand a little more closely what the sensors are seeing, tick the *Show chart* checkbox in the simulator and select the *Left light* and *Right light* traces. 

To start with, let's just make sure the datalog is empty:
<!-- #endregion -->

```python
# Clear the datalog
roboSim.clear_datalog()
```

The following program streams the necessary data elements to the simulator output window.

Run the program and observe the behavior of the traces.

How do the traces differ in value?

```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity_pc>5) 
       and (colorLeft.reflected_light_intensity_pc>5)):
    
    intensity_left = colorLeft.reflected_light_intensity_pc
    intensity_right = colorRight.reflected_light_intensity_pc
    
    print('Light_left: ' + str(intensity_left))
    print('Light_right: ' + str(intensity_right))
    
    left_motor_speed = SpeedPercent(intensity_right)
    right_motor_speed = SpeedPercent(intensity_left)
   
    tank_drive.on(left_motor_speed, right_motor_speed)

```
<font color='red'>JD: (This runs quite slowly (over a minute) on my old machine...)</font>

By inspection of the traces, you should notice that one of them is always slightly higher than the other.

We can also inspect the data in the notebook directly by looking at the data returned in the notebook synchronised datalog.

Run the following code cell.

```python
#Grab the logged data into a pandas dataframe
df = eds.get_dataframe_from_datalog(roboSim.results_log)

#Preview the first few rows of the dataset
df.head()
```

<font color='red'>JD: This only output the headings 'time', 'variable' and 'value' (i.e. no data)...</font>


Run the following code cell to plot the data using the `seaborn` scientific charting package:

```python
import seaborn as sns

# A line plot is a sensible chart type to use
# to plot the time series data
ax = sns.lineplot(x="index",
                  y="value",
                  hue='variable',
                  data=df)
```


<font color='red'>JD: This also didn't work (perhaps due to previous problem): error was "ValueError: Could not interpret input 'index' ".</font>

<!-- #region -->
## 3.2 Using ultrasound


We can also create a Braitenberg vehicle that uses a single distance sensor to moderate its behaviour, for example to try to avoid obstacles.
<!-- #endregion -->

<!-- #region activity=true -->
### Activity — Using ultrasound

Load in the *Obstacles_Test* background and run the following code cell to download the program to the simulator. Ensure that the background is loaded and that the ultrasound rays are enabled<font color='red'>JD: how do students 'ensure that the ultrasound rays are enabled'?</font>, and then run the program in the simulator.

Record your observations of the the behaviour of the robot when the program is run in the simulator with the robot starting in different positions (for example, for combinations of `(X, Y, Angle)` of `(120, 120, 90)`, `(200, 120, 90)`, `(500, 170, 145)` and `(500, 370, 75)`. Based on your observations, what sort of behaviour does the robot appear to be exhibiting?
<!-- #endregion -->

<!-- #region student=true -->
*Record your observations here about what the robot appears to be doing when the program is run in the simulator with the rovot starting in different positions.*
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Obstacles_Test -u -x 120 -y 120 -a 90
import time
ultrasonic = UltrasonicSensor(INPUT_1)

u = ultrasonic.distance_centimeters
print('Ultrasonic: ' + str(u))
time.sleep(1)
while  u > 1:
    u = ultrasonic.distance_centimeters
    print('Ultrasonic: ' + str(u))
    speed = min(100, u)
    left_motor_speed = SpeedPercent(speed)
    right_motor_speed = SpeedPercent(speed)
    tank_drive.on(left_motor_speed, right_motor_speed)

```

<!-- #region student=true -->
*Based solely on your observations, what sort of behaviour does the robot appear to be performing?*
<!-- #endregion -->

<!-- #region student=true -->
*With reference to the program, what actions is the robot actually performing?*
<!-- #endregion -->

<!-- #region activity=true -->
### Answer
*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true -->
When the program is run in the simulator, the robot moves forwards but then slows down as it approaches the obstacle as if it was a bit wary of it. The robot eventually stops as it reaches the obstacle *if* the obstacle is directly in front of the centerline of the robot. Otherwise, the robot inches up the obstacle, moves with its wheels over it, and then accelerates away once it is clear of the obstacle.

<font color='red'>JD: It never 'accelerates away' for me: it always stops on the pink square (at least for all the combinations of (X, Y, Angle) given above)...</font>

I have commented to the program to explain how I think it works.
<!-- #endregion -->

<font color='red'>JD: In the following, there is a comment that seems incomplete ("Resample the")...</font>

```python activity=true
%%sim_magic_preloaded -b Obstacles_Test -u -x 120 -y 120 -a 90

import time
ultrasonic = UltrasonicSensor(INPUT_1)

# Wait for a moment:
# ultrasound sensors can take a moment or two to
# start working as they take soundings on the environment
time.sleep(1)

# Grab the sensor reading
# as a distance in cm
u = ultrasonic.distance_centimeters

print('Ultrasonic: ' + str(u))

# If the distance to an obstacle is greater than 1cm
# Not that from the ray trace, the sensor 
# appears to be mounted a little way in
# from the front edge of the robot.
while  u > 1:
    # Resample the 
    u = ultrasonic.distance_centimeters
    print('Ultrasonic: ' + str(u))
    
    # Set a speed limit to the lesser of
    # 100 and the obstacle distance in cm
    speed = min(100, u)
    
    # Set the motor speeds based on the distance
    # to the nearest obstacle
    left_motor_speed = SpeedPercent(speed)
    right_motor_speed = SpeedPercent(speed)
    tank_drive.on(left_motor_speed, right_motor_speed)
    
# The distance must be less than 1cm
# so end the program and turn the motors off

```

<font color='red'>JD: The final comment implies that there will be code to explicitly turn the motors off (as you've earlier said is good practice), but there isn't any code to do that...</font>


## Summary

In this notebook you have experimented with some simple Braitenberg vehicles, seeing how a reactive control strategy based on some simple sensor inputs can lead to different emergent behaviours in the robot. In some cases, we might be tempted to call such behaviours ‘intelligent’, or to ascribe certain *desires* to the robot (such as ‘*it __wants__ to this*’), but that is not really the case: the robot is simply reacting to particular inputs in a particular way.
