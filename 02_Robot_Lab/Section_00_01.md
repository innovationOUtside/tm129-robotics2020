```python
# Run this cell to set up the robot simulator environment

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

# 1 Introduction to loops and branches

Loops and branches are powerful constructs in programming, and they are used extensively in almost all computer programs. In this lab session, I will introduce the different loop and branch statements provided by RoboLab. You will have an opportunity to see how they are used by working through the activities. We end the session with a number of challenges for you to attempt. These will give you practice in selecting and using different RobotLab statements.


# 2 Loops


## 2.1 An introduction to loops in computer programs


To illustrate the idea of a loop it is helpful to use a swimming analogy. Suppose you want to swim 20 lengths of a swimming pool. The chances are you will want to monitor your progress by keeping count of the number of lengths you complete. So, at the start, your personal counter (you) will be set to ‘0’. After one length of the pool you add 1 to your counter. You also ask yourself ‘have I done 20 lengths yet?’ If the answer is ‘no’, you ‘loop back’ to swim another length. On completion of the second length you add 1 to your counter and ask yourself the question again. If the answer is ‘no’ you loop back and repeat the process once more. You keep going like this until the answer to the question is ‘yes’, at which point you will have completed 20 lengths of the pool and the loop will end:


![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0QShTdGFydCkgLS0-IEJbU2V0IHRoZSBjb3VudCB0byAwXVxuXHRCIC0tPiBDW1N3aW0gYSBsZW5ndGhdXG5cdEMgLS0-IERbQWRkIDEgdG8gdGhlIGNvdW50XVxuICAgIEQgLS0-IEV7SXMgdGhlPGJyLz5jb3VudCBsZXNzPGJyLz50aGFuIDIwP31cbiAgICBFIC0tPiB8WWVzfCBDXG4gICAgRSAtLT4gfE5vfCBGKEVuZClcblx0XHRcdFx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- #raw -->
Mermaid code https://mermaid-js.github.io/mermaid-live-editor/
The mermaid editor is supposed to encode/decode base 64 strings
but I can't get my own encoder/decoder to work to encode/decode things the same way?

graph LR
    A(Start) --> B[Set the count to 0]
    B --> C[Swim a length]
    C --> D[Add 1 to the count]
    D --> E{Is the<br/>count less<br/>than 20?}
    E --> |Yes| C
    E --> |No| F(End)
    
Long description:

A flow chart for a person swimming 20 lengths of a pool. The flow chart starts with n oval shape labelled ‘Start’. From here there are sequences of boxes connected by arrows: first ‘set the count to zero’, then ‘swim a length’ and last ‘add 1 to the count’. From this box an arrow leads to a decision diamond labelled ‘is the count less than 20?’ Two arrows lead from this, one labelled ‘yes’, the other ‘no’. The ‘yes’ branch leads back to rejoin the box ‘swim a length’. The ‘no’ branch leads directly to an oval shape labelled ‘end’. There is thus a loop in the chart which includes the steps ‘swim a length’ and ‘add 1 to the count’ and ends with the decision ‘is the count less than 20?’
<!-- #endraw -->

As another example, consider a person ironing clothes. The loop starts with the person looking in the basket. Then a decision has to be made: are there any clothes left? If there are, the person must go round the loop: take out an item and iron it, put it on the pile of ironed clothes, and look in the basket again. When there are no clothes left in the basket the loop ends.


[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFN0YXJ0KSAtLT4gQntBbnkgY2xvdGhlczxicj5sZWZ0IGluPGJyLz5iYXNrZXQ_fVxuICAgIEIgLS0-IHxZZXN8IENbVGFrZSBvdXQ8YnIvPml0ZW0gYW5kPGJyLz5pcm9uXVxuICAgIEMgLS0-IERbUHV0IGl0IG9uIHBpbGU8YnIvPm9mIGlyb25lZDxici8-Y2xvdGhlc11cbiAgICBEIC0tPiBCXG4gICAgQiAtLT4gfE5vfCBFKEVuZCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFN0YXJ0KSAtLT4gQntBbnkgY2xvdGhlczxicj5sZWZ0IGluPGJyLz5iYXNrZXQ_fVxuICAgIEIgLS0-IHxZZXN8IENbVGFrZSBvdXQ8YnIvPml0ZW0gYW5kPGJyLz5pcm9uXVxuICAgIEMgLS0-IERbUHV0IGl0IG9uIHBpbGU8YnIvPm9mIGlyb25lZDxici8-Y2xvdGhlc11cbiAgICBEIC0tPiBCXG4gICAgQiAtLT4gfE5vfCBFKEVuZCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- #raw -->
Mermaid drawing (this is far from ideal...Maybe better to use draw.io?)

graph LR
    A(Start) --> B{Any clothes<br>left in<br/>basket?}
    B --> |Yes| C[Take out<br/>item and<br/>iron]
    C --> D[Put it on pile<br/>of ironed<br/>clothes]
    D --> B
    B --> |No| E(End)
    
Long desc:

A flow chart for a person ironing clothes. This starts with an oval ‘start’. An arrow leads to a decision diamond ‘any clothes left in the basket?’ Two arrows lead from this, one labelled ‘yes’, the other ‘no’. The ‘yes’ branch continues in turn to two boxes ‘take out item and iron it’ and ‘put it on the ironed pile of clothes’; an arrow leads back from this box to rejoin the decision ‘any clothes left in the basket?’ The ‘no’ branch leads directly to an oval ‘end’. There is thus a loop in the chart which begins with the decision ‘any clothes left in the basket?’ and includes the steps ‘take out item and iron it’ and ‘put it on the ironed pile of clothes’.
<!-- #endraw -->

<!-- #region -->
As you have seen, a sequential computer program is a sequence of lines of encoded commands, to be executed one after the other.

For example, the program to move a robot around a square course consisted of the following sequence of instructions repeated four times:

```python
# Draw side
tank_drive.on_for_seconds(SIDE_SPEED, SIDE_SPEED, SIDE_TIME)

