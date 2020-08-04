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

# 2 Branches


So far we have concentrated mainly on sequential programs, where the flow of control proceeds through the program statements in linear sequence, except when it encounters a loop element where the control flow is redirected back ‘up’ the program to the start of a loop block.

In the previous notebook, you saw how the conditional `if...` statement could be used to optionally pass control to a set of instructions in the sequential program *if* a particular condition was met.

The `if...` statement fits the the sequential program model by redirecting control flow, albeit briefly, to a set of ‘extra’ commands if the conditional test evaluates to true.

A sequential program will always follow the same sequentially ordered path. But to be useful, a robot program will often need to make decisions and behave differently in different circumstances. To do this, the program has to have alternative *branches* in the program flow where it can follow different courses of action depending on some conditional test.

Python provides an `if...else...` statement to do just that, and you will see how it is used in the following activities.

*In other programming languages, this construct may be referred to as an `if...then...else...`. In Python, the ‘then’ is assumed.*


## 2.1 Activity – Detecting black and grey

Load the *Grey\_and\_black* background into the simulator.

Download the program to the simulator and then run it several times with the robot moved to different starting positions.

What does the program cause the robot to do?

<font color='red'>JD: as in the previous notebook, the variable `sensor_value` doesn't vary between 0 and 100 (as I think the code expects), but between 0 and 255. When I change '100' to '255' in the condition in the while loop, then it runs as intended.</font>

```python
%%sim_magic_preloaded

import playsound

# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

#Check the light sensor reading
while sensor_value == 100:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity
    # and display it
    print(sensor_value)

# When the reading is below 100
# we have started to see something.
# Drive a little way onto the band to get a good reading
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 0.2)

#Check the sensor reading
sensor_value = colorLeft.reflected_light_intensity
# and display it
print(sensor_value)

# Now make a decision about what we see
if sensor_value < 50:
    playsound.say("I see black")
else:
    playsound.say("I see grey")
```

<!-- #region activity=true -->
### Activity

When you run the program, what does the robot do? 
<!-- #endregion -->

<!-- #region student=true -->
*Double click this cell to edit it and add your description here.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The robot moves forward over the white background until it reaches the grey or black area. If the background is black, then the robot says *black*; otherwise, it says *grey*. 

The program works by driving the robot forwards and continues in that direction while it is over the white background (a reflected light sensor reading of 100). When the light sensor reading goes below the white background value of 100, control passes out of the while loop and on to the statement that drives the robot forwards a short distance further (0.2 wheel rotations) to ensure the sensor is fully over the band. The robot then checks its sensor reading again, and makes a decision about what to say based on the value of the sensor reading.
<!-- #endregion -->

### Working through the program flow

The following flow chart shows how the flow of control passes through the program.

<font color='red'>JD: In both versions of the flow chart, it looks like if the light reading is less than the value (which is <100 in one and ==255 in the other flow chart) then there is a loop that simply displays the reading: should this loop also say something about keep moving forwards?</font>

```python
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget
```

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Move forwards
cond1=>condition: Light < 100?
op2=>parallel: Display reading
op3=>operation: Drive forward a short way
cond2=>condition: Light < 50?
op4=>operation: Say "grey"
op5=>operation: Say "black"

st(right)->op1(right)->cond1({'flowstate':{'cond1':{'yes-text' : 'ssno', 'no-text' : 'yes'}}} )
cond1(no,right)->op2(path1, top)->cond1
cond1(yes)->op3->cond2
cond2(no)->op4->e
cond2(yes)->op5->e

