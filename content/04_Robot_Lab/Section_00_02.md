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

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

# 2 Line followers and edge followers

In this section you will investigate how a robot can be made to follow a desired path as it navigates its environment.

When humans navigate around a house or a supermarket, most use the information provided by their eyes to control their movements. Many simple robots do not have complex vision systems like this and have to rely on much simpler sensors. One of the most commonly used methods for navigation by robots with simple light sensors is to follow a line.

The idea behind *line following* is that the environment has been adapted by the creation of a marked path that the robot can follow. For example, it could be a black line on a white background, or a wire embedded in the floor creating a magnetic field.

As well as following a line, we can also follow the *edge* of a line. You will have an opportunity to explore both forms of control.


## 2.1 A simple line follower using two sensors

In a simple visual line follower, we might use two light sensors along the front edge of the robot. Suppose the distance between the sensors slightly exceeds the thickness of a black line on a white background. With the robot placed over the line and straddling it, one sensor is on either side of the line.

If the robot turns across the *left-hand* side of the line, then the sensor on the *right-hand* side of the robot will turn onto the line and detect black. This provides us with an error signal we can use to correct the path of the robot and turn it back onto the line. In this case, the control strategy would be to turn towards the right-hand side of the robot.

<!-- #region activity=true -->
### SAQ

What would happen if the robot veered off the right-hand side of the line?
<!-- #endregion -->

<!-- #region student=true -->
*Write your answer here before revealing the answer.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
If the robot goes over the *right-hand* edge of the line, then the left-hand sensor will register black and the robot knows that it needs to turn to the left to move back over the line.
<!-- #endregion -->

<!-- #region activity=true -->
### SAQ

What would the robot do if the line started to curve to the left rather than continue in a straight line? Explain how it might stay on the line.
<!-- #endregion -->

<!-- #region student=true -->
*Write your answer here before revealing the answer.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
If the line turned to the left and the robot was moving straight ahead, then the left-hand sensor would move over the line and see black. This would generate an error signal indicating that the robot should turn to the left to stay on the line and move the left-hand light sensor back over the white background.
<!-- #endregion -->

<!-- #region activity=true -->
### SAQ

Suppose that the two sensors are moved closer together, separated by a distance less than the width of the line to be followed, with one sensor still on either side of the centreline of the robot.

Would the robot still be able to follow the line? Explain your reasoning.
<!-- #endregion -->

<!-- #region student=true -->
*Write your answer here before revealing the answer.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
If the sensors are close together, separated by less than the width of the line, then they will both be over the line when the robot is on the line, and both see black. If the robot moves off the line to the left, then the left-hand sensor will detect white, an error signal can be generated, and the robot can be turned away from that direction and back onto the line.
<!-- #endregion -->

## 2.2 Writing a line-follower program

The behaviour of the sensors and the interpretation of the data they provide is very important when creating line-following robots. We will start to look at these aspects in some detail in this activity and later ones.

The challenge is to write a robot control program to make the robot follow the line.


### Calibrating the required sensor readings

You first need to record the light sensor readings just to check that we know what reading the sensor gives when it is over the line, and off the line.

Even if you *think* you know what the likely sensor readings are, it’s still worth checking.

<!-- #region activity=true -->
### Taking readings

The light sensor defined by `ev3dev-py` as a `ColorSensor` object actually returns three RGB colour components: a `R` (red) value, a `G` green value and a `B` blue value, each in the range `0...255`. (The colour signal can also be mapped onto other representations, such as HSV – *Hue, saturation, value*.)

The `reflected_light_intensity` reading in the simulator is actually recorded as the value of the first RGB component: the *red* component.

Drag or otherwise move the robot around the screen, positioning it so the left-hand light sensor is directly over the area you want to record the sensor reading for. When you place the robot, the light sensor reading should be updated in the simulator sensor readings area.

What readings do you obtain? Record your readings in the cell below:
<!-- #endregion -->

<!-- #region student=true -->
- *value over black:*
- *value over white:*
- *value over the edge (where the sensor sees black and white):*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### My readings
*Click the arrow in the sidebar or run this cell to reveal my readings.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The readings I got were as follows:
    
- *value over black:* `0`
- *value over white:* `255`
- *value over the edge (where the sensor sees black and white):* varies between the black and white values, depending on how much of the line was in view of the sensor.
<!-- #endregion -->

<!-- #region -->
## 2.3 Creating a line-follower program

