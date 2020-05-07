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

# 3 Branches


So far we have concentrated mainly on sequential programs, where the flow of control proceeds through the program statements in linear sequence, except when it encounters loop element where the control flow is redirected back "up" the program to the start of a loop block.

In the previous notebook, you saw how the conditional `if..` statement could be used to optionally pass control to a set of instructions in the sequential programme *if* a particular condition was met.

The `if...` statement fits the the sequential program model by redirecting control flow, albeit briefly, to a set of "extra" commands if the conditional test evaluates true.

A sequential program will always follow the same sequentially order path. But to be useful, a robot program will often need to make decisions and behave differently in different circumstances. To do this, the program has to have alternative *branches* in the programme flow where we can follow different courses of actions depending on some conditional test.

Python provides an `if..else..` statement to do just that, and you will see how it is used in the following activities.

*In other programming languages, this may often be referred to as an `if...then...else...` construct. In Python, the "then" is assumed.*


## 3.1 Activity: Detecting black and grey


Load the *Grey and black* background into the simulator.

Download the programme to the simulator and then run it several times with the robot moved to different starting positions.

What does the programme cause the robot to do?

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
while sensor_value == 255:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity
    # and display it
    print(sensor_value)

# When the reading is below 255
# we have started to see something.
# Drive a little way onto the band to get a good reading
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 0.2)

#Check the sensor reading
sensor_value = colorLeft.reflected_light_intensity
# and display it
print(sensor_value)

# Now make a decision about what we see
if sensor_value < 128:
    playsound.say("I see black")
else:
    playsound.say("I see grey")
```

#### Question

What does the robot do? 


#### Answer

*Click the arrow in the sidebar to reveal the answer.*


The robot moves forward over the white background until it reaches the grey or black area. If the background is black, the robot says *black*; otherwise, it says *grey*. 

The programme works by driving the robot forwards and  continues in that direction while it is over the white background (a reflected light sensor reading of 255). When the light sensor reading goes below the white background value of 255, control passes out of the while loop and on to the statement that drives the robot forwards a short distance further (0.2 wheel rotations) to ensure the sensor is fully over the band. The robot then checks its sensor reading, and makes a decision about what to say based on the value of the sensor reading.


### Working through the programme flow

The following flow chart shows how the flow of control passes through the programme.

![](https://mermaid.ink/img/eyJjb2RlIjoiXG5ncmFwaCBURFxuICAgIEEoU3RhcnQpIC0tPiBCW01vdmUgZm9yd2FyZHNdXG4gICAgQiAtLT4gQ3tMaWdodCA9PSAyNTV9XG4gICAgQyAtLT4gfFllc3wgRFtEaXNwbGF5IHJlYWRpbmddXG4gICAgRCAtLT4gQ1xuICAgIEMgLS0-IHxOb3wgRVtEcml2ZSBmb3J3YXJkPGJyLz5hIHNob3J0IHdheV1cbiAgICBFIC0tPiBGe0xpZ2h0IDwgMTI4P31cbiAgICBGIC0tPiB8WWVzfCBHW1NheSAnYmxhY2snXVxuICAgIEYgLS0-IHxOb3wgSFtTYXkgJ2dyZXknXVxuICAgIEcgLS0-IEkoRW5kKVxuICAgIEggLS0-IElcbiAgICBcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

Although the `while` command does appear to offer some sort of branch like behaviour, will still think of it as a sequential style operator becuase the flow of control keeps trying to move in the same forwards direction.

In the branching `if..else..` operator, the program control flow takes one of two different "forward flowing" paths depending on whether the conditional statement evaluated as part of the `if..` statement evaluates true or false.

If it evaluates `True`, then the statements in the first "if" block of code are evaluate; if the condition evaluates `False`, then the statements in the `else` block are evaluated. In both cases, contorl then flows forwards to the next statement after the `if..else..` block.

<!-- #raw -->
# Mermaind.js code

graph TD
    A(Start) --> B[Move forwards]
    B --> C{Light == 255}
    C --> |Yes| D[Display reading]
    D --> C
    C --> |No| E[Drive forward<br/>a short way]
    E --> F{Light < 128?}
    F --> |Yes| G[Say 'black']
    F --> |No| H[Say 'grey']
    G --> I(End)
    H --> I
    
<!-- #endraw -->

## Activity: Stepping Through An `if..else...` Statement


In this activity we will look at another program to explore how `if...else..` works in more detail. 

Inspect the code in the following cell? If you run the code cell, what do you think will happen?


*Double click this cell to edit it and make your prediction here.*


Once you have made your prediction, run the following cell, and in the markdown cell beneath it, record what happened and how it compared to your prediction.

*You may find it informative to use `nbtutor` to step through each line of code in turn to see how the programme flow progresses. To do this, uncomment the `%%nbtutor` magic in the first line of the code cell by deleting the `#` at the start of the line before running the code cell.*

```python
#%%nbtutor --reset --force
x = 1

if x == 1:
    print("x equals 1")
else:
    print("x does not equal 1")
    
print("All done...")
```

*Double click this cell to edit it and record here what happened when you ran the code in the above cell. Did its behaviour match your prediction?*


