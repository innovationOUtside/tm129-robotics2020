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

# Introduction to sensor based control

In this session you will explore a range of simulator environments and sensor and motor drive noise settings, as well as modifying the robot configuration by changing the height of the simulated light sensor.

Through your experiments, you will investigate the way the sensors behave and how this information can be used to control the robot.



## 1 Simple robot control using sensors

You have already seen some earlier demonstrations of how we can use sensors to control the behaviour of our simulated robot. In this week's activities, you will have an opportunity to explore in more detail how we can use sensors to control the robot's activities.

We'll start by with a simple example of detecting a single change in the environemnt — the change from a white background to a black line — and acting on that change, before going on to look at some more elaborate robot behaviours and how we might actually program them.


## 1.1 Activity — Stopping at a black line

In this acti

<!-- #region hideCode=true hidePrompt=true -->
## 1.2 Activity: Keeping a robot in an area

This activity demonstrates how to keep a robot inside a particular area bounded by a boxed area marked out on the floor of the world. 

Load the simulator package and then load and display the simulator widget:
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
Select the `Loop` background which loads the robot in to the centre of a large rectangle drawn with thick black lines. 

The following `Stay_inside` program causes the robot moves forwards until its light sensor detects the black contour, at which point the robot reverses direction. When it encounters the contour again it changes direction. In this way the robot shuttles backwards and forwards inside the contour indefinitely.

Run the code cell to load the program into the simulator, then click on the simulator *Run* button; when you are ready to stop the program, click on the simulator *Stop* button.
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic_preloaded --background Loop

# Program to stay inside a bounded area

# Start to drive forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity_pc))

    if colorLeft.reflected_light_intensity_pc < 40:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)

        # Drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)

        # Drive forwards again
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

<!-- #region hideCode=true hidePrompt=true -->
At the start of the program is some so-called *IPython magic* which is prefixed by one (`%`) or two (`%%`) signs. The `%%` prefixed magic is a cell magic that is used to modify the behaviour of the contents of the whole cell.

```python
%%sim_magic_preloaded
```

In this case, the magic identifies the cell as one which is being used to download code to the simulator, as well as optionally configure it. 

The next two lines are comments:

```python
# Program to stay inside a bounded area

# Start to drive forwards
```

For these lines, a `#` ("hash" or, in American English, a "pound") sign identifies the line as a comment line; in this case, the first line gives a very concise statement of the objective of the programme, the second describes what an actual line of code is intended to do. Comments are "free text" areas that are not executed as lines of Python code. As such, they can be used to provide annotations or explanations of particular parts of the programme, or "comment out" lines of code that are unnecessary.

The control program properly starts by using a "tank drive" to drive the robot forwards at about half its full speed (the left wheel and the right when are both powered on at 20% of their maximum speed).

```python
tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

The `while True:` command means *do everything that follows for ever (or until the user stops the program)*. The `:` is *required* and it defines what to do if the tested condition evaluates as true.

The next line is indented, and starts the definition of a code block, each line of which will be executed in turn. The lines of code that define the code block are indented to the same level. If the condition evaluated by the `while` statement was not true, then the code block would not be executed.

The `print('Light_left: ' + str(colorLeft.reflected_light_intensity_pc))` command prints the current value of the left light sensor, which is reading the "reflected light intensity", as a percentage, to the output display window. As you will see later, this value can also be viewed via a dynamically updated chart, as well as analysed "offline" in the Python notebook when the simulation run has finished.

The next line in the code block, `if colorLeft.reflected_light_intensity_pc < 40:`, compares a specific sensor reading, interpreted in a particular way, to a particular value (100). If the value is below that threshold, as it is when the robot is over the black like, the programme moves on to a new code block defined by lines of code that are further indented.

Following the `if` statement, we start another new code block with another level of indentation. On the first line of code in that new code block, the robot drives *backwards* at half speed for 2 rotations of the wheels (`tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)`). (According to the [documentation](https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#ev3dev2.motor.MoveTank.on_for_rotations), *if the left speed is not equal to the right speed (i.e., the robot will turn), the motor on the outside of the turn will rotate for the full rotations while the motor on the inside will have its requested distance calculated according to the expected turn*).

After the robot moves backwards, there is a comment line suggesting what the next executed line of code does (`# Drive in a turn for 2 rotations of the outer motor`) and then the robot turns on the spot (`tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)`).