In the following challenge, you will develop a program that will allow the robot to use two sensors to help it follow a narrow line.

A starting constraint is that the line is quite a narrow one that can be straddled by the robot, with a light sensor to either side of the line over the white background.

As with many engineering problems, it is possible to consider the problem in different ways and decompose it in to different smaller sub-problems.

At quite a high level of abstraction, we might simply ask:

- *how can we get the robot follow a straight line?*, and
- *how can we get the robot to follow a line that turns a corner?*

This then splits into a perception problem at a slightly lower level of abstraction:

- what do the sensors see when they straddle a straight line?
- what do the sensors see if the robot turns off the line to the left or to the right?
- what do the robot sees if the line curves to the leve or to the right?



We might then want to focus on what motor actions we should take when presented with different sensor perceptions. For example, here are some questions you might want to bear in mind as you develop your program:

  - What should the robot do if both sensors see white?
  - What should the robot do if the left-hand sensor sees white and the right-hand sensor sees black?
  - What should the robot do if the left-hand sensor sees black and the right-hand sensor sees white?
  - Could there be a situation where both sensors see black? What should the robot do in such a case?

Note that there may be different possible answers to each question. Part of the challenge of the design task is to balance the various different potential solutions to each part of the problem that work together solve the problem as a whole.

How might you need to modify the program if the robot is placed on a black line that is slightly wider than the distance between the sensors?
<!-- #endregion -->

<!-- #region student=true -->
*Make your own notes on the design questions here.*
    
*For example, how can the robot tell:*

- *if it is on the line?*
- *if it is starting to veer off the line?*
- *if the line is starting to curve one way or the other?*

*And when it comes to controlling the robot:*
  
  - *What should the robot do if both sensors see white?*
  - *What should the robot do if the left-hand sensor sees white and the right-hand sensor sees black?*
  - *What should the robot do if the left-hand sensor sees black and the right-hand sensor sees white?*
  - *Could there be a situation where both sensors see black? What should the robot do in such a case?*

<!-- #endregion -->

<!-- #region activity=true -->
### Challenge — writing a line-follower program

There are many strategies for writing a line follower program, so a key aim for this activity is to provide you with an opportunity for you to come up with your own strategy for solving the problem.

If you get stuck, put yourself in the mind of the robot and talk aloud what steps you need to perform when different situations occur.

To simplify the program, do not worry about a terminating condition for it. Instead let it run forever (or at least, until you force the execution to stop by clicking the simulator *Stop* button). Do this by placing the main logic for your code inside an infinite loop (a `while True:` block, which will loop forever).

Use the `Line_Following_Test` background and set the pen down option to create a trace showing where the robot travelled:
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Line_Following_Test -p

# Define any original variables first

# Create an infinite control loop

    # Within the control loop
    #  - read sensor values
    #  - use sensor values to make a decision about motor actions

```

<!-- #region activity=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my anwer.*
<!-- #endregion -->

<!-- #region activity=true -->
The following code cell contains my solution, although it’s not necessarily a very good one!

My control strategy is to set the motor speed on each side to be proportional to the reflected light intensity. The more white the sensor sees, the faster that wheel travels. If the sensor sees black, then the motor stops.

Also, the robot falls off the line quite easily if the speed is set too high.
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Line_Following_Test -p

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
 
# Infinite loop
while True:
    
    # Grab the light sensor readings
    intensity_left = colorLeft.reflected_light_intensity_pc
    intensity_right = colorRight.reflected_light_intensity_pc

    # Display the light sensor readings
    print(intensity_left, intensity_right)
    
    max_percent_speed = 20
    
    # It may be worth trying to tune the
    # different speeds a bit more carefully.
    # We might also have a minimum speed for
    # each wheel by passing in a fixed positive
    # bias value into the SpeedPercent calculation,
    # whilst also remembering the SpeedPercent
    # function expects a value in the range -100...100
    left_motor_speed = SpeedPercent(max_percent_speed*intensity_left)
    right_motor_speed = SpeedPercent(max_percent_speed*intensity_right)
    
    # Set the motors to the desired speeds.
    tank_drive.on(left_motor_speed, right_motor_speed)
```

<!-- #region activity=true -->
Another approach might be to determine an error signal as the difference between the left-hand and right-hand sensor values and use that to set a steering value:
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Line_Following_Test

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

# The GAIN term "amplifies" the error signal
GAIN = 0.5