# Turn ninety degrees
tank_turn.on_for_rotations(STEERING, TURN_SPEED, TURN_ROTATIONS)
```
<!-- #endregion -->

How much easier it would be just to give these commands once, and tell the computer to loop back to the start, repeating until the instructions have been executed four times?

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFN0YXJ0KSAtLT4gQltTZXQgY291bnRlciB0byAwXVxuICAgIEIgLS0-IENbIyBEcmF3IHNpZGU8YnIvPi4uLmNvZGUuLi5dXG4gICAgQyAtLT4gRFsjIFR1cm4gbmluZXR5IGRlZ3JlZXM8YnIvPi4uLmNvZGUuLi5dXG4gICAgRCAtLT4gRVtBZGQgMSB0byBjb3VudGVyXVxuICAgIEUgLS0-IEZ7SXMgdGhlIGNvdW50ZXIgPCA0fVxuICAgIEYgLS0-IHxZZXN8IENcbiAgICBGIC0tPiB8Tm98IEcoRW5kKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFN0YXJ0KSAtLT4gQltTZXQgY291bnRlciB0byAwXVxuICAgIEIgLS0-IENbIyBEcmF3IHNpZGU8YnIvPi4uLmNvZGUuLi5dXG4gICAgQyAtLT4gRFsjIFR1cm4gbmluZXR5IGRlZ3JlZXM8YnIvPi4uLmNvZGUuLi5dXG4gICAgRCAtLT4gRVtBZGQgMSB0byBjb3VudGVyXVxuICAgIEUgLS0-IEZ7SXMgdGhlIGNvdW50ZXIgPCA0fVxuICAgIEYgLS0-IHxZZXN8IENcbiAgICBGIC0tPiB8Tm98IEcoRW5kKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- #raw -->
graph TD
    A(Start) --> B[Set counter to 0]
    B --> C[# Draw side<br/>...code...]
    C --> D[# Turn ninety degrees<br/>...code...]
    D --> E[Add 1 to counter]
    E --> F{Is the counter < 4}
    F --> |Yes| C
    F --> |No| G(End)
    
Long desc:

A flow chart for a robot program with a loop. This starts with an oval ‘start’. An arrow leads first to a box ‘set a counter to 0’ and then to a sequence of further boxes: ‘# Draw side’ with an implication of the code associated with that, ‘# Turn ninety degrees’, agin with a hint regarding the presnce of code associated with that activity, and lastly ‘add 1 to the counter’. The arrow from this box leads to a decision diamond ‘is the counter < 4?’ Two arrows lead from this, one labelled ‘yes’, the other ‘no’. The ‘yes’ branch loops back to rejoin the sequence at ‘# Draw side code’. The ‘no’ branch leads directly to an oval ‘end’. There is thus a loop in the chart which includes the sequence of motor control commands, incrementing the counter and ends with the decision ‘is the counter &lt; 4?’.
<!-- #endraw -->

Python gives you two main ways of implementing loops:

- a `for...in...` loop;
- a `while ...` loop.

The `for...in...` loop checks the status of an *iterator*, which is capable of returning items from a list of values, one at a time. If the list is empty, the looping ends. If the iterator is not empty, the programme flow passes to the first instruction inside the `for...in...` code block, otherwise it passes to the next instruction at the same block (indentation) level as the `for...in...` statement.

The `while...` loop tests the truth value of a statement. If the statement evaulates as `True`, the programme flow passes into the body of the loop, otherwise it proceeds to the next statement at the same block (indentation) level as the `while...` statement. 

Let's see how each of these constructs works in turn, first using a simple, pure Python example, then in the context of our simulated robot.


## Using a `for...in...` loop

A `for...in...` loop takes each item from a list of items (or a more general Python *iterator* object), one at a time, then enters the loop, until the list (or iterator) is empty.

In "pseudo-code" (that is, a human readable set of instructions that look like a form of stylised code), the `for...in...` loop behaves as follows:

```
for each item in turn in a list of items, do the following sequence of instructions

  {
  
  instruction 1
  
  instruction 2
  
  instruction 3
  
  etc.
  }