Finally, there is another code explaining comment — `# Drive forwards again` — and then robot is set to drive forwards again: `tank_drive.on(SpeedPercent(50), SpeedPercent(50))`)

The control flow initiation by the `while` loop then causes the sequence to repeat, with the programme control flow looping back to the while statement to check the sensor reading, and then working through each step in turn again. While the sensor reading is above 100, the robot keeps going. Every time it "sees" the black contour it reverses the direction of the motors, and then turns before driving forwards again. In this way the simulated robot shuttles backwards and forwards, staying inside the area defined by the contour.
<!-- #endregion -->

<!-- #region activity=true -->
### Activity - Simulated vs. Real Robots

How do you think the simulated robot in this activity compares with a real robot?
<!-- #endregion -->

<!-- #region student=true -->
*Double click this cell to edit it and enter your thoughts here, then "Run" this cell to return it to the styled / rendered HTML view.*
<!-- #endregion -->

<!-- #region activity=true -->
#### My thoughts on how a real robot might compare

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region activity=true -->
The following video clip shows a simple Lego robot executing the `Stay_inside` program discussed above.

A the real robot may not shuttle backwards and forwards as precisely as the simulated robot. Real robots are "noisy", but not just in terms of the sound they make. There is also "noise" in their mechanical gearing and control: the motors don't go at precisely the expected speed, the gears may not mesh perfectly, the wheels may slip or skid, and the sensors do not give instantaneous or perfect readings.

In other words, real robots may have sloppy and relatively unpredictable mechanisms so that the same control commands from the same initial position may result in a variety of outcomes. For this reason, the RoboLab simulator has a noise feature that allows you to set random variations to the motor speeds and sensor readings. This "noise" makes the simulated robot behave more realistically. It will be used in later RoboLab sessions. 
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
### Viewing the stay inside test on a real robot

__TO DO: should we try to have a video of an EV3 executing the same programe (ideally), or an equivalent one?__

<br/><br/>
<div class='alert-danger'>TO DO: the programmes should work on an EV3 running [`python-ev3dev`](https://python-ev3dev.readthedocs.io/). A [Visual Studio Code extension for browsing ev3dev devices](https://github.com/ev3dev/vscode-ev3dev-browser) seems to provide an environment for running the `python-ev3dev` code on a real robot which is perhaps something worth exploring. *Note that VS Code can also run notebooks, although I'm not sure if the simulation widget will run in that environment.*</div>
<br/><br/>
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
## Using Less Magic...

In the previous program, the `tank_drive` and `tank_turn` elements are predefined by our use of the `%%sim_magic_preloaded` magic. This really is a bit like magic, because it allows us to write Python code that would not ordinarliy be valid code. In the background, the magic itself defines some essential Python code that is *prepended* (that is, added to the start of) out programme code before it is downloaded to the simulated robot.

The following code cell uses a slightly less powerful magic, `%%sim_magic_imports`, that still masks some of the complexity in creating a valid Python programme although in this case it does require you to define the `tank_turn` and `tank_move` statements in turns of slightly lower level building blocks.

As with the `Move_a_robot` programme, the `MoveSteering` and `MoveTank` commands are commands provided the `ev3dev` Python package and then configured to use particular outputs on the (simulated) robot (`OUTPUT_B` and `OUTPUT_C`).

In addition, the light sensor is defined using the `ColorSensor` command to configure the sensor attached to `INPUT_2` as a colour sensor. The light sensor is shown as small white circle contained within a grey square on the simulated robot.
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic_imports

# Stay inside
tank_turn = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

colorLeft = ColorSensor(INPUT_2)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity_pc))
    if colorLeft.reflected_light_intensity_pc < 40:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)
        # drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

