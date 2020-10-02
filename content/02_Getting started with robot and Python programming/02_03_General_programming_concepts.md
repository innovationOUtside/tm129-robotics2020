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

# 3.1 Constants and variables in programs

In this notebook, you will learn how to use constants and variables in a robot control program.

Once again, you will be creating programs to run in the RoboLab simulator, so load the simulator by running the following code cell:

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

## 3.1.1 An introduction to constants in computer programs


Various elements of the code in the following code cell may be familiar to you from the previous notebook. Specifically, the code describes a program that is intended to cause the robot to traverse something approximating a square path in the simulator.

Download the program in the following code cell to the notebook and run it with the robot in *pen down* mode so that you can see the path it follows.

*Note that we have used the `-R` magic switch to automatically run the program as soon as it has been downloaded.*

```python
%%sim_magic_preloaded --pendown --pencolor green -R

# Try to draw a square

#Go straight
# Set the left and right motors
# in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40),
                            SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(-100,
                           SpeedPercent(40), 1.6)

#Go straight
# Set the left and right motors
# in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40),
                            SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(-100,
                           SpeedPercent(40), 1.6)

#Go straight
# Set the left and right motors 
# in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40),
                            SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(-100,
                           SpeedPercent(40), 1.6)

#Go straight
# Set the left and right motors 
# in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40),
                            SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(-100,
                           SpeedPercent(40), 1.6)
```
<!-- #region -->
Within the program, the explicit number `1.6` gives the number of rotations used when turning the robot. Several other numerical values are also evident; for example, the steering setting (`-100`) and the various speeds (`40`). These are all examples of a *literal value*, that is, values (numbers in this case) that are provided explicitly in the program at the point where they are referenced (which is to say, at the point in the program where they are meaningfully used). 

When writing computer programs it is bad practice to litter them with literal values like these. One reason is that the programmer may easily forget what the numbers mean, and if another programmer has to maintain the program, they will find it very hard to do so. Another reason is that using literal values can be inflexible, particularly if you need to use the same number at several points in the program, as we have done in the above example. 


You will see a better approach to referring to numbers in the next section.
<!-- #endregion -->

<!-- #region activity=true -->
### 3.1.2 Question — Interpreting what you read

In the program above, there are multiple occurrences of the literally stated number `40`. Do they all mean the same thing?
<!-- #endregion -->

<!-- #region student=true -->
*Record your answer here before revealing my answer.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Example observations

*Click the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
To a certain extent, the various occurrences of the number `40`  do mean the same thing because they are all motor speed percentage values.

However, in another sense, they are *not* the same at all: four of them refer to the speed of the left motor when driving forwards, four to the right motor speed for the same command, and four of them relate to the speed of both motors during the turn.
<!-- #endregion -->

### 3.1.3 Literals can make program updates and maintenance difficult

Suppose you want the robot to turn more slowly than it currently does to see if this affects the rotation count value you need to set to turn the robot through a right angle.

To do this, you would have to change the motor speed in each of the four turn instructions. You might then have to modify each of the four turn rotation count values so the robot itself continues to turn through roughly ninety degrees.

And then suppose you wanted to see if doing the turn *faster* rather than slower made the robot more or less accurate when trying to set the turn rotation value.

It could be a lot of work, couldn’t it? And possibly prone to error, making all those changes. So how might we improve things?

<!-- #region activity=true -->
### 3.1.4 Optional activity

Try changing the turn speed in the program to see if it makes any difference to the precision with which the robot turns through ninety degrees. If it does, try setting the turn rotation count so that the robot draws something close to a square, if not an exact square, once again.
<!-- #endregion -->

## 3.2 Working with constants and variables

If you tried changing the motor speeds to a reduced level in the turn commands, then you may have found that the robot became more controllable. And you probably also discovered that changing each numerical constant individually can be quite time-consuming. How much better it would be if they could all be changed at the same time? This can be achieved by *declaring* a constant in your program.


In some programming languages, *constants* are named items that are assigned a particular value once and once only in a program, and this value remains unchanged as the program executes. *Variables*, on the other hand, are named items whose value may be set at the start of a program but whose value may also change as the program executes.

*By convention*, in many Python programs, if we want to refer to an item with a value that is intended to be a fixed, *constant* value as the program runs, then we create a *variable* but with an UPPER-CASE name.