```

<!-- #region tags=["production_note"] -->
<div class='alert alert-warning'>The flowchart.js layout algorithm will allow us to change yes/no labels on conditions, but the magic does not currently provide a way to pass alternative values in (eg swapping yes/no labels to change the sense of the decision as drawn). Also, the layout algorithm seems to be broken when swapping yes and no.</div>
<!-- #endregion -->

![](https://mermaid.ink/img/eyJjb2RlIjoiXG5ncmFwaCBURFxuICAgIEEoU3RhcnQpIC0tPiBCW01vdmUgZm9yd2FyZHNdXG4gICAgQiAtLT4gQ3tMaWdodCA9PSAyNTV9XG4gICAgQyAtLT4gfFllc3wgRFtEaXNwbGF5IHJlYWRpbmddXG4gICAgRCAtLT4gQ1xuICAgIEMgLS0-IHxOb3wgRVtEcml2ZSBmb3J3YXJkPGJyLz5hIHNob3J0IHdheV1cbiAgICBFIC0tPiBGe0xpZ2h0IDwgMTI4P31cbiAgICBGIC0tPiB8WWVzfCBHW1NheSAnYmxhY2snXVxuICAgIEYgLS0-IHxOb3wgSFtTYXkgJ2dyZXknXVxuICAgIEcgLS0-IEkoRW5kKVxuICAgIEggLS0-IElcbiAgICBcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<font color='red'>JD: long description needed.</font>

Although the `while` command does appear to offer some sort of branch-like behaviour, we still think of it as a sequential-style operator becuase the flow of control keeps trying to move in the same forwards direction.

In the branching `if...else...` operator, the program control flow takes one of two different ‘forward-flowing’ paths depending on whether the conditional statement evaluated as part of the `if...` statement evaluates to true or false. If it evaluates to `True`, then the statements in the first if block of code are evaluated; if the condition evaluates to `False`, then the statements in the else block are evaluated. In both cases, contorl then flows forwards to the next statement after the if...else... block.

<!-- #raw -->
# Mermaid.js code

graph TD
    A(Start) --> B[Move forwards]
    B --> C{Light == 100}
    C --> |Yes| D[Display reading]
    D --> C
    C --> |No| E[Drive forward<br/>a short way]
    E --> F{Light < 50?}
    F --> |Yes| G[Say 'black']
    F --> |No| H[Say 'grey']
    G --> I(End)
    H --> I
    
<!-- #endraw -->

<font color='red'>JD: The Mermaid code is showing above.</font>

<!-- #region activity=true -->
## 2.2 Activity – Stepping through an `if...else...` statement
<!-- #endregion -->

<!-- #region activity=true -->
In this activity we will look at another program to explore how `if...else...` works in more detail. 

Inspect the code in the following cell. If you run the code cell, what do you think will happen?
<!-- #endregion -->

<!-- #region student=true -->
*Double-click this cell to edit it and make your prediction here.*
<!-- #endregion -->

<!-- #region activity=true -->
Once you have made your prediction, run the following cell. In the cell beneath it, record what happened and how it compared to your prediction.

*You may find it informative to use `nbtutor` to step through each line of code in turn to see how the program flow progresses. To do this, uncomment the `%%nbtutor` magic in the first line of the code cell by deleting the `#` at the start of the line before running the code cell.*
<!-- #endregion -->

```python activity=true
#%%nbtutor --reset --force
x = 1

if x == 1:
    print("x equals 1")
else:
    print("x does not equal 1")
    
print("All done...")
```

<!-- #region student=true -->
*Double-click this cell to edit it to record here what happened when you ran the code in the above cell. Did its behaviour match your prediction?*
<!-- #endregion -->

<!-- #region activity=true -->
What do you think will happen when you run the following code cell?

Run the cell and use *nbtutor* to step through the program. How does the program flow differ from the case where `x` had the value `1`? 
<!-- #endregion -->

```python activity=true
%%nbtutor --reset --force
x = 2

if x == 1:
    print("x equals 1")
else:
    print("x does not equal 1")

print("All done...")
```

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
In the cell where `x = 1`, I predicted that the program would print the message *'x equals 1'* and then the messge *'All done...'*.

Viewing the trace, I could see how the program started by initialising the `x` variable to the value `1`, then checked whether `x == 1` (that is, whether `x` was equal to `1`); because it was, the program then moved onto the `print("x equals 1")` statement and printed the first message. Then the program flow continued to the first instruction after the `if...else...` block, which was the statement that printed the *'All done...'* message.

When I ran the program with a value of `x` other then `1`, the control passed from the `if...` statement, where the conditional test evaluated as `False`, to the first line in the `else...` block, which printed the message *'x does not equal 1'*, before moving onto the first line after the `if...else...` block as before.
<!-- #endregion -->

## 2.3 An `if...` without an `else...`


It is sometimes useful to have just a single branch to the `if` statement. Python provides a simple `if...` statement for this purpose.<font color='red'>JD: students have already seen `if` on its own in the previous notebook. Mention this?</font>

<!-- #region activity=true -->
### Activity – An `if` on its own