```

Note that any of the instructions inside the loop may make use of the current value of the item  that has just been retrieved from the list.

When the loop has finished, the value of the last item retrieved from the list will continue to be available.

Run the following code cell to see how the `for...in...` loop retrieves one item at a time from a list of items (line 1), enters the code block within the loop starting at line 2, executes each line 2-3 in turn, then returns to line 1 to get the next item from the list.

When all the items have been retrieved from the list, the programme flow moves on to next item at the same indentation as the `for...in...` loop, which is to say line 4:

```python
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    print(' and ')

print('All done...')
```

It is also worth noting that the value of the `item` variable is the value of the last item to be retrieved from the list, as you can see if you display the value by running the following code cell:

```python
item
```

We can use the `nbtutor` extension to step thrhough the programme exectution to see what exactly is going on.

Run the following code cell to load in the `nbtutor` magic:

```python
%load_ext nbtutor
```

<!-- #region -->
The `%%nbtutor` cell block magic can be used to prefix Python code (but *not* code intended for the simulator) we want to step through.


__TO DO: the `nbtutor` display is low contrast and perhaps inaccessible. I started a [related issue](https://github.com/lgpage/nbtutor/issues/37) but this needs addressing somewhere.__

One thing to note about the notebook environment is that if we have already created any Python variables in the current notebook, they will be displayed by default in the `%%nbtutor` visualisation.

We can limit the variables that are displayed by `nbtutor` by calling the magic using the command `%%nbtutor --reset --force`.

Run the following code cell to invoke the `nbtutor` widget, and then use the `Next` button in the *cell toolbar* that is created to step through each line of code in turn.

Observe the progress of the control flow through the code via the two differently coloured arrows that show the next line to be executed (red line) and the previous line to be executed (green arrow). Also notice how the statement previously executed may update the value of `item` variable as a consequence of its execution.
<!-- #endregion -->

```python
%%nbtutor --reset --force
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    print(' and ')