### 3.2.1 Using constants in RoboLab programs

In the following code cell, I have replaced the literal values ‘inside’ the program with ‘constants’ that are defined at the start of the program.

If you download and run the program, then you should find that it behaves as before.

```python
%%sim_magic_preloaded -b Empty_Map -R -p -C

# Try to draw a square
STEERING = -100
TURN_ROTATIONS = 1.6
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 1

#Go straight
# Set the left and right motors in a
# forward directionand run for 
# STRAIGHT_ROTATIONS number of rotations
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                            STRAIGHT_SPEED_PC,
                            STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(STEERING,
                           SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a
# forward directionand run for 
# STRAIGHT_ROTATIONS number of rotations
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                            STRAIGHT_SPEED_PC,
                            STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(STEERING,
                           SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a
# forward directionand run for 
# STRAIGHT_ROTATIONS number of rotations
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                            STRAIGHT_SPEED_PC,
                            STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(STEERING,
                           SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a
# forward directionand run for 
# STRAIGHT_ROTATIONS number of rotations
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                            STRAIGHT_SPEED_PC,
                            STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations
# *of the wheels*
tank_turn.on_for_rotations(STEERING,
                           SpeedPercent(TURN_SPEED), TURN_ROTATIONS)
```

Note that I have used two slightly different approaches to define the turn speed and the straight speed. In the case of the turn speed, I have defined `TURN_SPEED = 40`, setting the constant to a value that is passed to the `SpeedPercent()` function. For the straight speed, `STRAIGHT_SPEED_PC = SpeedPercent(40)`, I used a slightly different naming convention and defined the constant as a `SpeedPercent()` value directly.

<!-- #region activity=true -->
### 3.2.2 Activity – Changing a constant to tune a program

When the program is executed in the simulator, the value of the constant in the code is used in the same way as the literal value.

However, if we want to try running the program using different robot speeds or turn rotation values, we can now do so very straightforwardly: we simply change the required values in a single place, once for each constant value, at the top of the program.
 
Modify the above program using different values for the constants, then download and run the program in the simulator. How much easier is it to explore different values now?
<!-- #endregion -->

<!-- #region student=true -->
*Record your own observations about how the use of variables influences the ease with which you can experiment with programme settings here.*
<!-- #endregion -->

<!-- #region activity=true -->
### 3.2.3 Activity – RoboLab challenge

In the simulator, load the *Square* background by selecting it from the drop-down list at the top of the simulator.

The challenge is to get the robot to go round the outside of the solid grey square and stay within the outer square boundary, without the robot touching either the inner square or the outside square boundary, in the shortest time possible.

*Hint: you may find it useful to use the previous program for traversing a square, or create your own program using a for loop and one or more constants.*
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Square -pC  -x 550 -y 300 -a -90

# YOUR CODE HERE
```

<!-- #region activity=true -->
#### Example solution

*Click on the arrow in the sidebar or run this cell to reveal an example solution.*
<!-- #endregion -->

<!-- #region activity=true -->
I tried to simplify the program by using a `for` loop to generate each side and turn. I used constants to define the motor speeds and the number of wheel rotations required when driving in a straight line for the edges, and during the turns.
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Square -pCR -x 550 -y 300 -a -90

SIDES = 4

# Try to draw a square
STEERING = -100
TURN_ROTATIONS = 1.6
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 6

for side in range(SIDES):
    #Go straight
    # Set the left and right motors in a forward direction
    # and run for STRAIGHT_ROTATIONS number of rotations
    tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

    #Turn
    # Set the robot to turn on the spot
    # and run for a certain number of rotations *of the wheels*
    tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

```

### 3.2.4 Optimising parameter values

If you have not already done so, try adjusting the values of `STRAIGHT_ROTATIONS` so that the robot goes as close as possible to the grey square without touching it. Don’t spend too long on this: the simulator might not provide you with the resolution you are reaching for.


## 3.3 Working with variables

How many coins have you got on you? At the moment I have 12 coins in my pocket. (You might say: I have four tappable cards or phone payment devices!)

I could write:

`number_of_coins_in_my_pocket = 12`

If I buy lunch using five of these coins, then there are only seven left. So I could write:

`number_of_coins_in_my_pocket = 7`

At any time the number of coins in my pocket may vary. The name `number_of_coins_in_my_pocket` is an example of what is called a *variable* when used in computer programs.