__TO DO: I have some magic, [`nb_cell_diff`](https://github.com/innovationOUtside/nb_cell_diff), that displays the differences between code cells, which could be used to show how the contents of this cell differ from the contents of the previous cell; it doesn't work properly with magicked cells yet, but I'll fix that next time I get a chance to look at that extension's code.__

```python
# example of differ not quite working yet
# also need to use the correct cell run index values
#%pip install git+https://github.com/innovationOUtside/nb_cell_diff.git
%load_ext nbcelldiff
%diff_magic --compare 27,28
```

<!-- #region hideCode=true hidePrompt=true -->
## A Complete Python Programme


The following code cell shows a fully defined Python program. In this case, a series of "package import" statements appear at the start of the programme. Python packages are code libraries written to support particular activities.

The core Python language includes a variety of packages that are distributed as part of the Python language, but additional packages can be written using core Python language elements, *or* Python commands imported from other additional packages, to build ever more powerful commands.

In particular, the Python `ev3dev` package provides a range of language constructs that allow us to write a Python programme that can work with a Lego EV3 brick running the `ev3dev` operating system, or our `nbev3devsim` simulated robot.

As you can see from the code cell below, which uses the minimal `%%sim_magic` magic to download just the contents of the cell to the simulator, in this case we `import` the custom elements we need `from` the `ev3dev` Python package that we then make use of in our programme. 
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic

# Stay inside
from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor

tank_turn = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
colorLeft = ColorSensor(INPUT_2)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity_pc))
    if colorLeft.reflected_light_intensity_pc < 40:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)
        # drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```



<!-- #region hideCode=true hidePrompt=true -->
## Robots that speak

As well as moving about the simulated world, the robot can also affect the state of the world by making a noise it. In particular, we can get the robot to speak by using a function from the `playsound` package (created as a custom package for use in this module in the javascript Skulpt/Python environment): `playsound.say()`.

Run the following code cell to download the programme to simulator and then run it in the simulator. Does it say hello?!
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic
# Say hello
import playsound

your_name = "TM129 student"
playsound.say("Hello there," + your_name)
```

<!-- #region hideCode=true hidePrompt=true -->
See if you can modify the name string so that the robot says something that sounds more like *tee, em, one, two, nine* rather than *one hundred and twenty nine*. Run the modified code cell to download the programme to the simulator, and then run the programme there to test it.

Can you also get the robot to say hello to you using your own personal name?
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
## Robots That Count

That's a good start with regards to getting the robot to speak, but can we do something more elaborate?

How about counting up from 1 to 5?

The Python `range()` function can be used to generate an iterator (a loopy thing...) over a series of integers that cover a certain range:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
range(5)
```

We can enumerate the contents of an enumerator by casting it to an explicit list of values:

```python
list(range(5))
```

<div class='alert alert-warning'>You'll see that by default, the list of values returned from the `range()` starts is the index value `0`. The value `0` is conventionally used to represent the first index value in a series because it quite often makes lots of other things easier...</div>

<!-- #region hideCode=true hidePrompt=true -->
We can use a `for` loop to iterate through the range, displaying each value within the range using a `print()` statement:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
for i in range(5):
    print(i)
```

<!-- #region hideCode=true hidePrompt=true -->
If we supply just a single value to the `range()` function, as in `range(N)`, it defines a range that spans from $0$ to $N-1$.
<!-- #endregion -->

```python hideCode=true hidePrompt=true
M = 5

list(range(M))
```

<!-- #region hideCode=true hidePrompt=true -->
If we provide two arguments, `range(M, N)`, it defines a range from $M$ to $N-1$:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
M = 5
N = 10

list(range(M, N))
```

<!-- #region hideCode=true hidePrompt=true -->
If we provide *three* arguments, `range(M, N, S)`, it spans a range of integeres from $M$ to $N-1$ with a step value $S$ between them:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
M = 0
N = 30
S = 10

list(range(M, N, S))
```

<!-- #region hideCode=true hidePrompt=true -->
If we set $M=0$, $N=30$ and $S=10$, the first value returned from the range is the intial start value, $0$.

We then add a step of $10$ to get the next value ($10$).

Adding another step of $10$ gives us the next number in the range: $20$.

If we now try to add another $10$, that gives us a total of $30$, which is *outside* the upper range of $N-1$, and so that number is not returned as within the range.
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
Now let's see if we can get our robot to count up to five in the simulator.

Note that the `playsound.say()` function accepts a *string* value, so if we want it to speak a number aloud we must first cast it to a string; for example, `str(5)`.

__TO DO: maybe define a "say_number()" function? Or may say more robust and error trap / cast non-strings to string values? [Related issue](https://github.com/innovationOUtside/nbev3devsim/issues/37).__

Run the following code cell to download the programme to the simulator and then run it in the simulator. What happens? Does the robot count up to five? 
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic
# I can count...
import playsound

for i in range(5):
    playsound.say(str(i))
```