Run the following code cell as it stands, with the `x` variable taking the intial value `1` (`x = 1`). Can you predict what will happen?
<!-- #endregion -->

```python activity=true
#%%nbtutor --reset --force
x = 1

print("Are you ready?")

if x == 1:
    print("x equals 1")

print("All done...")
```

<!-- #region activity=true -->
Try to predict what will happen if you change the initial value and run the cell again.
<!-- #endregion -->

<!-- #region student=true -->
*Double-click this cell to edit it and record your own prediction*
<!-- #endregion -->

<!-- #region activity=true -->
Run the code cell above again with a modified initial value. Was your prediction about what would happen correct? Make a note in the cell below about how successful your prediction was. If your prediction was incorrect, try to explain why you think your prediction was different to how the program actually behaved.
<!-- #endregion -->

<!-- #region student=true -->
*Double-click this cell to edit it to record notes on the success or otherwise of your own prediction.*
<!-- #endregion -->

<!-- #region activity=true -->
Uncomment the *%%nbtutor* magic and run the code cell using different values of `x`, observing how the program flow progresses in each case.
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
With the initial value of the variable `x` set to `1` (`x = 1`) the program displayed the messages *Are you ready?*, *x equals 1* and *All done...* because the `if...` statement evaluated the `x == 1` test condition as `True` and passed control *into* the `if...` block.

When `x` was initialised to a different value, for example as `x = 2`, only the messages *Are you ready?* and *All done...* were displayed because the `if...` conditional test failed and redirected control flow to the first statement *after* the `if...` block.
<!-- #endregion -->

## 2.4 Combining loops and branching statements 


It is important to be clear that the condition in a branching statement (`if...` or `if...else...`) is checked only when execution reaches that part of the program.

In the examples above, you stepped through the programs and saw that execution passed through the `if` statement only once. When creating useful robot programs, we often want conditions to be checked repeatedly. For example the robot may need to repeatedly check that it has not bumped into an obstacle, or whether it has found a bright or dark area. 

You have already seen how the `while...` loop tests a condition at the start of a loop and and then passes control to the statements inside the loop before looping back to test the `while...` condition again.

You may also recall from an earlier notebook that we also used an `if...` statment to return the control flow back to the top of a loop before all the statements in the loop body had been executed, or break out of a loop early and pass control to the first statement after the loop block.

This ability to combine loop and branching statements is very powerful and even a very simple program can produce quite complex robot behaviour.

<!-- #region activity=true -->
### Activity – Combining loops and branching statements 


Can you predict what the following program will cause the robot to do when it is downloaded and run in the simulator using the *Loop* background with the robot initially placed inside the loop ?
<!-- #endregion -->

<!-- #region student=true -->
*Double click this cell to edit it and record your prediction.*
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded --background Loop

tank_drive.on(SpeedPercent(30), SpeedPercent(30))

while True:
    if colorLeft.reflected_light_intensity < 100:
        tank_drive.on_for_rotations(SpeedPercent(-30),
                                    SpeedPercent(-30), 2)

        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(30), SpeedPercent(30))

```

<!-- #region activity=true -->
Download the program to the simulator and run it there to check your prediction. After a minute or two, stop the program from executing.

How does the behaviour of the program lead to the robot’s emergent behaviour in the simulator?
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
When the program runs, the robot will explore the inside of the black oval, remaining inside it and reversing direction each time it encounters the black line.

The program is constructed from an `if` statement inside a *forever* loop. The `if` statement checks the light sensor reading; when this is low (which it will be when the black line is reached) the motor direction is reversed. 

The `while True:` loop is a so-called *infinite loop* that will run indefinitely. In this case it is useful because we want the robot to continue to keep on behaving in the same way as the program runs.

In other circumstances, we might want the loop to continue only while some condition holds true. In such cases, using the `while` statement to test the truth of a conitional statement is more useful.
<!-- #endregion -->

## 2.5 Multiple conditions Using `if...elif...else...`

The `if...else...` statement allows us to creating a branching control flow statement that performs a conditional test and then chooses between two alternative outcomes depending on the result of the test.

Python also supports a yet more complex branch construction in the form of an `if...elif...else...` statement that allows us to make multiple conditional tests. Run the following code cell and then use `nbtutor` to explore the flow through the program.<font color='red'>JD: Note that nbtutor is already 'on'; should it be commented out to start with?</font> 

```python
%%nbtutor --reset --force

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

