```python
#Testing  - can we load from a package?
import _load_nbev3devwidget_requirements
#import _load_nbev3devwidget
```

```python
import _load_nbev3devwidget
```

```python
from IPython.display import Javascript
Javascript('$( "#notebook-container" ).resizable({ghost: false})')
```

```python
# If the above doesn't work, old skool is below...
```

```python
from nbev3devsim import ev3devsim_nb as eds
import jp_proxy_widget

#Load the nbtutor extension
%load_ext nbtutor

#https://github.com/AaronWatters/jp_doodle/blob/master/notebooks/misc/JQueryUI%20dialogextend%20plugin%20demo.ipynb
#Load and initialise the jquery.dialogextend package

cdn_url = "https://cdn.jsdelivr.net/npm/binary-com-jquery-dialogextended@1.0.0/jquery.dialogextend.js"
cdn_url = eds.get_file_path('js/jquery.dialogextend.js')
module_id = "dialogExtend"

# Load the module using a widget (any widget -- the module loads to the global jQuery object).
loader = jp_proxy_widget.JSProxyWidget()

# Configure the module to be loaded.
loader.require_js(module_id, cdn_url)

# Load the module
loader.js_init("""
    element.requirejs([module_identifier], function(module_value) {
        //element.html("loaded " + module_identifier + " : " + module_value);
    });
""", module_identifier=module_id)
loader

# I think we need to wait for this to load
# else we may get an error in next cell from dialogExtend not being available?
```

```python
from nbev3devsim import ev3devsim_nb as eds

#Reset the notebook style
from IPython.core.display import display, HTML, Javascript

#display(HTML("<style>#notebook-container { resize:vertical; border: 5px solid;  width: 300px; resize: horizontal; overflow: auto; float:left !important;}</style>"))
display(HTML("<style>#notebook-container { width:50%; float:left !important;}</style>"))

#Launch the simulator
from nbev3devsim import ev3devsim_nb as eds
%reload_ext nbev3devsim

roboSim = eds.Ev3DevWidget()

roboSim.element.dialog();


roboSim.js_init("""
element.dialog({ "title" : "Robot Simulator" }).dialogExtend({
        "maximizable" : true,
        "dblclick" : "maximize",
        "icons" : { "maximize" : "ui-icon-arrow-4-diag" }});
""")

display(roboSim)
```

```javascript
//This allows us to resize this view
//Click on the right hand edge to drag
$( "#notebook-container" ).resizable({ghost: false})
```

```python
%load_ext nbtutor
%load_ext nbev3devsim
```

# 4 Emergent behaviour: Braitenberg’s vehicles


In Study week 2 you came across Valentino Braitenberg’s ideas on the behaviour of robots *emerging* from the way they are wired up. The figure belows shows two ways of connecting sensors to motors. In (a), the left sensor is connected to the left motor and the right sensor is connected to the right motor. In (b) these connections are reversed.


![Diagrams representing Braitenberg vehicles alongside simulated robots wired up in a similar fashion. A Braitenberg vehicle and our simulated robot are very similar: they have two wheels, one each side, and two light sensors, one on the left and one on the right of the front of the robot. A pair of Braitenberg vehicles are shown, one light avoiding and one seeking. A light avoiding vehicle has the left light sensor connected to the left motor and wheel, and the right light sensor connected to the right motor and wheel. A light seeking vehicle has the left light sensor connected to the right motor and wheel, and the right light sensor connected to the left wheel. The simulated robots have wiring indicating identical connections. ](../images/tm129_rob_p4_f008.gif)


## 4.1 Activity: Testing Braitenberg’s vehicles


A 'thought experiment' suggests that the vehicle in figure (a) will move away from a light source. Similarly, another thought experiment suggests that the vehicle in figure (b) will move towards a light source. In the following activities you will test these predictions using an enivironment that models this set up, but uses downward facing light sensors that take measurements from a "light gradient" background, rather than forward facing light sensors that look for a light source at "eye-level" (that is, sensor-level!).


### Reconfiguring the robot

