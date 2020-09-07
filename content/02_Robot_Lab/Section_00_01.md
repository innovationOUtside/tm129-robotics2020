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

<!-- #region -->
# Introduction to loops and branches

Loops and branches are powerful constructs in programming, and they are used extensively in almost all computer programs. In this session, I will introduce the different loop and branch statements provided by RoboLab. You will have an opportunity to see how they are used by working through the activities. We end the session with a number of challenges for you to attempt. These will give you practice in selecting and using different RobotLab statements.


In particular, this notebook will focus on *loops* and the next notebook on *branches*. Two further notebooks will provide you with a series of challenges to help develop your understanding of how these sorts of construction can be used in the context of some simple robot programming tasks.
<!-- #endregion -->

# 1 Loops


## 1.1 An introduction to loops in computer programs


To illustrate the idea of a loop it is helpful to use a swimming analogy. Suppose you want to swim 20 lengths of a swimming pool. The chances are you will want to monitor your progress by keeping count of the number of lengths you complete. So, at the start, your personal counter (you) will be set to ‘0’. After one length of the pool you add 1 to your counter. You also ask yourself ‘have I done 20 lengths yet?’ If the answer is ‘no’, then you ‘loop back’ to swim another length. On completion of the second length you add 1 to your counter and ask yourself the question again. If the answer is ‘no’, then you loop back and repeat the process once more. You keep going like this until the answer to the question is ‘yes’, at which point you will have completed 20 lengths of the pool and the loop will end:

