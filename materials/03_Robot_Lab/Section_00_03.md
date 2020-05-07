```python
# Run this cell to set up the robot simulator environment

#Load the nbtutor extension
%load_ext nbtutor

#Reset the notebook style
from IPython.core.display import display, HTML

display(HTML("<style>#notebook-container { width:50% !important; float:left !important;}</style>"))


#Launch the simulator
from nbev3devsim import ev3devsim_nb as eds
%load_ext nbev3devsim

roboSim = eds.Ev3DevWidget()
display(roboSim)
roboSim.element.dialog();
```

# 4 Emergent behaviour: Braitenberg’s vehicles


In Study week 2 you came across Valentino Braitenberg’s ideas on the behaviour of robots *emerging* from the way they are wired up. The figure belows shows two ways of connecting sensors to motors. In (a), the left sensor is connected to the left motor and the right sensor is connected to the right motor. In (b) these connections are reversed.


![Diagrams representing Braitenberg vehicles alongside simulated robots wired up in a similar fashion. A Braitenberg vehicle and our simulated robot are very similar: they have two wheels, one each side, and two light sensors, one on the left and one on the right of the front of the robot. A pair of Braitenberg vehicles are shown, one light avoiding and one seeking. A light avoiding vehicle has the left light sensor connected to the left motor and wheel, and the right light sensor connected to the right motor and wheel. A light seeking vehicle has the left light sensor connected to the right motor and wheel, and the right light sensor connected to the left wheel. The simulated robots have wiring indicating identical connections. ](../images/tm129_rob_p4_f008.gif)


## 4.1 Activity: Testing Braitenberg’s vehicles


A 'thought experiment' suggests that the vehicle in figure (a) will move away from a light source. Similarly, another thought experiment suggests that the vehicle in figure (b) will move towards a light source. In the following activities you will test these predictions using an enivironment that models this set up, but uses downward facing light sensors that take measurements from a "light gradient" background, rather than forward facing light sensors that look for a light source at "eye-level" (that is, sensor-level!).


### Reconfiguring the robot

In order to detect different values from the light sensors on the right and left hand side of the robot, we need to reconfigure the robot so that the sensors are placed further apart than they are in the default robot configuration.

You can increase the spacing between the sensors by:

- clicking the *Configure Robot* button in the simulator to pop=up a window containing the robot configuration settings;
- in the robot configuration settings window, scroll down to the `"sensor1"` parameters and change the `"x"` value from the default value of `-20` to the new value `-60`;
- for `"sensor2"`, change the `"x"` value from its default value of `20` the new value `60`;
- click the *Apply* button.

If you look at the robot in the simulator, you should notice that the two light sensors are now located nearer the sides of the robot and are no longer located close to the centreline.


In the simulator, select the *Radial grey* background and check the *Pen down* checkbox.

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

When the programme runs this time, the robot veers *towards* the light. If it starts below the centre line, the robot turns to its left and up towards the light. If it starts above the light, the robot turns to its right, and  curves down towards the light.



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
### TO DO


?? ultrasound example?

Datalog - eg chart the light sensor values?
print('Colour: ' + str(colorLeft.reflected_light_intensity ))





Run the program. As you do so, note what happens. (If you have printed this document, use the second column of Table 4.2 to record your results.)

Try dragging Simon to different starting positions in the environment to explore its behaviour. You may want to leave Simon running for a while to be sure how it behaves. Use the `Show trail` button to record its behaviour. Remember that you can use the `Simulator &gt; Zoom in` and `Zoom out` features.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+NumPlus and Ctrl+NumMinus</p></div>
<!--ITQ-->

#### Question

Did the Braitenberg_A robot avoid the light? Explain why.
<!-- #endregion -->

#### Answer

The Braitenberg_A robot vehicle avoids the light. The power delivered to the wheels is proportional to the light received by the motor on the same side of the vehicle. If the left sensor receives more light than the right sensor, then the left wheel turns faster than the right, and the robot will turn right, away from the light.
<!--ENDITQ--><!--ITQ-->

#### Question

Was the Braitenberg_B robot attracted to the light? Explain why.


#### Answer

The Braitenberg_B robot vehicle is attracted to the light. The power delivered to the wheels is proportional to the light received by the motor on the opposite side of the vehicle. If the left sensor receives more light than the right sensor, then the right wheel turns faster than the left, and the robot will turn left, towards the light.
<!--ENDITQ--><!--ITQ-->

#### Question

Did the modified version of the robot stay at the brightest part of the environment? Explain why it behaved as it did.


#### Answer

No. The Braitenberg_B robot vehicle is attracted to the light. However, it speeds up as it approaches the brightest part of the environment and, as a result, overshoots.
<!--ENDITQ-->
This activity illustrates the important idea developed in Study week 2 that a robot may have a behaviour in its environment that was not programmed in. Nowhere in the RobotLab program is there an explicit goal of ‘avoid light’.

The idea of building robots with desirable emergent behaviour that does not need explicit programming is very attractive. At the moment, however, the question of how to produce complex behaviours systematically is unresolved.