print('All done...')
```

Did you notice how the program flow repeatedly went from the last line of the code inside the `for..in..` block back up to the `for..in..` statement, before going from the `for..in..` statement to the final `print('All done..')` statement when the loop had iterated through all the items in the list?

Close the `nbtutor` cell toolbar view by clicking on the notebook toolbar `View` menu option, selecting `Cell Toolbar` and then `None`.


### Activity

See if you can write a simple programme that loops through a list of days of the week, print out a message of the form 'day 1 is Monday' followed by "day 2 is Tuesday', and so on.

*Hint: Python f-strings ("formatted strings" or "formatted string literals") provide a convenient way of getting the value of a variable into a string. For example, if you have a variable `day_of_week = "Monday"`, we can display a message using the construction `print(f"Today is {day_of_week}")`. The `f"..."` construction denotes the f-string. The curly brace brackets (`{..}`) contain the name of a variable whose value you want to substitute into the string. Note that f-strings are not available in the simulator's Python implementation.*

```python
# YOUR CODE HERE
```

#### Answer

*Click on the arrow in the sidebar to reveal my answer*


First I created a counter value, then I created a list containing the days of the week. Using a `for..in..` loop, I iterated through the list. Inside the loop, I incremented a counter, then displayed the required message.

```python
counter = 0

for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    
    counter += 1
    print(f"Day {counter} is {day}")
```

### Using a `for..in..` Loop in a Robot Control Program

Loops are very useful when it comes to executing repetitive tasks.

You may remember from the programme we use to draw a square that there was a lot of repeated code, with the same code used to draw a single side and then turn through a right angle repeated four times each. At the time, you may have tought "there must be a better way than this?" and the use of a loop provides just such a better way.

Look through the code in the code cell below and predict what you think the robot will do when it runs that programme.


*DOUBLE CLICK this cell to edit it and enter your prediction of what the robot will do as it runs through the programme.*

```python
%%sim_magic_preloaded roboSim

# Draw something...
for count in range(3):

    #Go straight
    # Set the left and right motors in a forward direction
    # and run for 1 rotation
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)

    #Turn
    # Set the robot to turn on the spot
    # and run for a certain number of rotations *of the wheels*
    tank_turn.on_for_rotations(-100, SpeedPercent(75), 0.846)

```

Now run the code cell to download the programme to the robot. With the pen trace enabled, run the programme in the simulator and observe what happens. Was your predcition correct?

Modify the programme (if necessary...) so that the robot will trace out something close to a square (don't spend too much time trying to make it perfect: that may not be possible!). Clear the trace in the simulator, reset the robot location, and download and run the programme again to check your programme modification worked.


### Returning to the top of a loop early

Sometimes we may want to to return to the top of a loop from within a loop code block *before* we have executed all the lines in the looped block. We can do this using the `continue` instruction.

Run the following code cell and step through each line of code a line at a time using the `nbtutor` *Next* button. Watch the programme flow particularly closely when the `item` variable takes the value `three`.

```python
%%nbtutor --reset --force
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    if item=='three':
        continue
    print(' and ')

print('All done...')
```

<!-- #region -->
### Conditional Tests Using the Branch Construct, `if`...

In the previous programme, you may have noticed another new statement, an `if` statement. This is another sort of conditional statement, often referred to as a *branch*. The `if` statement will test a logical condition and if it evaluates as `True` programme flow will pass to any statements contained within the `if` statement block.

```python
if LOGICAL_TEST_STATEMENT:
    #if the LOGICAL_TEST_STATEMENT evaluates as True
    # run the following command
    print('The statement was True...')
    