<!-- #region hideCode=true hidePrompt=true -->
Although we set the range value as $5$, remember that ths means the robot will count, by default, from $0$ in steps of $1$ to $N-1$. So the robot will count $0, 1, 2, 3, 4$, as we can see if we explicitly enumerate the values created by the `range()` statement:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
list(range(5))
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Activity
In the following code cell, create a `range()` statement that will creates a list of numbers from $1$ to $5$ inclusive. Use a `list()` statement to generate a list from the `range()` statement.

Run the code cell to display the result so you can check your answer:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
# Display a list of values [1, 2, 3, 4, 5] created from a single rannge() statement

# YOUR CODE HERE
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
Now create a programme that will cause the simulated robot to count from 1 to 5 inclusive.

Run the cell to download the programme to the simulator, and then run it in the simulator. Does it behave as you expected?
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
%%sim_magic
# Count from 1 to 5 inclusive

# ADD YOUR CODE HERE
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
Can you modify your program so that it counts from ten to one hundred, inclusive, in tens (so, *ten, twenty, ..., one hundred*)?
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true hidden=true -->
We can display a range of values from $1$ to $5$ inclusibe by using a range command of the form `range(M, N)` where `M=1`, the initial value, and $N=5+1$, since the the range spans to a maximum value less than or equal to $N-1$:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true hidden=true
list(range(1, 6))
```

<!-- #region hideCode=true hidePrompt=true activity=true hidden=true -->
We can now create a programme that counts fom one to five inclusive:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true hidden=true
%%sim_magic
# I can count from one to five inclusive...
import playsound

start_value = 1
# To get the desired final value, it must be within the range
# So make the range one more than the desired final value
end_value = 5 + 1

for i in range(start_value, end_value):
    playsound.say(str(i))
```

<!-- #region hideCode=true hidePrompt=true activity=true hidden=true -->
To count from ten to one hundred in tens, we need to add an additional step value as well as the range limit values:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true hidden=true
%%sim_magic
# I can count from ten to one hundred in tens...
import playsound

start_value = 10
end_value = 100 + 1
step_value = 10

for i in range(start_value, end_value, step_value):
    playsound.say(str(i))
```

<!-- #region hideCode=true hidePrompt=true -->
## Announcing Bands As The Robot Encounters Them

One of the ways we can use the `playsound.say()` function is to count out the bands as we come across them. To do this, we need to identify when we cross from the white background onto a band.

We can detect the edge of a band by noticing when the sensor value goes from white (a reading of $100$) to a lower value. The following program will detect such a transition and say that it has crossed onto a band, also displaying a print message to announce the fact too.

Reset the robot location in the simulator, run the following cell to download the program to the simulator, and then run it in the simulator. Does it behave as you expected?
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic_preloaded --background Grey_bands
# Onto a band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity_pc

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity_pc ))
    current_value = colorLeft.reflected_light_intensity_pc
    if previous_value==100 and current_value < 100:
        print('Onto a band...')
        playsound.say("New band")

    previous_value = current_value
```

<!-- #region hideCode=true hidePrompt=true -->
The programme starts by turning the motors on to drive the robot forward (`tank_drive.on(SpeedPercent(50), SpeedPercent(50))`) and then taking a sample of the light sensor reading (`previous_value = colorLeft.reflected_light_intensity_pc`).

The `while True:` statement creates a loop that repeats until the programme in the simulator is manually stopped. Inside the loop, a new sample is taken of the light sensor reading (`current_value = colorLeft.reflected_light_intensity_pc`):

If the robot was on the white background on the previous iteration (`previous_value==100`) __and__ on a band in this iteration — that is,  `and (current_value < 100)` — then the robot has moved onto a band; declare this via the output display window (`print('Onto a band...')`) and audibly (`playsound.say("New band")`).

The `previous_value` variable is then updated to the current value (`previous_value = current_value`) and the programme goes round the loop again.
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
You may notice that there may be a slight delay between the robot encountering a band and saying that it has done so. This is because it takes some time to create the audio object inside the browser. If we were to speed up the robot's forward motion, it's quite possible that the robot might leave one band and encounter the next before it had finished saying it had entered the first band.