What do you think will happen when you run the following code cell?

Run the cell and use *nbtutor* to step through the programme. How does the programme flow differ from the case where `x` had the value `1`? 

```python
%%nbtutor --reset --force
x = 2

if x == 1:
    print("x equals 1")
else:
    print("x does not equal 1")

print("All done...")
```

### Discussion

Click the arrow in the sidebar to reveal my observations.


In the cell where `x=1`, I predicted that the program would print the message *'x equals 1'* and then the messge *'All done...'*.

Viewing the trace, I could see how the programme started by initialising the `x` variable to the value `1`, then checked whether `x==1` (that is, whether `x` was equal to `1`); becuase it was, the programme then moved onto the `print("x equals 1")` statement and printed the first message, then programme flow continued to the first instruction after the `if...else...` block, which was the statement that printed the *'All done...'* message.

When I ran the programme with a value of `x` other then `1`, the control passed from the `if...` statement, where the conditional test evaluated as `False`, to the first line in the `else..` block, which printed the message *'x does not equal '*, before moving on to the first line after the `if..else..` block as before.


## An `if..` without an `else...`


It is sometimes useful to have just a single branch to the `if` statement. Python provides a simple `if...` statement for this purpose.

Run the following code cell as it stands, with the `x` variable taking the intial value `1` (`x=1`). Can you predict what will happen?

```python
#%%nbtutor --reset --force
x = 1

print("Are you ready?")

if x == 1:
    print("x equals 1")

print("All done...")
```

Try to predict what will happen if you change the initial value and run the cell again. Was your prediction correct?

Uncomment the *%%nbtutor* magic and run the code cell using different values of `x`, observing how the program flow progresses in each case.


### Discussion

*Click on the arrow in the sidebar to reveal my observations.*


With the initial value of the variable `x` set to `1` (`x = 1`) the program displayed the messages *Are you ready?*, *x equals 1* and *All done* as the `if ...` statement evaluated the `x == 1` test condition as `True` and passed control *into* the `if..` block.

When `x` was initialised to a different value, for example as `x = 2`, only the messages *Are you ready?* and *All done* were displayed as the `if..` conditional test failed and redirected control flow to the first statement *after* the `if..` block.


## 3.4 Activity: Combining loops and branching statements 


It is important to be clear that the condition in a branching statement (`if…then` or `if…then…else`) is checked only when execution reaches that part of the program. In the examples above, you stepped through the programs and saw that execution passed through the `if` statement only once. When creating useful robot programs, we often want conditions to be checked repeatedly. For example the robot may need to repeatedly check that it has not bumped into an obstacle, or whether it has found a bright or dark area. 

To do this, we can combine loops and branching statements in a program. 

Open the `Stay_inside` program; it is shown below. 


![figure ../tm129-19J-images/tm129_rob_p1_f027.jpg](../tm129-19J-images/tm129_rob_p1_f027.jpg)


Figure 3.6 Listing: Stay_inside


comment :  STAY_INSIDE

output left_motor on A

output right_motor on C

sensor light_sensor on 2 is light as percent

main

      comment :  set motors going forward

      forward [left_motor right_motor]

      on [left_motor right_motor]

      forever

            comment :  wait for light_sensor to 'see' black line

            if light_sensor &lt; 40

                  then

                        comment :  change direction and keep going

                        reverse [left_motor right_motor]

                        wait 100
<!--ITQ-->

#### Question

Can you predict what the robot will do when this program is run? 


#### Answer

Run the program to confirm your prediction. 
<!--ENDITQ-->
The robot will remain inside the black oval, reversing direction each time it encounters a black line. The program is constructed from an `if` statement inside a `forever` loop. The `if` statement checks the light sensor reading; when this is low (which it will be when the black line is reached) the motor direction is reversed. 

The `forever` loop is a loop that will run indefinitely. In this case it is useful because we want the robot to continue behaving in the same way. In other circumstances, we might want the loop to continue only while some condition holds true; in such cases a `while` statement is more useful. Note that the `while` statement includes its own conditional test. 


## 3.5 Challenge: Three shades of grey


The program `Branch` (in Section 3.1) showed how an `if…then…else` statement could be used to decide between black and grey areas. The background actually contains three different shades: black, dark grey, and light grey. Can you construct a program that will report which the robot encounters? 

Use the program `Branch` as a starting point. You will need to extend the code to decide between three alternatives.

To help make the program more readable, it already defines constants for the `send` command to speak the correct colours. These four constants are: `say_black`, `say_grey`, `say_light_grey` and `say_dark_grey`, with the values 25, 26, 27 and 28 respectively. Thus, for example, `send say_black` is the same as `send 25`. The robot sends the requisite code back to RobotLab, which triggers the corresponding audio file.
<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Note-->
Some programming languages have statements that let the programmer choose between more than two alternative branches. Branching statements in RobotLab are restricted to `if…then…else` and `if…then`, so combinations of `if…then…else` are needed to create more than two paths. 
</div><!--ITQ-->

#### Question

Would you like a hint? 


#### Answer