```python
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget
```

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Set the count to 0
op2=>operation: Swim a length
op3=>operation: Add 1 to the count
cond=>condition: Is the count less than 20?
st(right)->op1(right)->op2(right)->op3(right)->cond
cond(yes,right)->op2
cond(no)->e
```
<!-- #region tags=["alert-warning"] -->
*An [issue](https://github.com/adrai/flowchart.js/issues/186) has been filed regarding the misaligned return path in the flow diagram.*
<!-- #endregion -->


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

A flow chart for a person swimming 20 lengths of a pool. The flow chart starts with an oval shape labelled ‘Start’. From here there are sequences of boxes connected by arrows: first ‘Set the count to 0’, then ‘Swim a length’ and last ‘Add 1 to the count’. From this box an arrow leads to a decision diamond labelled ‘Is the count less than 20?’ Two arrows lead from this: one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch leads back to rejoin the box ‘Swim a length’. The ‘No’ branch leads directly to an oval shape labelled ‘End’. There is thus a loop in the chart which includes the steps ‘Swim a length’ and ‘Add 1 to the count’ and ends with the decision ‘Is the count less than 20?’
<!-- #endraw -->

<font color='red'>JD: which flowchart are we using? Note that in the figure description, it mentions that 'Start' and 'End' are in OVAL shapes, but this is not true in the Mermaid code, which uses ROUNDED RECTANGLES instead. However, the Mermaid flow charts look better than the other flow charts. I've updated the raw code for some of the Mermaid flow charts (e.g. to make the text consistent with the preceeding text and/or the description). Presumably this will need to be remade somehow?</font>

As another example, consider a person ironing clothes. The loop starts with the person looking in the basket. Then a decision has to be made: are there any clothes left? If there are, the person must go round the loop: take out an item and iron it, put it on the pile of ironed clothes, and look in the basket again. When there are no clothes left in the basket the loop ends.

```python
%%flowchart_magic
st=>start: Start
e=>end: End
cond=>condition: Any clothes left in basket?
op2=>operation: Take out item and iron
op3=>operation: Put it on pile of ironed clothes
st(right)->cond
cond(yes, right)->op2
op2(right)->op3(top)->cond
cond(no, bottom)->e
```

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFN0YXJ0KSAtLT4gQntBbnkgY2xvdGhlczxicj5sZWZ0IGluPGJyLz5iYXNrZXQ_fVxuICAgIEIgLS0-IHxZZXN8IENbVGFrZSBvdXQ8YnIvPml0ZW0gYW5kPGJyLz5pcm9uXVxuICAgIEMgLS0-IERbUHV0IGl0IG9uIHBpbGU8YnIvPm9mIGlyb25lZDxici8-Y2xvdGhlc11cbiAgICBEIC0tPiBCXG4gICAgQiAtLT4gfE5vfCBFKEVuZCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFN0YXJ0KSAtLT4gQntBbnkgY2xvdGhlczxicj5sZWZ0IGluPGJyLz5iYXNrZXQ_fVxuICAgIEIgLS0-IHxZZXN8IENbVGFrZSBvdXQ8YnIvPml0ZW0gYW5kPGJyLz5pcm9uXVxuICAgIEMgLS0-IERbUHV0IGl0IG9uIHBpbGU8YnIvPm9mIGlyb25lZDxici8-Y2xvdGhlc11cbiAgICBEIC0tPiBCXG4gICAgQiAtLT4gfE5vfCBFKEVuZCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- #raw -->
Mermaid drawing (this is far from ideal...Maybe better to use draw.io?)<font color='red'>JD: To be resolved.</font>

graph LR
    A(Start) --> B{Any clothes<br>left in<br/>basket?}
    B --> |Yes| C[Take out<br/>item and<br/>iron]
    C --> D[Put it on pile<br/>of ironed<br/>clothes]
    D --> B
    B --> |No| E(End)
    
Long description:

A flow chart for a person ironing clothes. This starts with an oval ‘Start’. An arrow leads to a decision diamond ‘Any clothes left in basket?’ Two arrows lead from this: one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch continues in turn to two boxes ‘Take out item and iron’ and ‘Put it on pile of ironed clothes’; an arrow leads back from this box to rejoin the decision ‘Any clothes left in basket?’ The ‘No’ branch leads directly to an oval ‘End’. There is thus a loop in the chart which begins with the decision ‘Any clothes left in basket?’ and includes the steps ‘Take out item and iron’ and ‘Put it on pile of ironed clothes’.
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

How much easier would it be just to give these commands once, and tell the computer to loop back to the start, repeating until the instructions have been executed four times?

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Set counter to 0
op2=>operation: Draw side code
op3=>operation: Turn ninety degrees code
op4=>operation: Add 1 to counter
cond=>condition: Is counter < 4?
st(right)->op1(right)->op2->op3->cond
cond(yes, right)->op2
cond(no, bottom)->e
```

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFN0YXJ0KSAtLT4gQltTZXQgY291bnRlciB0byAwXVxuICAgIEIgLS0-IENbIyBEcmF3IHNpZGU8YnIvPi4uLmNvZGUuLi5dXG4gICAgQyAtLT4gRFsjIFR1cm4gbmluZXR5IGRlZ3JlZXM8YnIvPi4uLmNvZGUuLi5dXG4gICAgRCAtLT4gRVtBZGQgMSB0byBjb3VudGVyXVxuICAgIEUgLS0-IEZ7SXMgdGhlIGNvdW50ZXIgPCA0fVxuICAgIEYgLS0-IHxZZXN8IENcbiAgICBGIC0tPiB8Tm98IEcoRW5kKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFN0YXJ0KSAtLT4gQltTZXQgY291bnRlciB0byAwXVxuICAgIEIgLS0-IENbIyBEcmF3IHNpZGU8YnIvPi4uLmNvZGUuLi5dXG4gICAgQyAtLT4gRFsjIFR1cm4gbmluZXR5IGRlZ3JlZXM8YnIvPi4uLmNvZGUuLi5dXG4gICAgRCAtLT4gRVtBZGQgMSB0byBjb3VudGVyXVxuICAgIEUgLS0-IEZ7SXMgdGhlIGNvdW50ZXIgPCA0fVxuICAgIEYgLS0-IHxZZXN8IENcbiAgICBGIC0tPiB8Tm98IEcoRW5kKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- #raw -->
graph TD
    A(Start) --> B[Set counter to 0]
    B --> C[# Draw side<br/>...code...]
    C --> D[# Turn ninety degrees<br/>...code...]
    D --> E[Add 1 to counter]
    E --> F{Is counter < 4?}
    F --> |Yes| C
    F --> |No| G(End)
    
Long description:

A flow chart for a robot program with a loop. This starts with an oval ‘Start’. An arrow leads first to a box ‘Set counter to 0’ and then to a sequence of further boxes: ‘# Draw side’ with an implication of the code associated with that, ‘# Turn ninety degrees’, again with a hint regarding the presnce of code associated with that activity, and lastly ‘Add 1 to counter’. The arrow from this box leads to a decision diamond ‘Is counter < 4?’ Two arrows lead from this, one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch loops back to rejoin the sequence at ‘# Draw side code’. The ‘No’ branch leads directly to an oval ‘End’. There is thus a loop in the chart which includes the sequence of motor control commands, incrementing the counter and ends with the decision ‘Is counter < 4?’.
<!-- #endraw -->

Python gives you two main ways of implementing loops:

- a `for...in...` loop
- a `while...` loop.

The `for...in...` loop checks the status of an *iterator*, which is capable of returning items from a list of values, one at a time. If the list is empty, then the looping ends. If the iterator is not empty, then the program flow passes to the first instruction inside the `for...in...` code block; otherwise it passes to the next instruction at the same block (indentation) level as the `for...in...` statement.

The `while...` loop tests the truth value of a statement. If the statement evaulates as `True`, then the program flow passes into the body of the loop; otherwise it proceeds to the next statement at the same block (indentation) level as the `while...` statement. 

Let’s see how each of these constructs works in turn, first using a simple, pure Python example, then in the context of our simulated robot.


## 1.2 Using a `for...in...` loop

A `for...in...` loop takes each item from a list of items (or a more general Python *iterator* object), one at a time, then enters the loop, until the list (or iterator) is empty.

In ‘pseudo-code’ (that is, a human-readable set of instructions that look like a form of stylised code), the `for...in...` loop behaves as follows:

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

Run the following code cell to see how the `for...in...` loop retrieves one item at a time from a list of items (line&nbsp;1), enters the code block within the loop starting at line&nbsp;2, executes each line&nbsp;2–3 in turn, then returns to line&nbsp;1 to get the next item from the list.

When all the items have been retrieved from the list, the program flow moves on to the next item at the same indentation as the `for...in...` loop, which is line&nbsp;4:

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

We can use the `nbtutor` extension to step thrhough the program exectution to see what exactly is going on.

Run the following code cell to load in the `nbtutor` magic:

```python
%reload_ext nbtutor
```
The `%%nbtutor` cell block magic can be used to prefix Python code we want to step through, but *not* code intended for the simulator.

One thing to note about the notebook environment is that if we have already created any Python variables in the current notebook, then they will be displayed by default in the `%%nbtutor` visualisation.

We can limit the variables that are displayed by `nbtutor` by calling the magic using the command `%%nbtutor --reset --force`.

Run the following code cell to invoke the `nbtutor` widget, and then use the *Next*&nbsp;> button in the *cell toolbar* that is created to step through each line of code in turn.

Observe the progress of the control flow through the code via the two differently coloured arrows that show the next line to be executed (red line) and the previously executed line (green arrow). Also notice how the statement previously executed may update the value of the `item` variable as a consequence of its execution.

```python
%%nbtutor --reset --force
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    print(' and ')

print('All done...')
```

Did you notice how the program flow repeatedly went from the last line of the code inside the `for...in...` block back up to the `for...in...` statement, before going from the `for...in...` statement to the final `print('All done...')` statement when the loop had iterated through all the items in the list?

Close the `nbtutor` cell toolbar view by clicking on the notebook toolbar *View* menu option, selecting *Cell Toolbar* and then *None*.


## Using `print()` and `display()` statements to help debug a program

As well as using the `nbtutor` to keep help us see what's going on in the loop as it executes *within the notebook*, we can also using `print()` and `display()` statements to display the value of one or more variables as the loop executes. 

Python *f-strings* ("formatted strings" or "formatted string literals") also provide a convenient way of getting the value of a variable into a string. For example, if you have a variable `day_of_week = "Monday"`, we can display a message using the construction `print(f"Today is {day_of_week}")`. The `f"..."` construction denotes the f-string. The curly brace brackets (`{..}`) contain the name of a variable whose value you want to substitute into the string.

<!-- #region tags=["alert-danger"] -->
Note that *f-strings* and the use of the `display()` function are not available in the simulator's Python implementation. In such cases, you can print several variables and strings at once by using commas in the print statement (e.g. `print('Today is', day_of_week)`*
<!-- #endregion -->

<!-- #region activity=true -->
### Activity

See if you can write a simple program that loops through a list of days of the week and prints out a message of the form ‘day 1 is Monday’ followed by ‘day 2 is Tuesday’, and so on.
<!-- #endregion -->

```python activity=true
# YOUR CODE HERE
```

<!-- #region activity=true heading_collapsed=true -->
#### Answer

*Click on the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
There are several ways in which we could implement the code to perform this task.

For example, in the following worked example, I created a counter value (`counter = 0`) and then used a `for...in...` loop to iterate through a list containing the names of the days of the week.

The code to be executed by the loop was "nested" inside it as a code block by indenting the code I wanted to execute within the loop.

Inside the loop, I incremented a counter (`counter = counter + 1`), then displayed the required message using a simple `print()` statement:
<!-- #endregion -->

```python hidden=true
counter = 0

for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    
    counter = counter + 1
    
    print("Day", counter, "is", day)
```

<!-- #region activity=true hidden=true -->
The following code example performs the same task, but implemented in a lightly different way.

In particular, I first declare a variable (`days_of_week`) to refer to the list of the days of the week, and then iterate over the list *as referred to by the variable* in the loop.

Within the loop, I use a shorthand construction `counter += 1` that essentially says: *update the value of the `counter` variable to its current vale, plus 1*.

Finally, I have used a Pyhton *f-string* to print the message on each iteration through the loop:
<!-- #endregion -->

```python activity=true hidden=true
counter = 0

days_of_week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_week:
    
    counter += 1
    
    print(f"Day {counter} is {day}")
```
<!-- #region tags=["alert-danger"] -->
### Using loops in code intended to be downloaded and run in the simulator

If you use a loop in code you want to download to the simulator, then you need to put something in the loop that ‘uses up’ simulator time and allows its internal clock to proceed; otherwise you may find that your simulator Python program gets stuck and ‘hangs’ your web browser.

Turning motors on for a specified time or rotation count, or polling sensors, is one way to do this. Another way is to add an excplcit delay into the loop. For example, if you add the line `from time import sleep` to the start of your simulator program, then you can add a step `sleep(0.01)` to pause in the loop for one hundredth of a second. This gives the simulator a chance to model the progress of time in the simulated world, rather than getting stuck in very rapidly iterating loop in the code it’s trying to execute.
<!-- #endregion -->

### Using a `for...in...` loop in a robot control program

Loops are very useful when it comes to executing repetitive tasks. In this section, you will see how we can use a loop in a simple robot control program.

But first, we need to ensure we have loaded in the simulator Python package and enabled the simulator magic:

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

You may remember from the program we used to draw a square that there was a lot of repeated code, with the same code used to draw a single side and then turn through a right angle repeated four times each. At the time, you may have thought ‘there must be a better way than this?’. The use of a loop provides just such a better way.

Look through the code in the code cell below and predict what you think the robot will do when it runs that program.

*The magic used to configure the simulator specifies the robot location (`-x`/`-y`), orientation angle (`-a`), pen down mode (`-p`) and cleared trace (`-C`).*

<!-- #region student=true -->
*Double-click this cell to edit it and enter your prediction of what the robot will do as it runs through the program.*
<!-- #endregion -->

```python
%%sim_magic_preloaded -x 1000 -y 500 -a 0 -p -C 

# Draw something...
for count in range(3):

    #Go straight
    # Set the left and right motors in a forward direction
    # and run for 1 rotation
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)

    #Turn
    # Set the robot to turn on the spot
    # and run for a certain number of rotations *of the wheels*
    tank_turn.on_for_rotations(-100, SpeedPercent(75), 1.62)

```

Now run the code cell to download the program to the robot. With the pen trace enabled, run the program in the simulator and observe what happens. Was your prediction correct?

Modify the program (if necessary...) so that the robot will trace out something close to a square (don’t spend too much time trying to make it perfect: that may not be possible!). Clear the trace in the simulator, reset the robot location, and download and run the program again to check your program modification worked.


### Returning to the top of a loop early

Sometimes we may want to to return to the top of a loop from within a loop code block *before* we have executed all the lines in the looped block. We can do this using the `continue` instruction.

Run the following code cell and step through each line of code a line at a time using the `nbtutor` *Next*&nbsp;> button. Watch the program flow particularly closely when the `item` variable takes the value `three`.

```python
%%nbtutor --reset --force
for item in ['one', 'two', 'three', 'fish', 'four']:
    print(item)
    if item=='three':
        continue
    print(' and ')

print('All done...')
```
As you , you should see the `item` variable be updated to each item `one`, `two`, `three`, `fish` and `four` in turn. As the program iterates through the loop, the current value of the `item` variable is displayed. The value of the `item` variable is checked, and if it *does not* equal `three` the loop continues by displaying the word `and`, giving a message that bilds up as *one and two and three*.

However, when the value of `item` does match `three`, the `continue` statement is run and control passes back to the top of the loop before printing the word `and`; in this case, that means the next word in the list, `fish`, is printed after the word `three`, giving the output message *one and two and three fish*.

The loop continues to operate as before and the final message that is displayed is *one and two and three fish and four*.

<!-- #region -->
### Conditional tests using the conditional construct, `if...`

In the previous program, you may have noticed another new statement: an `if` statement. This is another sort of conditional statement. The `if` statement will test a logical condition and if it evaluates as `True`, then the program flow will pass to any statements contained within the `if` statement block.

```python
if LOGICAL_TEST_STATEMENT:
    #if the LOGICAL_TEST_STATEMENT evaluates as True
    # run the following command
    print('The statement was True...')
    
print("This will always be printed...")
```


In and of itself, the `if` statement is tested once and once only. *If* the conditional test pass, then control flows into the body of the *if* statement and then on to the next statement after the *if* construct. If the conditional test evaluates as false, then control passes immediately to the next statement *after* the if block.

In the `if` statement, the `==` sign is used to test whether the value of the thing on the left is the same as the value of the thing on the right.

So the following is `True`:
<!-- #endregion -->

```python
1 == 1
```

because numeric `1` does indeed equal numeric `1`. However, the following evaluates as `False` because numeric `1` *does not* equal the string `one`:

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

<!-- #region -->
As well as using the `==` operator to test for equivalence, we can also use a range of other operators. For example:


- `X != Y`: returns `True` if a a string or numerical value `X` is not equal to `Y`;
- `X > Y`: returns `True` if a numerical value `X` is *strictly greater than* a numerical value `Y`;
- `X < Y`: returns `True` if a numerical value `X` is *strictly less than* a numerical value `Y`;
- `X >= Y`: returns `True` if a numerical value `X` is *greater than or equal to* a numerical value `Y`;
- `X <= Y`: returns `True` if a numerical value `X` is *less than or equal to* a numerical value `Y`.


Try experimenting with you own equivalent, or unequivalent, statements in the code cell below.

*Feel free to create more code cells if you want to keep a record of things you have tried. Or comment out each line after you have tried it if you want to try mutliple statements in the same code cell.*
<!-- #endregion -->

```python
# TRY SOME EQUIVALENT AND UNEQUIVALENT STATEMENTS OF YOUR OWN HERE


```

<!-- #region activity=true -->
### Activity

Suppose Wednesday is early closing day. Building on elements from your earlier program that displays the days of the week, modify the program to use a `continue` statement so that it prints out the message *I could go shopping on DAY afternoon* for every day except Wednesday.
<!-- #endregion -->

```python activity=true
# YOUR ANSWER HERE
```

<!-- #region activity=true heading_collapsed=true -->
#### Answer
*Click on the arrow in the sidebar to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
I used a simple `if` statement to check if it was Wednesday. If it was, then the `continue` statement passed the program control flow back to the top of the loop *before* the program had a chance to print out that day of the week. 
<!-- #endregion -->

```python activity=true hidden=true
for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    
    if day=='Wednesday':
        continue
    print(f"I could go shopping on {day} afternoon.")
```

### Escaping from a loop early

As well as returning back to the top of a loop early using a `continue` statement, we may sometimes want to escape from a loop altogether before the loop would normally finish. We can achieve this using the `break` statement, which breaks the control flow out of a loop when it is encountered.

Run the following code cell, stepping through it a line at a time, again paying particulalry close attention when the `item` variable has the value `three`:

```python
%%nbtutor --reset --force
for item in ['one', 'two', 'three', 'fish']:
    print(item)
    if item=='three':
        break
    print(' and ')

print('All done...')
```
<!-- #region activity=true -->
### Activity  - Escape from a `for...in...` loop

Suppose we get weekends off. Using a `break` construct inside a `for...in...` loop, create a simple program that takes a list containing the days of the week in order *Monday*...*Sunday* and displays the message *DAY is a workday...* for days Monday to Friday, but then breaks out of the loop when it realises it is Friday.
<!-- #endregion -->

```python activity=true
# YOUR CODE HERE
```

<!-- #region activity=true heading_collapsed=true -->
#### Answer
*Click on the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
In this case, I display the print message before I break out of the loop using the `break` statement:
<!-- #endregion -->

```python activity=true hidden=true
for day in ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']:
    print(f"{day} is a workday.")
    if day=='Friday':
        break
```

## 1.3 Using a `while...` loop

A `while...` loop tests the truth of a statement on each iteration of the loop. In ‘pseudo-code’, the behaviour can be described as:

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

In some respects the `while` resembles an `if` statement in that if (while) the tested condition is true, then control passes into the body of the while statment block, and if it evaluates false, then control passes immediately to the next statement after the while block. However, *unlike* the `if` statement, when all the statements inside the `while` block have been executed, in sequential order, control does not then flow to the next statement after the while block: it passes back to the top of the while loop and the condition is re-evaluated.

In this way, the program can keep repeating the lines of code inside the while block until some condition is met, or some condition fails.

Note that if the conditionally tested value changes to a value that would cause the condition to evaluate as false whilst the program flow is inside the while block, the statements insde the while block will continue to execute in sequential order. Control only passes from the while statement to the statement after the while block at the point when control passes to the while statement and its condition is tested and found to evaluate as false.

Let’s see an example of how to use a `while` loop to help us keep track of whether we have counted up to a particular number yet.

<!-- #region -->
## 1.3 Using a `while...` loop

A `while...` loop tests the truth of a statement on each iteration of the loop. In ‘pseudo-code’, the behaviour can be described as:

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

In some respects the `while` resembles an `if` statement in that if (while) the tested condition is true, then control passes into the body of the while statment block, and if it evaluates false, then control passes immediately to the next statement after the while block. However, *unlike* the `if` statement, when all the statements inside the `while` block have been executed, in sequential order, control does not then flow to the next statement after the while block: it passes back to the top of the while loop and the condition is re-evaluated.

In this way, the program can keep repeating the lines of code inside the while block until some condition is met, or some condition fails.

Note that if the conditionally tested value changes to a value that would cause the condition to evaluate as false whilst the program flow is inside the while block, the statements insde the while block will continue to execute in sequential order. Control only passes from the while statement to the statement after the while block at the point when control passes to the while statement and its condition is tested and found to evaluate as false.

Let’s see an example of how to use a `while` loop to help us keep track of whether we have counted up to a particular number yet.

The following lines of code are rendered using language sensitive code styling within this markdown cell:


```python
#%%nbtutor --reset --force
counter = 1

while counter < 5:
    print(counter)
    counter = counter + 1
    
#Display the final value of counter
counter
```


Although it *looks* like code, we can't execute it becuase it isn't in a code cell.

Copy the code and paste it into the empty code cell below (or create your own new code cell) and run the cell and observe what happens.

Then uncomment the `%%nbtutor`cell magic by deleting the `#` symbol at the start of the first line and run it again to step through the code as it executes a line at a time.

Observe how the program flow repeatedly moves from the last line of the code inside the `while` block back up to the `while` statement, before going from the `while` statement to the final `counter` statement when the conditional tests eventually evaluate as false.
<!-- #endregion -->

```python

```

<!-- #region activity=true -->
### Activity – Use a `while` loop

The Python `random` function from the `random` package is capabale of generating a random number between 0 and 1, as you will see if you run the following cell repeatedly.
<!-- #endregion -->

```python activity=true
import random

random.random()
```

<!-- #region activity=true -->
We can think of this as a coin toss, where we toss ‘heads’ for values greater than or equal to 0.5, or ‘tails’ for values less than&nbsp;0.5.

Write a simple while loop that tests a simulated coin toss for as long as it tosses the equivalent of ‘heads’, printing ‘heads’ for each successful toss.

Run the code cell several times to see what happens.
<!-- #endregion -->

```python activity=true
# Add your code here
```

<!-- #region activity=true heading_collapsed=true -->
#### Answer
*Click on the arrow in the sidebar or run this cell to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
To test the coin toss, we are looking for a random value of greater than or equal to 0.5, that is, a value of `random.random() >= 0.5`.

We can use this as a conditional test in a `while` loop. In the body of the loop, we print ‘heads’ to show we are in the loop.
<!-- #endregion -->

```python activity=true hidden=true
while random.random() >= 0.5:
    print("heads")
```

<!-- #region activity=true hidden=true -->
If we run the cell multiple times, then sometimes nothing is printed (if the ‘coin’ flips as ‘tails’, that is, the first random value is *less than* 0.5); at other times, we may get one or more ‘heads’ displayed. (The most I saw in several attempts was eight heads in a row!)
<!-- #endregion -->

<!-- #region tags=["alert-success"] hidden=true -->
Typically, a package only needs to imported once into a notebook even if we call it from multiple calls.  However, if we run a cell run using the `%%nbtutor --reset --force` magic, it creates a fresh Python environment with no previously set variables or imported packages for its code execution. In such a case, we would need to import the package again onto that specific cell.
<!-- #endregion -->

### Infinite loops

We can create a special sort loop known as an *infinite loop* using the `while True:` construction, where the statement `True` *always* evaluates as `True` and so the loop repeats until the program is forced to stop or the flow is forced out of the loop and onto the next instruction using a `break` statement.

The following code cell demonstrates how to escape an otherwise infinite loop by using a `break` statement. Run the cell to see how it works. Uncomment the `nbtutor` magic to step through it a line at a time as it executes.

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
<!-- #region tags=["alert-success"] -->
In the expression `counter = counter + 1` we explictly set the new value of `counter` on the left hand side of the expression to be equal to the current value of `counter` incremented by `1`.

We could also use the equivalent expression `counter += 1`, which reads as "add the value on the right hand side of the expression to the numerical variable on the left hand side.
<!-- #endregion -->

<!-- #region -->
### Using a `while` loop in the simulator

Being able to loop *whilst* a particular condition holds allows us to perform actions *until* that condition no londer holds.

This may be particularly useful in a robot programming context, as the following simple example demonstrates.


To start with, load the simulator into the notebook:
<!-- #endregion -->

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds
%load_ext nbev3devsim
```

In the simulator reset the trace and select the *Grey_bands* background. (You can also disable the *Pen Down* control: we don’t need to keep track of where the robot has travelled for this activity.)

Now run the following code cell to download the program to the simulator and then run it in the simulator, observing the behaviour of the robot. (If you have already not selected the  *Grey_bands* background, it should be automatically loaded by the magic invocation.)

```python
%%sim_magic_preloaded -b Grey_bands
from ev3dev2.sensor import INPUT_2

# Drive the robot forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

# Create a variable that refers to the colour sensor on INPUT_2
colorLeft = ColorSensor(INPUT_2)

# For the sensor value, use the reflected light intensity as a percentage
sensor_value = colorLeft.reflected_light_intensity_pc
# We can also obtain the raw value as: colorLeft.reflected_light_intensity

# Test the sensor value; loop while the sensor value exceeds 99
while sensor_value > 99:
    # Display the sensor value in the simulator output window
    print(sensor_value)
    # Update the sensor_value variable to the latest sensor reading
    sensor_value = colorLeft.reflected_light_intensity_pc

# The sensor value is now greater than 99 so print a final message...
print("I now see {}".format( colorLeft.reflected_light_intensity_pc))
# And explicitly turn the motors off to stop the simulated robot
tank_drive.off()
```

When you run the program in the simulator, the robot should drive forwards until it encounters the first, light grey line, and then it should stop.

*By default, the robot will stop when the program ends, becuase the simulator run stops at the end of the program. However, it is good practice to explicitly turn the motors off yourself. By doing this, you know for sure what state the motors are in at the end of the program. In the above example, what would happen if, for some reason, the motor off command was omitted and the simulator carried on running even as the program execution had completed?*

The program works by checking the value from one of the robot’s sensors: a downward-facing light sensor, which you will meet in more detail in a later notebook. The sensor returns a ‘reflected light’ reading: a percentage value which relates to the colour of the background over which the robot is travelling. The simulator output display window shows the sensor value, starting at `100` when the robot is on the plain white background. This value is above the conditionally tested threshold value of `99` used in the original program’s `while` statement, and so the program continues looping round the while loop. When the robot encounters the first grey line, the sensor returns a lower value of just over 94 when I ran the program.

*Rather than testing and reporting the `colorLeft.reflected_light_intensity_pc` value directly, the program is constructed as it is because the sensor value may change in going from the `while` program step to the `print()` step. Even though computers may step between lines of code very quickly, they still take a finite time to do so.*

Try modifying the numerical value used in the `while` conditional test and downloading and running the modified program. Can you get the robot to stop as soon as it encounters the second medium grey band? How about on the third, dark grey line, or on the final, black line?

<!-- #region activity=true -->
### Activity – Counting up to 10
<!-- #endregion -->

<!-- #region activity=true -->
As well as programming the siunulated robot to respond to a sensor value, we can also get it to count aloud.

The following program, for example, when downloaded to the simulator, will cause the simulated robot to count aloud.

Can you get the robot to count to 10, rather than 5?
<!-- #endregion -->

```python activity=true
%%sim_magic

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

In this notebook, you have seen how we can control the way in which program statements are executed in a program by using various program flow control constructs and how we can use the `nbtutor` extension to step through and monitor the flow of simple Python programs executing in the notebook’s Python environment (unfortunately, it does not allow us to step through code we download into the simulator).


Regarding the program control flow, you have seen how:

- the `for...in...` loop allows a program to work through a set of statements in the loop body once for each item in a list of values or ‘iterator’ construct
- the `if...` conditional command checks a logical condition once and once only: if the tested condition evaluates as true, then control passes inside the block, and then continues after the if block; if the condition evaluates as false, then control passes immediately to the statement after the if block
- the `while...` loop allows us to repeatedly test a condition; if it is found to be true, then it passes control to a sequnece of instructions inside the while block. Once those instructions have been executed, control is passed back the top of the while loop and the test condition is evaluated again. If the while condition evaluates as false, then control passes to the first statement after the while block.

Control flow in `for` and `while` loops can also be interrupted using `continue` and `break` statements:

- `continue` prematurely forces the flow of control back to the top of the loop, rather than requiring all the instructions in the loop to execute and then passing control back to the top of the loop
- `break` prematurely forces the flow of control out of the loop to the next statement after the loop block, rather than requiring control to be passed following the failure of the conditional test at the top of the loop.

Control flow instructions are part of the core Python language and are used in a similar way inside in the simulator and the ‘native’ notebook Python environment.
<!-- #endregion -->

## Addendum

*Remember that addendum sections are optional and go beyond what’s needed for the module. Only look at these sections if you have the time.*

This addendum provides additional explanatory material that offers an insight into some of the technical issues associated with creating speech actions in a Jupyter notebook context as well as creating speech actions in a pure Python environment.


The robot simulator speech action is built up from a JavaScript function that builds on a built-in browser function for creating speech utterances. We can force the Jupyter notebook to run JavaScript code in the browser from a code cell using the `%%javascript` cell magic. This means we can get the browser to ‘speak’ by callng the browser speech functions via JavaScript directly.

*Note that there may be a brief delay between running the code cell and hearing the speech utterance.*

```javascript
speechSynthesis.speak(new SpeechSynthesisUtterance("hello"))
```

We can also create a simple wrapper around a JavaScript call that we can use in a Jupyter notebook context to speak, via the browser, from a Python statement:

```python pinned_outputs=[]
from IPython.display import Javascript

class Speech():
    def say(self, txt):
        display(Javascript(f'speechSynthesis.speak(new SpeechSynthesisUtterance("{txt}"))'))

speaker = Speech()
speaker.say('hello')
```

We can also create a simple Python program to count aloud up to 10, for example by using a `while` loop:

```python
n = 1

while n <= 10:
    speaker.say(n)
    n = n + 1
```

As currently defined, there is no way we can stop the `speaker` from counting unless we reload this notebook webpage.