*TO DO: if we queue too many audio messages, things get painful and we need to clear the speech buffer (maybe reload the page?) See [related issue](https://github.com/innovationOUtside/nbev3devsim/issues/8) for how we might start to fix this.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Activity - Announce When the Robot Has Left a Band

In the code cell below, the previous robot control program has been modified so that the robot says "on" when it goes onto a band. Modify the programme further so that it also says, "off" when it goes from a band and back onto the white background.

Reset the robot location, download the program to the simulator and run it there. Does it behave as you expect?
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
%%sim_magic_preloaded
# On and off band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity_pc

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity_pc ))
    current_value = colorLeft.reflected_light_intensity_pc
    if previous_value==100 and current_value < 100:
        print('Onto a band...')
        playsound.say("On")
    
    #YOUR CODE HERE
    
    
    previous_value = current_value
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
To detect when the robot has left a band, we can check to see if it was on a band on the previous iteration of the `while True:` loop (`previous_value < 100`) and back on the white background on the current iteration (`current_value == 100`).
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
%%sim_magic_preloaded
# On and off band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity_pc

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity_pc ))
    current_value = colorLeft.reflected_light_intensity_pc
    if previous_value==100 and current_value < 100:
        print('Onto a band...')
        playsound.say("On")
    
    if previous_value < 100 and current_value == 100:
        print('Off a band...')
        playsound.say("Off")
    
    previous_value = current_value
```

### Creating Your Own Programme From Scratch

You've already seen several robot control programmes in this notebook, and you now you have an opportunity to create your own from scratch.

The following activity includes the skeleton of a programme based on descriptive, non-executed comments that describe what each line of the programme should do.

Using comments in this way provides one way of helping you plan or design a new programme.

As for the lines of code that you will need to write: you have already seen examples of similar lines in the programmes you have already encountered.

Reusing lines of code copied from programmes that have used such lines successfully in previous programmes is a completely valid way of writing your own programmes.

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Activity - Count the Bands

Using the previous programmes as inspiration, see if you can write a program that counts each new line as it encounters it, displaying the count to the output window and speaking the count number aloud.

Reset the location of the robot, download your program to the simulator and run it there. Does it work as you expected?

*Hint: you may find it useful to create a counter, initially set to 0, that you increment whenever you enter a band, and then display it and speak it aloud.*

*Another hint: remember, the `playsound()` function must be passed a string, rather than an integer, value.*
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
%%sim_magic_preloaded
# Count the bands aloud

# Import necessary package(s)


# Start the robot moving

# Initial count value

# Initial sensor reading

# Create a loop

    # Check current sensor reading
    
    # Test when the robot has entered a band

        # When on a new band:
        # - increase the count

        # - display the count in the output window
    
        # - say the count aloud

    # Update previous sensor reading
    
```

<!-- #region hideCode=true hidePrompt=true activity=true heading_collapsed=true -->
### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true hidden=true -->
Using the comment skeleton as a plan for the program, we can reuse statements from the previous programmes wwith just a few additions.

In the first case, we need to add a counter (`count = 0`). Inside the loop, when we detect we are on a new band, increase the counter (`count = count + 1`), display it (`print(count)`) and after casting the count to string value, speak it aloud (`playsound.say(str(count))`).

Note that we could make out output display message a little bit more elaborate by constructing an output message string, such as `print("Band count is" + str(count))`. *(Unfortunately, the simulator does not support the rather more elaborate Python "f-string" formatting method that allows variable substitution within text strings.)*
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true hidden=true
%%sim_magic_preloaded
# Count the bands aloud

# Import necessary package(s)
import playsound

# Start the robot moving
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

# Initial count value
count = 0

# Initial sensor reading
previous_value = colorLeft.reflected_light_intensity_pc

# Create a loop
while True:

    # Check current sensor reading
    current_value = colorLeft.reflected_light_intensity_pc
    
    # Test when the robot has entered a band
    if previous_value==100 and current_value < 100:
        # When on a new band:
        # - increase the count
        count = count + 1
        # - display the count in the output window
        print(count)
        # - say the count aloud
        playsound.say(str(count))
        
    # Update previous sensor reading
    previous_value = current_value
```
<!-- #region hidden=true -->

<!-- #endregion -->