The current program has a condition (`light_sensor &lt; 30`) that determines if black is discovered. If the colour isn’t black, it is assumed to be grey. How could you decide whether the colour was light or dark grey? 
<!--ENDITQ--><!--ITQ-->

#### Question

Would you like another hint? 


#### Answer

You will need to combine `if…then…else` statements (try *nesting* them, that is, placing a second `if…then…else` statement in either the `then` or `else` branch of the first) to create three alternative paths. 
<!--ENDITQ--><!--ITQ-->

#### Question

Would you like an answer? 


#### Answer


```python

 if light_sensor &lt; 30 

 then 

 send say_black 

 else 

 if light sensor &lt; 60 

 then 

 send say_dark_grey 

 else 

 send say_light_grey 

```


Other solutions are possible. 
<!--ENDITQ--><div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Tip-->
When building programs containing `if…then…else` statements, you must be careful to drag new statements to the correct places. RobotLab will add comments ‘Add statements here…’ to act as targets for the `then` and `else` branches. If you want to add a statement to follow the whole `if…then…else` construct, you should drop the new statement over the `if` part. It may be easier to see what you are doing if you collapse the `if…then…else` statement by <div style="background:lightblue"><p>Keyboard: Cursor key Left/Right or use -/+/* on numeric keypad to collapse, expand, or expand all</p></div>clicking [-] by the `if` part; click on [+] to expand it again.
</div>

## 3.6 Activity: Robots that can speak


In Robot Lab Session 1 you looked at a program that could count up to 20. In this activity you are going to see how to make a program that can count up to 100.

The program you saw in Robot Lab Session 1 had a separate sound file for each of the numbers 1 to 20. The range of values that can be sent in messages is limited and only values between 0 and 127 are available for playing sound files. So if we used one hundred of these for numbers there would only be twenty-seven ‘slots’ left for other sounds, and this is not enough for our requirements.

Therefore, the difference between this program and the previous counting program is that there will not be a separate sound file for each message.
<!--ITQ-->

#### Question

What do you think is the minimum number of sound files needed to have a robot that counts to 100?


#### Answer

I hope you saw that the answer was less than 100! For numbers such as ‘thirty-two’ and ‘thirty-three’ we can combine pairs of files: ‘thirty’ with ‘two’ and with ‘three’. See below to find the exact number required.
<!--ENDITQ-->
It seems essential to have separate sound files for zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen and twenty. After this, we can start to double up: twenty and the numbers one to nine can be used in pairs to make twenty-one, twenty-two, …, twenty-nine. Similar considerations apply to thirty, forty, fifty, sixty, seventy, eighty and ninety. To finish off, we would also need the word ‘hundred’.

It turns out, then, that we need only 29 sound files to count from 0 to 100. The counting program uses the files listed in Table 3.1.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 3.1 RobotLab messages and corresponding sound files</caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan="">
 0 zero.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 15 fifteen.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 1 one.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 16 sixteen.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 2 two.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 17 seventeen.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 3 three.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 18 eighteen.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 4 four.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 19 nineteen.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 5 five.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 20 twenty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 6 six.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 30 thirty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 7 seven.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 40 forty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 8 eight.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 50 fifty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 9 nine.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 60 sixty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 10 ten.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 70 seventy.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 11 eleven.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 80 eighty.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 12 twelve.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 90 ninety.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 13 thirteen.wav
</td>
<td class="highlight_" rowspan="" colspan="">
 100 hundred.wav
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 14 fourteen.wav
</td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
</tbody>
</table>

A full listing of the sound message files in RobotLab is given in the Appendix (The RobotLab send codes). 

So, for example, `send 14` results in the program saying ‘fourteen’, while `send 90` followed by `send 6` results in the program saying ‘ninety-six’. 

When numbers are sent, RobotLab begins playing them and immediately moves on to the next line of the program. The program works much faster than the time it takes to speak, so if two numbers are sent consecutively, the second will overtake the first and will result in garbled or lost words. For this reason it is usually necessary to add a `wait` command after a `send` command. 

Run the program `I_can_count_to_100`. Have a look at the program code (Figure 3.7 below) and see if you can work out what is going on. 


![figure ../tm129-19J-images/tm129_rob_p3_f018.gif](../tm129-19J-images/tm129_rob_p3_f018.gif)


Figure 3.7 Listing: I_can_count_to_100


comment I_CAN_COUNT_TO_100

var N = 1

var N_divided_by_10 = 0

var large_part = 0

var small_part = 0

main

      wait 100

      while N &lt; 101

            comment Add statements here...

            if N &lt; 21

                  then

                        comment Add statements here...

                        send N

                        wait 80

                  else

                        comment Add statements here...

                        set N_divided_by_10 = N / 10

                        set large_part = (n_divided_by_10 * 10)

                        set small_part = N - large_part

                        send large_part

                        wait 80

                        wait 40

                        if small_part &gt; 0

                              then

                                    comment Add statements here...

                                    send small_part

                        wait 80

            set N = N + 1

      send 82

In this section you have seen how a robot can be made to ‘speak’ using different combinations of words. In principle, a robot could be given a very large vocabulary, and could say almost anything. Of course, this does not mean it understands what it says!