for day in days_of_week:
    print(f'Today is {day}...')
    
    if day == 'Wednesday':
        print('...half day closing')
    elif day in ['Saturday', 'Sunday']:
        print('...the weekend')
    else:
        print('...a weekday')
        
print("And that's all the days of the week.")
```
<font color='red'>JD: This is the first time that nbtutor has worked nicely.</font>

We can also have multiple `elif` statements between the opening `if...` and the closing `else`.

Read through the code in the following code cell. Try to work out what the program will do and how the control flow will pass though the program as it executes.

```python
# TO DO
# need a simple toolbar buttom to toggle the notebook display?
from IPython.display import HTML
display(HTML("<style>#notebook-container { width:100% !important; float:left !important;}</style>"))
display(HTML("<style>#notebook-container { width:50% !important; float:left !important;}</style>"))

```
<font color='red'>JD: The above needs to be addressed.</font>

```python
%%nbtutor --reset --force

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

for day in days_of_week:
    message = f'Today is {day}...'
    print(message)
    
    if day == 'Monday':
        feeling = "...I don't like Mondays..."
    elif day == 'Tuesday':
        feeling = '...Ruby Tuesday'
    elif day == 'Friday':
        feeling = "...Friday I'm In Love"
    else:
        feeling = "...I don't know a song title for that day"
    
    print(feeling)
```

Now run the previous code cell and step through its execution using *nbtutor*<font color='red'>JD: Note that nbtutor is already 'on'; should it be commented out to start with?</font>; observe how the control flow steps increasingly through the stack of `...elif...` tests as the `for...` loop iterates through the items in the `days_of_week` list. 


Note that there is no requirement that you test the same variable in each step. The different steps could test a different variable or range of variables.

For example, in the following program we might decide what to take out with us on a walk based on a variety of conditions:

```python
raining = False
temperature = 'warm'

if raining:
    print("Wear boots")
elif temperature == 'warm':
    print("Wear sandals")
else:
    print("Wear shoes")
```

<!-- #region -->
Also note that there is an *order* in which we test the various conditions as the control passes through the `if...elif...` conditional tests. We can use this as an informal way of prioritising one behaviour over another:

```python
if this_really_important_thing:
    ...
elif this_less_important_thing:
    ...
elif this minor_thing:
    ...
else:
    ...
```
<!-- #endregion -->

<!-- #region activity=true -->

## 2.6 Challenge – Three shades of grey
<!-- #endregion -->

<!-- #region activity=true -->
The program at the start of this notebook (in Section 2.1) showed how an `if...else...` statement could be used to decide between black and grey areas. The background (loaded into the simulator as the *Grey\_and\_black* background) actually contains four different shades: black, dark grey, medium grey and light grey. Can you construct a program that will report which shade the robot encounters? 

A copy of the original program is provided below as a starting point. You will need to extend the code so that it can decide between three grey alternatives as well as the black band and say which band it saw.
<!-- #endregion -->

<font color='red'>JD: I needed to add "from ev3dev2.sensor import INPUT_2" to make this work (and change '100' to '255' as the value of 'white').</font>

```python activity=true
%%sim_magic_preloaded

# Use this program with the 'Grey_and_black' background

import playsound

# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

#Check the light sensor reading
while sensor_value == 100:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity
    # and display it
    print(sensor_value)

# When the reading is below 100
# we have started to see something.
# Drive a little way onto the band to get a good reading
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 0.2)

#Check the sensor reading
sensor_value = colorLeft.reflected_light_intensity
# and display it
print(sensor_value)

# Now make a decision about what we see
if sensor_value < 50:
    playsound.say("I see black")
else:
    playsound.say("I see grey")