print("This will always be printed...")
```


In and of itself, the `if` statement is tested once and once only. *If* the conditional test pass, control flows into the body of the *if* statement and then on to the next statement after the *if* construct. If the conditional test evaluates as false, control passes immediately to the next statement *after* the if block.

In the `if` statement, the `==` sign is used to test whether the value of the thing on the left is the same as the value of the thing on the right.

So the following is `True`:
<!-- #endregion -->

```python
1 == 1
```

because numeric `1` does indeed equal numeric `1`; but the following evaluates as `False` because numeric `1` *does not* equal the string `one`:

```python
1 == 'one'
```

The following is also `False` because the *numeric* value `1` is *not* the same as the *string* value `'1'`:

```python
1 == '1'
```

However, the following string values *are* equivalent even though we used different string delimiters (single quotes in the first case, double quotes in the second) to create them:

```python
'1' == "1"
```

Try experimenting with you own equivalent, or unequivalent, statements in the code cell below.

*Feel free to create more code cells if you want to keep a record of things you have tried. Or comment out each line after you have tried it if you want to try mutliple statements in the same code cell.*

```python
# TRY SOME EQUIVALENT AND UNEQUIVALENT STATEMENTS OF YOUR OWN HERE


```

### Activity

Suppose Wednesday is early closing day. Building on elements from your earlier programme that displays the days of the week, modify the programme to use a `continue` statement so that it prints out the message *I could go shopping on DAY afternoon* for every day except Wednesday.

```python
# YOUR ANSWER HERE
```

#### Answer
*Click on the arrow in the sidebar to reveal my answer.*


I used a simple `if` statement to check if it was Wednesday, and if it was, the `continue` statement passed the programme control flow back to the top of the loop *before* the programme had a chance to print out that day of the week. 

```python
for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    
    if day=='Wednesday':
        continue
    print(f"I could go shopping on {day} afternoon.")
```

### Escaping from a Loop Early

As well as returning back to the top of a loop early using a `continue` statement, we may sometimes want to escape from a loop altogether before the loop would normally finish. We can achieve this using the `break` statement, which breaks the control flow oout of a loop when it is encountered.

Run the following code cell, stepping through it a line at a time, again paying particulalry close attention when the `item` variable has the value `three`:

```python
%%nbtutor
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    if item=='three':
        break
    print(' and ')

print('All done...')
```

### Activity  - Escape from a `for...in...` loop

Suppose we get weekends off. Using a `break` construct inside a `for..in...` loop, create a simple programme that takes a list containing the days of the week in order *Monday*...*Sunday* and displays the message *DAY is a workday...* for days Monday to Friday, but then breaks out of the loop when it realises it is Friday.

```python
# YOUR CODE HERE
```

#### Answer
*Click on the arrow in the sidebar to reveal my answer.*


In this case, I display the print message before I break out of the loop using the `break` statement:

```python
for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    print(f"{day} is a workday.")
    if day=='Friday':
        break
```

## Using a `while...` loop

A `while...` loop tests the truth of a statement on each iteration of the loop. In "pseudo code", the bevaiour can be described as:

```

do the following sequence of instructions while a condition holds 

 { 

 instruction 1 

 instruction 2 

 instruction 3 

 instruction 4 

 instruction 5 

 etc 

 } 
 ```

In some respects the `while` resembles an `if` statement in that if (while) the tested condition is true, control passes into the body of the while statment block, and if it evaluates false, control passes immediately to the next statement after the while block. However, *unlike* the `if` statement, when all the statements inside the `while` block have been executed, in sequential order, control does not then flow to the next statement after the while block, it passes back to the top of the while loop and the condition is re-evaluated.

In this way, the programme can keep repeating the lines of code inside the while block until some condition is met, or some condition fails.

Note that if the conditionally tested value changes to a value that would cause the condition to evaluate as false whilst the programme flow is inside the while block, the statements insde the while block will continue to execute in sequential order. Control only passes from the while statement to the statement after the while block at the point when  control passes to the while statement and its condition is tested and found to evaluate as false.

Let's see an example of how to use a `while` loop to help us keep track of whether we have counted up to a particular number yet as you will see if you run the programme in the following code cell:

```python
#%%nbtutor --reset --force
counter = 1

