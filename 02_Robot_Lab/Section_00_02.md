# 3 Branches


So far we have concentrated on sequential programs. A sequential program will always behave in the same way, but to be useful a robot program will often need to make decisions and behave differently in different circumstances. To do this, the program has to have alternative *branches*. Python provides an `if...then...else` statement to do just that, and you will see how it is used in the following activities. 


## 3.1 Activity: Detecting black and grey


Open the `Branch` program. Run the program several times with the robot moved to different starting positions. 


![figure ../tm129-19J-images/tm129_rob_p3_f010.small.png](../tm129-19J-images/tm129_rob_p3_f010.small.png)


Figure 3.1 The branch program


The program ‘Branch’ loaded into RobotLab. The Program Editor contains the listing below. The Simulator window shows the robot positioned beneath and facing two broad horizontal lines across the top. The first line is divided into three areas: from left to right, these are pale grey, black and mid grey. Above this is a second line which is all black.
<!--ITQ-->

#### Question

What does the robot do? 


#### Answer

The robot (Simon) moves forward over the white background until it reaches the grey or black area. If the background is black, Simon says ‘black’; otherwise, Simon says ‘grey’. 
<!--ENDITQ-->

![figure ../tm129-19J-images/tm129_rob_p3_f011.png](../tm129-19J-images/tm129_rob_p3_f011.png)


Figure 3.2 Flowchart for the branch program


The flowchart shows that the program branches to give two alternative paths of execution. In one of these, Simon will say ‘black’ and in the other Simon will say ‘grey’. To decide which branch is taken, a *condition* is checked; in this case the condition is whether the light sensor reading is less than 30. 

The flowchart (Figure 3.2) shows that the program branches to give two alternative paths of execution. In one of these, Simon will say ‘black’ and in the other Simon will say ‘grey’. To decide which branch is taken, a *condition* is checked; in this case the condition is whether the light sensor reading is less than 30. 


![figure ../tm129-19J-images/tm129_rob_p3_f012.png](../tm129-19J-images/tm129_rob_p3_f012.png)


Figure 3.3 Listing: Branch


comment : if-then-else branching program

output left_motor on A

output right_motor on C

sensor light_sensor on 2 is light as percent

const say_black = 25

const say_grey = 26

const say_light_grey = 27

const say_dark_grey = 28

main

      comment Add statements here...

      forward [left_motor right_motor]

      on [left_motor right_motor]

      while light_sensor &gt; 90

            comment (keep moving).

      if light_sensor &lt; 30

            then

                  comment Add statements here...

                  send say_black

            else

                  comment Add statements here...

                  send say_grey

      off [left_motor right_motor]

Turning to the code, you can see the `if…then…else` statement. It has two branches: one hanging from `then`, the other hanging from `else`. The condition (here `light_sensor &lt; 30`) is used to decide which branch to take. If the condition is *true* then the `then` branch is taken, the `send say_black` statement is executed and we hear ‘black’. Otherwise, (i.e. if the condition is *false*), the `else` branch is taken, the `send say_grey` statement is executed and we hear ‘grey’. 