while True:
    print('Left_light: ' + str(colorLeft.reflected_light_intensity ))
    print('Right_light: ' + str(colorRight.reflected_light_intensity ))
    
    # Calculate an error term
    error = colorLeft.reflected_light_intensity - colorRight.reflected_light_intensity
    
    #Amplify the error to generate a steering correction value
    correction = error * GAIN
    
    #Steer the robot accordingly
    steering_drive.on(correction, 20)

```

## 2.4 A simple edge follower using a single sensor

In the line-follower program we used *two* light sensors to detect when the robot started to veer off the line, either to the left, or to the right.

But what happens if the line is much wider than the distance between the two sensors?

In that case, it might make more sense to follow a particular edge of the line. For example, if we follow the right-hand edge, then the robot is over the edge of the line when the left-hand sensor sees black and the right-hand sensor sees white. If both sensors see white, then the robot needs to turn back to the left so the left-hand sensor can reacquire the black line.

But do we really need *two* sensors to follow the edge of a line? Or can we get away with using just a single sensor?


<font color='red'>JD: I'm wondering whether it's worth having 'activities' - in the previous week I don't recall there being many 'activities', but there were still things for students to do. Most activities aren't numbered anyway and if students want to refer to a particular part of a notebook, they can refer to the cell number anyway.</font>

<!-- #region activity=true -->
### Activity – Following a single edge

What strategy might you use to control a robot so that it can follow a line using just a single light sensor?
<!-- #endregion -->

<!-- #region student=true -->
*Write your solution here.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The basic idea is that, as the robot moves forwards, the light sensor tells it if it should move towards the edge or away from it. For example, if the light sensor picks up a light background then the robot needs to turn (say to the right) until it detects the dark line. Once the light sensor detects it is over the dark line, the robot should start moving forwards whilst also turning back to the left to find the edge of the line again. In this way, the robot would ‘edge’ forwards as it follows the *right-hand* edge of the black line.
<!-- #endregion -->

### Turning a control strategy into code

Having a strategy for writing a robot control program that will allow a robot to follow a line using just a single sensor is one thing, but can you now turn that strategy into a working control program?

<!-- #region activity=true -->
### Challenge – An edge follower using a single sensor

Building on the control strategy you developed in the previous activity, see if you can implement that strategy by writing a program to follow the edge of a line using just a single light sensor.

Download your program to the simulator and test it against various lines in the *Line_Following_Test* background.

What happens if you start your robot on the other edge? How would you modify your program so that the robot could follow the other edge?
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Line_Following_Test

# Add your code here
```

<!-- #region student=true -->
*Record a description of how well your control program worked here.*
<!-- #endregion -->

<!-- #region activity=true -->
Were there any lines or line features it particularly struggled with?

How did it compare in terms of performance to the line followers that used two light sensors?
<!-- #endregion -->

<!-- #region student=true -->
*Record your observations and reflections here.*
<!-- #endregion -->

<!-- #region activity=true -->
What advantages and disadvantages might arise from using a single light sensor solution compared to a two-sensor solution? 
<!-- #endregion -->

<!-- #region student=true -->
*Record your thoughts here.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### My answer

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
My program is below. It uses a `while True` to infinitely loop through a code block that checks to see whether the single sensor detects white or black; if it detects white then the robot turns about one wheel back onto the line, which eases it forwards on one side; if it detects black then it turns about one wheel away from the line, again edging it slightly forwards.

In this manner the robot wiggles along the line. If we use the right-hand sensor rather than left-hand sensor to detect the edge, and enable the pen trace, we see the trace follows the first line reasonably well.
<!-- #endregion -->

```python activity=true hidden=true
%%sim_magic_preloaded --background Line_Following_Test

colorLeft = ColorSensor(INPUT_2)
while True:
    
    intensity_left = colorLeft.reflected_light_intensity
    
    print("Left_light: "+str(intensity_left))
    
    if intensity_left < 50:
        left_motor_speed = SpeedPercent(0)
        right_motor_speed = SpeedPercent(20)
    else:
        left_motor_speed = SpeedPercent(20)
        right_motor_speed = SpeedPercent(0)
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

<!-- #region activity=true hidden=true -->
In terms of the relative trade off between one or two sensors, the single-sensor approach would likely be cheaper, but the two-sensor approach is more general: the two-sensor robot can follow the line or either edge, whereas the control program for the single-sensor solution confines the robot to following a specific edge.
<!-- #endregion -->

## Summary

In this notebook, you have learned how to <font color='red'>JD: To be completed...</font>