The value of a variable can change as the program executes. Contrast this with a constant, which is intended to remain unchanged while the program executes.

<!-- #region activity=true -->
### 3.3.1 Constant or variable?

Which of the following are intended as constants (that is, things that aren’t intended to change) and which are variables (that is, they are quite likely to change)? Stylistically, how might we represent constants and variables in a Python program so that we can distinguish between them?

`number_of_coins_in_my_pocket`

`the_number_of_pennies_in_a_pound`

`the_diameter_of_robots_wheels`

`the_distance_robot_travels_in_a_second`
<!-- #endregion -->

<!-- #region student=true -->
Write your answers here:


`number_of_coins_in_my_pocket`: __variable or constant?__

`the_number_of_pennies_in_a_pound`: __variable or constant?__

`the_diameter_of_robots_wheels`: __variable or constant?__

`the_distance_robot_travels_in_a_second`: __variable or constant?__

My thoughts on how we might stylistically distinguish between them: ...
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Example answer

*Click the arrow in the sidebar or run this cell to reveal the example answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The amount of money in my pocket varies all the time, so if this were used in a computer program it would be a variable. 

The number of pennies in a pound is always a hundred, so this would be a constant. 

A robot’s wheels might be 50&nbsp;mm in diameter and this would be a constant. (A different robot might have different size wheels, but their size will not vary while the program executes.)

You may have wondered whether the distance a robot travels in a second is best represented as a constant or a variable. For a robot that could speed up or slow down its drive motors or change gear, and where this value may be used to report the speed of the robot, this would certainly be a variable. But for a simple robot (like the simulated one) with a fixed gear drive travelling at a constant speed we might used the value to *define* a fixed property of the robot, in which case it would make more sense to treat it as a constant, albeit one that we might wish to tweak or modify as we did in the programs above.

Stylistically, by convention, we use upper-case characters to identify constants and lower-case characters to represent variables. So for example, we might define the constant values `PENNIES_IN_A_POUND` or `WHEEL_DIAMETER`.
<!-- #endregion -->

### 3.3.2 Using variables

Anything that will not change during the execution of the program should be defined as a constant, whereas anything that may change should be viewed as a variable.

Variables are an essential ingredient of computer programs: they allow the computer to store the value of things at a given instant of time. 

Using the `nbtutor` extension, we can keep track of how specific variables can change their value as a program executes.

First, load in the `nbtutor` extension by running the following code cell:

```python
%reload_ext nbtutor
```
<!-- #region tags=["alert-success"] -->
*You may find you need to expand the width of this notebook column to see the `nbtutor` display correctly. Click on the right hand edge of the notebook column to drag it and expand or reduce the column width.*
<!-- #endregion -->

Now let’s use the `nbtutor` visualisation to follow what happens to the values of the `counter` and `previous` variables as the following program executes.

Run the code cell below, then step through each line of code one line at a time using the `nbtutor` *Next >* button.

As you do so, observe how the previously executed line, identified by the green arrow, modifies the value of the variables. Also note how the program flow progresses by comparing the location of the previously executed line with the next line (red arrow).

```python
%%nbtutor --reset --force
counter = 0

while counter < 5:
    print("value",counter)
    previous = counter
    counter += 1

counter, previous
```

<!-- #region tags=["alert-success"] -->
*The `%%nbtutor` magic opens a toolbar above each cell in the notebook. When you have completed an `nbtutor` activity, you can close the notebook toolbar from the notebook `View` menu `Cell menu`: selecting the `None` option will the cell toolbar.*
<!-- #endregion -->

<!-- #region tags=["alert-danger"] -->
*Note that after running an `%%nbtutor` activity, the ability to use simulator magic to download new programs to the `nbev3devsim` simulator seems to be broken.*
<!-- #endregion -->


## 3.5 Summary

In this notebook, you have seen how we can use constants and variables in a program to take literal values out of the body of a program and replace them by meaningfully named terms defined at the top of the program. This can improve readability of a program, as well as making it easier to maintain and update.

Although Python doesn’t really do constants, by convention we can refer to terms we want to treat as constant values by using upper-case characters when naming them.

When a program executes, the values of variables may be updated by program statements.

In the next notebook, you will explore another way of using variables in a robot control program by associating them with things like particular sensors and using them to provide a means of referring to, and accessing, current sensor values.
