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

# 2 Constants and variables in programs

In this notebook, you will learn how to use constants and variables in a robot control programme.

Once again, you will be creating programmes to run in the robot simulator, so load the simulator by running the following code cell.

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

## 2.1 An introduction to constants in computer programs


Various elements of the code in the following code cell may be familiar to you from the previous notebook. Specifically, the code describes a programme that is intended to cause the robot to traverse something approximating a square path in the simulator.

Download the programme in the following code cell to the notebook and run it with the robot in *pen down* mode so that you can see the path it follows.

```python
%%sim_magic_preloaded --pendown

# Try to draw a square

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(-100, SpeedPercent(40), 0.826)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(-100, SpeedPercent(40), 0.826)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(-100, SpeedPercent(40), 0.826)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 1)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(-100, SpeedPercent(40), 0.826)
```

<!-- #region -->
Within the programme, the explicit number `0.826` gives the number of rotations used when turning the robot. Several other numerical values are also evident; for example, the steering setting (`-100`) and the various speeds (`40`). These are all examples of a *literal value*, that is, values, in this case, numbers, that are provided explicitly in the program at the point where they are referenced (which is to sat, at the point in the programme where they are meaningfully used). 

When writing computer programs it is bad practice to litter them with literal values like these. One reason is that the programmer may easily forget what the numbers mean, and if another programmer has to maintain the program, they will find it very hard to do so. Another reason is that using literal values can be inflexible, particularly if you need to use the same number at several points in the programme, as we have done in the above example. 


You will see a better approach to referring to numbers in the next section.
<!-- #endregion -->

<!-- #region activity=true -->
#### Question

In the program above, there are multiple occurrences of the number `40`. Do they all mean the same thing?
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
In one sense, yes, they are all motor speed percentage values; but in another sense, no: four of them refer to the speed of the left motor when driving forwards, four to the right motor speed for the same command, and four of them relate to the speed of both motors during the turn.
<!-- #endregion -->

### Literals can make programme updates and maintenance difficult

Suppose you want the robot to turn more slowly than it currently does to see if this affects the rotation count value you need to set to turn the robot through a right angle.

To do this, you would have to change the motor speed in each of the four turn instructions. You might then have to modify each of the four turn rotation count values so the robot itself continues to turn through roughly ninety degrees.

And then suppose you wanted to see if doing the turn *faster* rather than slower made the robot more or less accurate when trying to set the turn rotation value.

It could be a lot of work, couldn't it? And possibly prone to error, making all those changes.

You have already seen how you could use a loop to simplify the square drawing programme, but you would still be having to delve into the depths of the programme to change the values? And the values would still be *literal* values. So how can we improve things?

<!-- #region activity=true -->
### Optional Activity

Try changing the turn speed in the programme to see if it makes any difference to the precision with which the robot turns through ninety degrees. If it does, try setting the turn rotation count so that the robot draws something close to a square, if not an exact square, once again.
<!-- #endregion -->

## 2.2 Working with constants and variables

If you tried changing the motor speeds, you possibly found that you also had to change the turn rotations value too. And you probably also discovered that changing each numerical constant individually can be quite time-consuming. How much better it would be if they could all be changed at the same time. This can be achieved by *declaring* a constant in your programme.


In some programming languages, *constants* are named items that are assigned a particular value once and once only in a programme, and this value remains unchanged as the programme executes. *Variables*, on the other hand, are named items whose value may be set at the start of a programme, but whose value may also change as the programme executes.

*By convention*, in many Python programmes, if we want to refer to an item with a value that is intended to be a fixed, *constant* value as the programme runs, we create a *variable* but with an UPPERCASE name.


### Using constants in RobotLab programs

In the following code cell, I have replaced the literal values "inside" the programme with "constants" that are defined are the start of the programme.

If you download and run the programme, it should behave as before.

```python
%%sim_magic_preloaded

# Try to draw a square
STEERING = -100
TURN_ROTATIONS = 0.826
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 1

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

#Go straight
# Set the left and right motors in a forward direction
# and run for 1 rotation
tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

#Turn
# Set the robot to turn on the spot
# and run for a certain number of rotations *of the wheels*
tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)
```

Note that I have used two slightly different approach to define the turn speed and the straight speed. In the case of the turn speed, I have defined `TURN_SPEED = 40`, setting the constant to a value that is passed to the `SpeedPercent()` function. For the straight speed, `STRAIGHT_SPEED_PC = SpeedPercent(40)`, I used a slightly different naming convention and defined the "constant" as a `SpeedPercent()` value directly.

<!-- #region activity=true -->
### Activity — Changing a constant to tune a program

When the programme is executed in the simulator, the value of the "constant" into the code is used in the same way as the literal value.

However, if we want to try running the programme using different robot speeds or turn rotation values, we can now do so very straightforwardly, simply by changing the requierd values in a single place, once for each "constant" value, at the top of the programme.
 
Modify the above programme using different values for the constants, then download and run the programme in the simulator. How much easier is it to explore different values now?
<!-- #endregion -->

<!-- #region activity=true -->
## Activity: Robo Lab challenge

In the simulator, load the *Square* background.

The challenge is to get the robot to go round the outside of the solid grey square and stay within the outer square boundary, without the robot touching either the inner square or the outside square border loop, in the shortest time possible.

*Hint: you may find it useful to use the previous programme for traversing a square, or create your own programme using a for loop and sone or more "constants".*
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded

# YOUR CODE HERE
```

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click on the arrow in the sidebar to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
I tried to simplify the programme by using a `for` loop to generate each side and turn. I used "constants" to define the motor speeds and the number of wheel rotations required when driving in a straight line for the edges, and durig the turns.
<!-- #endregion -->

```python activity=true hidden=true
%%sim_magic_preloaded