while counter < 5:
    print(counter)
    counter = counter + 1
    
#Display the final value of counter
counter
```

Uncomment the `%%nbtutor`cell magic  by deleting the `#` symbol at the start of the first line and run the previous cell again to step through the code as it executes a line at a time.

Observe how the program flow repeatedly moves from the last line of the code inside the `while` block back up to the `while` statement, before going from the `while` statement to the final `counter` statement when the conditional tests eventually evaluate as false.



### Activity - Use a `while` Loop

The Python `random` functon from the `random` package is capabale of generating a random number between 0 and 1, as you will see if you run the following cell repeatedly. (The package is only imported once despite multiple calls to it.)

```python
import random

random.random()
```

We can think of this as a coin toss, where we toss "heads" for values greater than or equal to 0.5, or tails for a random value between 0 and 1 that is less than 0.5.

Write a simple while loop that tests a simulated coin toss for as long as it tosses the equivalent of "heads", printing "heads" for each successful toss.

Run the code cell several times to see what happens.

```python
# Add your code here
```

#### Answer
*Click on the arrow in the sidebar to reveal my answer.*


To test the coin toss, we are looking for a random value of greater than or equal to 0.5, which is to say, a value of `random.random() >= 0.5`.

We can use this as a conditional test in a `while` loop. In the body of the loop, we print "heads" to show we are in the loop.

```python
while random.random() >= 0.5:
    print("heads")
```

Running the cell multiple times, sometimes nothing is printed (if the "coin" flips as "tails", that is, the first random value is *less than* 0.5); at other times, we may get one or more "heads" displayed. (The most I saw in several attempts was eight heads in a row!)


### Infinite Loops

We can create a special sort loop known as an *infinite loop* using the `while True:` construction, where the statement `True` *always* evaluates as `True` and so the loop repeats until the program is forced to stop or the flow is forced out of the loop and onto the next instruction using a `break` statement.