Note that, whichever branch is taken, execution continues with the statement following the `if…then…else` statement. Here it is simply an `off` statement to ensure that the motors are turned off. It can sometimes be useful to hide the detail in the `if…then…else` statement so that you can see the overall shape of the program. <div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Cursor key Left/Right or use -/+/* on numeric keypad to collapse, expand, or expand all</p></div>Click on [-] besides `if` to hide the detail; click again on [+] to reveal the detail. 


## 3.2 Activity: A program with two branches


In this activity we will look at another program to explore how `if…then…else` works in more detail. 

Open the `Two_branches` program. The program is shown below. 


![figure ../tm129-19J-images/tm129_rob_p3_f013.png](../tm129-19J-images/tm129_rob_p3_f013.png)


Figure 3.4 Listing: Two_branches


comment : Program with two branches

output left_motor on A

output right_motor on C

var x = 1

main

    comment : begin the main program =========

    send x

    wait 100

    comment : the if-then-else statement follows ==

    if x = 1

        then

            comment :  x equals 1 is true

            forward [left_motor right_motor]

        else

            comment : x equals 1 is false

            backward [left_motor right_motor]

    comment :  the rest of the program ==========

    on [left_motor right_motor] for 200

    comment :  end of program ================
<!--ITQ-->

#### Question

Can you predict what the robot will do when this program is run? 

Run the program to confirm your prediction; then see my answer. 


#### Answer

This program will drive the robot a short distance. However, the direction in which it moves can be either forward or backward. The decision about direction is made by checking the value of a variable. If the variable is equal to 1 then the motors are set in the forward direction; otherwise, they are set in the backward direction. Then the motors are turned on for two seconds, making the robot move. A more detailed explanation is given below these questions.
<!--ENDITQ--><!--ITQ-->

#### Question

Which branch of the `if…then…else` statement is executed when the program is run? 


#### Answer

Single-step through the program to confirm your prediction. Click the single-step  ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f012.gif](../tm129-19J-images/tm129_rob_p4_f012.gif)  button in the toolbar, or use the `Run &gt; Step` menu or its shortcut.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: F6</p></div>
<!--ENDITQ--><!--ITQ-->

#### Question

Change the initial value of `x` to 0. Which branch will now be executed? How will the robot behave? 


#### Answer

You change the initial value of `x` by selecting that `var x = 1` statement, and then changing the initial value to 0. Single-step through the program to see which execution path is taken and how the robot behaves (see the description that follows). You may find it useful to open the `Variables` window to check the value of `x` just before the `if` statement is executed. 
<!--ENDITQ-->
This program will drive the robot a short distance. However, the direction in which it moves can be either forward or backward. The decision about direction is made by checking the value of a variable. If the variable is equal to 1, the motors are set in the forward direction; otherwise, they are set in the backward direction. Then the motors are turned on for two seconds, making the robot move.

In more detail, the program works as follows. The initial few statements configure the robot and also declare a variable `x` and set its initial value. The first few lines of the `main` part of the program use `send` to make RobotLab speak the current value of `x`. The `if…then…else` statement follows. If `x` is equal to 1, then the statements following `then` are executed and the motors are set to run forward. If the test `x = 1` is not true (that is, `x` has some value other than 1), the statements following `else` are executed and the motors are set to run backward. Finally, execution continues with the statements following the `if…then…else` construct and the motors are turned on for two seconds, driving the robot.


## 3.3 Activity: A program with an optional branch


It is sometimes useful to have just a single branch to the `if` statement. RobotLab provides an `if…then` statement for this purpose. Open the `One_branch` program; it is shown below. 


![figure ../tm129-19J-images/tm129_rob_p3_f014.png](../tm129-19J-images/tm129_rob_p3_f014.png)


Figure 3.5 Listing: One_branch


comment : Program with optional branch

output left_motor on A

output right_motor on C

var x = 1

main

    comment : begin the main program =========

    send x

    wait 100

    comment : the if-then statement follows ======

    if x = 1

        then

            forward [left_motor]

            backward [right_motor]

            on [left_motor right_motor] for 20

    comment :  the rest of the program ==========

    forward [left_motor right_motor]

    on [left_motor right_motor] for 200

    comment :  end of program ================
<!--ITQ-->

#### Question

Can you predict what the robot will do when this program is run? 


#### Answer

Run or single-step the program to confirm your prediction; then see my discussion below. 
<!--ENDITQ--><!--ITQ-->

#### Question

Change the initial value of `x`. How will the robot behave? 


#### Answer

Run or single-step the program to confirm your prediction. 
<!--ENDITQ-->
In this case the robot always drives forward for two seconds. However, if the variable `x` is equal to 1, the robot will spin by a small amount first and therefore head in a different direction. This extra step is the `then` branch of the `if` statement. It will be executed only if the condition `x = 1` is true; otherwise it will be skipped and execution will continue following the entire `if…then` statement. 


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