In order to detect different values from the light sensors on the right and left hand side of the robot, we need to reconfigure the robot so that the sensors are placed further apart than they are in the default robot configuration.

In the simulator, select the *Radial grey* background and check the *Pen down* checkbox.

You may notice that the simulator's left and right light sensors appear to be further apart than they have been previously.

This has been done via a change to the robot configuration setting update that is applied automatically when the *Radial grey* background is loaded.


#### Manually Changing the Robot Configuration Settings

You can increase the spacing between the sensors by:

- clicking the *Configure Robot* button in the simulator to pop=up a window containing the robot configuration settings;
- in the robot configuration settings window, scroll down to the `"sensor1"` parameters and change the `"x"` value from the default value of `-20` to the new value `-60`;
- for `"sensor2"`, change the `"x"` value from its default value of `20` the new value `60`;
- click the *Apply* button.

If you look at the robot in the simulator, you should notice that the two light sensors are now located nearer the sides of the robot and are no longer located close to the centreline.

```python
# Linting is all a bit broken at the moment
# May or may not be ready in time...

#%load_ext pycodestyle_magic
#%pycodestyle_on
#%flake8_off --ignore D100
```

#### Exploring the *Radial Grey* World

Run the following code cell to download the programme to the simulator and then run it in the simulator. For now, don't pay too much atttention to the code; our initial focus is purely on what we can observe about the behaviour of the robot.

Observe what happens paying particularly close attention to the trajectory the robot follows.

Enter a new starting location in the simulator, changing the original *Y* value from `400` to the new value `600`. Click the *Move* button to move the robot to that location and run the simulator again. How does the robot move this time? 

```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
    
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    intensity_left_pc = 100.0 * (intensity_left / 255.0)
    intensity_right_pc = 100.0 * (intensity_right / 255.0)
    
    print(intensity_left_pc, intensity_right_pc)
    
    left_motor_speed = SpeedPercent(intensity_left_pc)
    right_motor_speed = SpeedPercent(intensity_right_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

With the robot starting just *below* the centreline on the radial grey background, you shoul notice that as it moves across the background it veers away from the light on a path that curves towards the bottom right of the simulator, steering to the right from the robot's perspective. 

When the robot starts *above* the centreline, it veers away on the left hand side of the central bright point (that is, the robot steers to its left).

If the robot starts on the centreline, it continues on a straight path.

<!-- #region -->
So how does the programme work?

If you inspect it closely, you will see it is split into several parts.

The first part just clarifies the sensor configuration:

```python
colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
```

Then we have a `while..` loop that ensures the programme keeps running unitl either the left or the right sensor value sees a particularly dark value:

```python
while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
```

Inside the `while..` block is the "intelligence" of the programme.

It starts with the sampling of the sensor values, which are then scaled from their `0..255` range to a percentage range, `0..100`:

```python
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    intensity_left_pc = 100.0 * (intensity_left / 255.0)
    intensity_right_pc = 100.0 * (intensity_right / 255.0)