The following code cell demonstrates how to escape an otherwise infinite loop by using a `break` statement. Run the cell to see how it works. (Uncomment the `nbtutor` magic to step through it a line at a time as it executes.

```python
#%%nbtutor --reset --force
counter = 0

while True:
    counter = counter + 1
    print(counter)
    if counter == 5:
        break
        
print(f"We escaped at counter=={counter}")
```

### Using a `while` loop in the simulator

Being able to loop *whilst* a particular condition is holds allows us to perform actions *until* that condition no londer holds.

This may be particularly useful in a robot programming context, as the following simple example demonstrates.

In the simulator, load in the *Grey bands* background and reset the trace. (You can also disable the *pen down* control: we don't need to keep track of where the robot has travelled for this activity.)

Run the following code cell to download the programme to the simulator and then run it in the simulator, observing the behaviour of the robot.

```python
%%sim_magic_preloaded roboSim
from ev3dev2.sensor import INPUT_2

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

colorLeft = ColorSensor(INPUT_2)

sensor_value = colorLeft.reflected_light_intensity

while sensor_value > 250:
    print(sensor_value)
    sensor_value = colorLeft.reflected_light_intensity

print("I now see {}".format( colorLeft.reflected_light_intensity))
tank_drive.off()
```

When you run the programme in the simulator, the robot should drive forwards until it encounters the first, light grey line, and then it should stop.

*Although the robot will stop, by default, when the programme ends, becuase the simulator run stops at the end of the programme, it is often good practice to explicitly turn the motors off yourself. By doing this,  you know for sure what state the motors are in at the end of the programme. In the above example, what would happen if, for some reason, the motor off command was omitted and the simulator carried on running even as the programme execution had completed?*

The programme works by checking the value from one of the robot's sensors, a downward facing light sensor, which you will meet in more detail in a later notebook. The sensor returns a "reflected light" sensor, which relates to the colour of the background canvas over which the robot is travelling. The simulator output display window shows the sensor value, starting at `255` when the robot is on the plain white background. This value is above the conditionally tested threshold value of `250` used in the original programme's `while` statement, and so the programme continues looping round the while loop. When the robot encounters the first grey line, the sensor returns a lower value of 240 when I ran the programme.

*Rather than testing and reporting the `colorLeft.reflected_light_intensity` value directly, the programme is constructed as it is because the sensor value may change in going from the `while` programme step to the `print()` step. Even though computers may step between lines of code very quickly, they still take a finite time to do so.*

Try modifying the numerical value used in the `while` conditional test and downloading and running the modified programme. Can you get the robot to stop as soomn as it encounters the second medium grey band? On the third, dark grey line? On the final, black line?


## Activity: Changing a loop variable count up to 10


As well as programming the siunulated robot to respond to a sensor value, we can also get it to count aloud.

The following programme, for example, when downloaded to the simulator, will cause the robot (?!) to count aloud.

Can you get the robot to count to 10, rather than 5?

```python
%%sim_magic roboSim

#Counting robot...
import playsound

count = 1

while count < 5:
    # The playsound.say() function expects a string...
    playsound.say(str(count))
    count = count + 1
```

<!-- #region -->
## Summary

In this notebook, you have seen how we can control the way in which programme statements are executed in a programme by using various programme flow control constructs and how we can use the `nbtutor` extension to step through and monitor the flow of simple Python programmes executing in the notebook's Python environment (unfortunately, it does not allow us to step through code we download into the simulator).


Regarding the programme control flow, you have seen how:

- the `for..in..` loop allows a the programme to work through a set of statements in the loop body once for each item in a list of values or "iterator" construct;
- the `if...` branch command checks a logical condition once and once only; if the tested condition evaluates true, control passes inside the block, and then continues after the if block. If the condition evaluates as false, control passes immediately to the statement after the if block;
- the `while...` loop allows us to repeatedly test a condition, and if it is found to be true, pass control to a sequnece of instructions inside the while block. Once those instructions have been executed, control is passed back the top of the while loop and the test condition is evaluated again. If the while condition evaluates as false, control passes to the first statement after the while block.

Control flow in `for` and `while` loops can also be interrupted using `continue` and `break` statements.

- `continue` prematurely forces the flow of control back to the top of the loop, rather than requiring all the instructions in the loop to execute and then passing control back to the top of the loop;
- `break` prematurely forces the flow of control out of the loop to the next statement after the loop block, rather than requiring control to be passed following the failure of the conditional test at the top of the loop.

Control flow instructions are part of the core Python language and are used in a similar way inside in the simulator and the "native" notebook Python environment.
<!-- #endregion -->

## Addendum

The robot simulator speech action is built up from a Javascript function that builds on a built-in browser function for creating speech utterances. We can force the Jupyter notebook to run Javascript code in the browser from a code cell using the `%%javascript` cell magic. This means we can get the browser to "speak" by callng the browser speech functions via Javascript directly.

*Note that there may be a brief delay between running the code cell and hearing the speech utterance.*

```javascript
speechSynthesis.speak(new SpeechSynthesisUtterance("hello"))
```

We can also use the Python `pyttxsx` package to create speech utterances, which we can call directly from a notebook code cell if we create a building block around it:

```python
import pyttsx3

class Speech():
    def __init__(self):
        self.engine = pyttsx3.init()
    def say(self, txt):
        if isinstance(txt, int) or isinstance(txt, float):
            txt = str(txt)
        self.engine.say(txt)
        self.engine.runAndWait()
        
```

As before, there may be a brief delay between running the code cell and hearing the speech utterance.

Run the following code cell to hear Python speak to you:

```python
speaker = Speech()
speaker.say('hello')
speaker.say(1)
speaker.say("2.5")
speaker.say(2.5)
speaker.say('goodbye')
```

We can also create a simple Python programm to count aloud up to 10, for example by using a `while` loop:

```python
n = 1

while n <= 10:
    speaker.say(n)
    n = n + 1
```