```

<!-- #region activity=true -->
When you have modified the code, run the cell to download it to the simulator, ensure the *Grey\_and\_black* background is loaded, and then run the program in the simulator for various starting positions of the robot. Does it behave as you intended?
<!-- #endregion -->

<!-- #region student=true -->
*Use this cell to record your own notes and predictions related to this challenge.*
<!-- #endregion -->

<!-- #region activity=true -->
#### Hint: click the arrow in the sidebar or run this cell to reveal a hint.
<!-- #endregion -->

<!-- #region activity=true -->
The original program uses an `if...else...` condition to distinguish between black and grey reflected light readings. An `...elif...` statement lets you test alternative values within the same `if...else...` block.

To identify the values to use in the condition statements, inspect the simulator output window messages to see what sensor values are reported when the robot goes over different bands.
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->

#### Worked answer

*Click the arrow in the sidebar or run this cell to display a worked answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The robot sees the following values over each of the grey bands:

- light grey: ~86
- medium grey: ~82
- dark grey: ~50
- black: 0

Generally, when we see lots of decimal places, we assume that the chances of ever seeing exactly the same sequence of numbers may be unlikely, so rather than testing for an exact match, we use one or more threshold tests to see if the number lies within a particular *range* of values, or is above a certain minimum value.

If we assume those sensor readings are reliable, and the same value is always reported for each of those bands, then we can make the make the following decisions:

```python
if sensor_value > 86: 
    print('light grey')
elif sensor_value > 82: 
    print('medium grey')
elif sensor_value > 50: 
    print('dark grey')
else:
    print('black')
```

We can make the test even more reliable by setting the threshold test values to values that are halfway between the expected values for a particular band. For example, 84, rather than 82, for distinguishing between light and medium grey; 66 rather than 82 for distinguishing between dark and medium grey; and 25 rather than 50 for distinguising between black and dark grey.

__TO DO: an activity with noise values around the sensor would be useful here._<font color='red'>JD: To be resolved.</font>

This means that if there is a slight error in the reading, our thresholded test is likely to make the right decision about which side of the threshold value the (noisy) reading actually falls on.

__ TO DO - a diagram to illustrate this would be useful. __<font color='red'>JD: To be resolved.</font>
<!-- #endregion -->

```python activity=true hidden=true
%%sim_magic_preloaded

# Use this program with the 'Grey_and_black' background

import playsound

# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

#Check the light sensor reading
while sensor_value == 100:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity
    # and display it
    print(sensor_value)

# When the reading is below 100
# we have started to see something.
# Drive onto the band to get a good reading
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 0.2)

#Check the sensor reading
sensor_value = colorLeft.reflected_light_intensity
# and display it
print(sensor_value)

# Now make a decision about what we see
if sensor_value >  86: 
    playsound.say("I see light grey")
elif sensor_value > 82: 
    playsound.say("I see medium grey")
elif sensor_value > 50: 
    playsound.say("I see dark grey")
else:
    playsound.say("I see black")
```


<!-- #region activity=true hidden=true -->
Other solutions are possible.

One thing you might notice is that sometimes the robot gives the wrong answer, for example if the sensor is not completely over the band and gives a reading that does not exactly match a value you used in your conditional tests.

You will see how to address this sensitivity in the next notebook.
<!-- #endregion -->

## Summary

In this notebook, you have seen how `if...` statements can be used to make a variety of decisions and trigger a range of different actions based on one or more tested conditions. In particular:

- a simple `if...` statement lets us perform one or more actions once and once only if a single conditional test evaluates to true
- an `if...else...` statement allows us to *branch* between two possible futures based on the whether a single conditional test evaluates to true; if it is true, do one action, if not, do the other
- an `if...elif...else...` construction lets us run mutliple different conditional tests. If the first test is true, do one thing, otherwise test the next thing, and if that is true, do something, otherwise, do another test, and so on. If all the other `elif...` tests evaluate to false, then do the final `else` condition.

<!-- #region commentate=true -->
## Addendum

Sometimes it can be useful to draw on additional resources that provide alternative explanations of particulalry challenging topics. This addendum (which like all addendum sections is *not required* to successfully pass this module) gives an example of how to embed YouTube video resources that you may have found to supplement your own personal notes or comments.
<!-- #endregion -->

<!-- #region commentate=true -->
The IPython interpreter that underpins code execution in Jupyter notebooks has a range of display functions that are capable of embedding and playing a wide variety of media, include audio and video files.

For example, if you run the following code cell, then you can embed a YouTube video given the unique video identifier which you will find in every YouTube video URL (web address):
<!-- #endregion -->

```python commentate=true
from IPython.lib.display import YouTubeVideo
YouTubeVideo('mGgMZpGYiy8')
```

<!-- #region commentate=true -->
What, me, dodgy goth? Goth hippy groover, more like... ;-)
<!-- #endregion -->