```

The values are displayed in the simulator output window using a `print()` statement, and are then used to set the motor speeds:

```python
    left_motor_speed = SpeedPercent(intensity_left_pc)
    right_motor_speed = SpeedPercent(intensity_right_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
```

In this configuration:

- the percentage scaled *left* sensor value determines the speed value applied to the *left* motor, and
- the percentage scaled *right* sensor value sets the *right* motor speed.

The sensor value reports a higher reading the brighter the background. As the robot approaches the light source from below the centreline, the left sensor reads a higher value than the right sensor. As described by the programme, the left motor thus turns more quickly than the right motor, and so the robot turns toward its right hand side and veers away from the light source.
<!-- #endregion -->

### Crossing the Wires...

Now let's see what happens if we run the following program which uses:

- the *left* light sensor to control the speed of the *right* motor; and
- the *right* light sensor to control the speed of the *left* motor.

Still using the *Radial grey* background, clear the traces in the simulator.

Run the following code cell to download the programme to the simulator and then run it in the simulator.

Move the robot to the starting location `X=100, Y=700` and run the program again.

How does the robot's behaviour with the "cross-wired" sensors and motors compare with the "direct", same-side wiring?

```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
    
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    intensity_left_pc = 100.0 * (intensity_left / 255.0)
    intensity_right_pc = 100.0 * (intensity_right / 255.0)
    
    print(intensity_left_pc, intensity_right_pc)
    
    left_motor_speed = SpeedPercent(intensity_right_pc)
    right_motor_speed = SpeedPercent(intensity_left_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

When the programme runs this time, the robot arcs *towards* the light: if it starts below the centre line, the robot turns to its left and up towards the light; if it starts above the light, the robot turns to its right, and  curves down towards the light.



#### Question

How is the robot's behaviour explained by the programme this time?


*Double click this cell to edit it and enter your explanation of why the robot behaves as it does.*


#### Answer

*Click the arrow in the sidebar to reveal my answer.*

<!-- #region -->
The sensor values are mapped onto motor speeds with the following lines of code:

```python
    left_motor_speed = SpeedPercent(intensity_right_pc)
    right_motor_speed = SpeedPercent(intensity_left_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
```
 
In this configuration, the percentage scaled *right sensor* value determines the speed value applied to the *left motor*, and the percentage scaled left sensor* value sets the *right motor* speed.

As before, the sensor value reports a higher reading the brighter the background. As the robot approaches the light source from below the centreline, the left sensor reads a higher value than the right sensor. This results in the right motor turning more quickly than the left motor. As a result, the robot turns toward its left hand side and turns towards the light source.
<!-- #endregion -->

<!-- #region -->
### Looking at the Data


To understand a little more closely what the sensors are seeing, click the *Show chart* checkbox in the simulator and select the *Left light* and *Right light* traces. The following programme streams the necessary data elements to the simulator output window.

Run the program and observe the behvavior of the traces.

How do the traces differ in value?
<!-- #endregion -->

```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
    
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    intensity_left_pc = 100.0 * (intensity_left / 255.0)
    intensity_right_pc = 100.0 * (intensity_right / 255.0)
    
    left_motor_speed = SpeedPercent(intensity_right_pc)
    right_motor_speed = SpeedPercent(intensity_left_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
    print('Light_left: ' + str(colorLeft.reflected_light_intensity ))
    print('Light_right: ' + str(colorRight.reflected_light_intensity ))
```

By inspection of the traces, you should notice that one of them is always slightly higher than the other.

```python

#Grab the logged data into a pandas dataframe
df = eds.get_dataframe_from_datalog(roboSim.results_log)

#Preview the first few rows of the dataset
df.head()
```

```python
import seaborn as sns
ax = sns.lineplot(x="index", y="value", hue='variable', data=df)
```

<!-- #region -->
# Using Ultrasound


We can also create a Braitenberg vehicle that uses a single distance sensor to moderate its behaviour, for example to try to avoid obstacles.

Load in the *Obstacles Test* background, run the following code cell to download the programme to the simulator, and then run it in the simulator.

By observing what happens when you start the robot in different positions, what do you think the robot is doing?
<!-- #endregion -->

```python
%%sim_magic_preloaded
import time
ultrasonic = UltrasonicSensor(INPUT_1)

u = ultrasonic.distance_centimeters
print('Ultrasonic: ' + str(u))
time.sleep(1)
while  u > 1:
    u = ultrasonic.distance_centimeters
    print('Ultrasonic: ' + str(u))
    u = min(100, u)
    left_motor_speed = SpeedPercent(u)
    right_motor_speed = SpeedPercent(u)
    tank_drive.on(left_motor_speed, right_motor_speed)

```

## Summary

In this notebook you have experimented with some simple Braitenberg vehicles, seeing how a reactive control strategy based on some simple sensor inputs can lead to different emergent behabviours in the robot. In some cases, we might be tempted to call such behaviours "intelligent", or to ascribe certain *desires* to the robot (such as '*it __wants__ to this*) but that is not really the case: the robot is simply reacting to particular inputs in a particular way.