SIDES = 4

# Try to draw a square
STEERING = -100
TURN_ROTATIONS = 0.826
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 6

for side in range(SIDES):
    #Go straight
    # Set the left and right motors in a forward direction
    # and run for 1 rotation
    tank_drive.on_for_rotations(STRAIGHT_SPEED_PC, STRAIGHT_SPEED_PC, STRAIGHT_ROTATIONS)

    #Turn
    # Set the robot to turn on the spot
    # and run for a certain number of rotations *of the wheels*
    tank_turn.on_for_rotations(STEERING, SpeedPercent(TURN_SPEED), TURN_ROTATIONS)

```

### Optimising Parameter Values

If you have not already done so, try adjusting the values of `forwardTime` so that the robot goes as close as possible to the grey square without touching it. Don’t spend too long on this.



## 2.4 Working with variables

How many coins have you got on you? At the moment I have 12 coins in my pocket. (You might say: I have four tappable cards / phone devices!)

I could write:

`number_of_coins_in_my_pocket = 12`

If I buy lunch using five of these coins, there are only seven left. So I could write:

`number_of_coins_in_my_pocket = 7`

At any time the number of coins in my pocket varies, and the name `number_of_coins_in_my_pocket` is an example of what is called a *variable* when used in computer programs.

The value of a variable can change as the program executes. Contrast this with a constant which is intended to remain unchanged while the program executes.

<!-- #region activity=true -->
#### SAQ — Question

Which of the following are intended as constants (that is, things that aren't intended to change and which are variables (that is, they are quite likely to change)? Stylistically, how might we represent constants and variables in a Python programme so that we can distinguish between them?

`number_of_coins_in_my_pocket`

`the_number_of_pennies_in_a_pound`

`the_diameter_of_robots_wheels`

`the_distance_robot_travels_in_a_second`.
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
#### Answer

*Click the arrow in the sidebar to reveal the answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The amount of money in my pocket varies all the time, so if this were used in a computer program it would be a variable. 

The number of pennies in a pound is always a hundred, so this would be a constant. 

A robot’s wheels might be 50 mm in diameter and this would be a constant. (A different robot might have different size wheels, but their size will not vary while the program executes.)

You may have wondered whether the distance a robot travels in a second is best represented as a constant or a variable. For a robot that could speed or slow its drive motors or change gear, and where this value may be used to report the speed of the robot, this would certainly be a variable. But for a simple robot (like the simulated one) with a fixed gear drive travelling at a constant speed we might used the value to *define* a fixed property of the robot in which case it would make more sense to treat it as a constant, albeit one that we might wish to "tweak" or modify as we did in the programmes above.

Stylistically, by convention, we use upper case characters to identify constants and lower case characters to represent variables. So for example, we might define the constant values `PENNIES_IN_A_POUND` or `WHEEL_DIAMETER`.
<!-- #endregion -->

### Using Variables

Anything that will not change during the execution of the program should be defined as a constant, and anything that may change should be viewed as a variable.

Variables are an essential ingredient of computer programs. They allow the computer to store the value of things at a given instant of time. 

You have already seen how variables can change their value as a programme executes using the `nbtutor` extension.

Let's look again at how that works.

First, load in the `nbtutor` extension by running the following code cell:

```python
%load_ext nbtutor
```

Now let's use the `nbtutor` visualisation to follow what happens to the values of the `counter` and `previous` variables as the following programme executes.

Run the code cell, then step through each line of code a line at a time using the `nbtutor` *Next >* button.

Observe how the previously executed line, identified by the green arrow, modifies the value of the variables. Also note how the program flow progresses by comparing the location of the previously executed line with the next line (red arrow).

```python
%%nbtutor --reset --force
counter = 0

while counter < 5:
    print(counter)
    previous = counter
    counter += 1

counter, previous
```

## Updating Variables from Sensor Values

Load the *Grey bands* background in to the simulator, and download and run the following programme, which you may recall from the previous notebook. Observe the values of that are displayed in the simulator output window.

```python
%%sim_magic_preloaded
from ev3dev2.sensor import INPUT_2

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

colorLeft = ColorSensor(INPUT_2)

sensor_value = colorLeft.reflected_light_intensity_pc

while sensor_value > 99:
    print(sensor_value)
    sensor_value = colorLeft.reflected_light_intensity_pc

print("I now see {}".format( colorLeft.reflected_light_intensity_pc))
tank_drive.off()
```

In the programme, the `colorLeft.reflected_light_intensity_pc` element represents a variable that describes the current value of a particularly configured robot sensor. We then set another variable, `sensor_value`equal to the value of that sensor variable.

From the simulator output display, we see that the `sensor_value` changes as the robot crosses the grey lines. But there is nothing explicitly stated in the program where *we* update the `colorLeft.reflected_light_intensity_pc` value. Rather, it's value is updated "live" from a regular poll of the sensor within the simulator.

*By polling a sensor, we mean that a reading is taken from the sensor, somehow(!) and used to set the value of a variable associated with that sensor so we can make decisions based on the sensor value from within our robot control program.*

<!-- #region -->
## Summary

In this notebook, you have seen how we can use constants and variables in a programme to take literal values out of the body of a programme  and replace them by meaningfully named terms defined at the top of the programme. This can improve readability of a programme, as well as making it easier to maintain and update.

Although Python doesn't really do constants, by convention we can refer to terms we want to treat as constant valus by using upper cases characters when naming them.


When a programme executes, the value of variables may be updated by programme statements.

In a robot context, variables may also be associated with things like particular sensors, in which case we think of the sensor itself updating the value of the variable.
<!-- #endregion -->
