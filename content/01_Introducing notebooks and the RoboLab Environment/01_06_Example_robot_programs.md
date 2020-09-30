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
# 6 Example robot programs

In this notebook, you will see various examples of robot programs.


 at this stage the intention is to give you an overview of the sorts of things that are possible, rather than expecting you to learn and remember the details.

Load the simulator widget into the notebook in the normal way by running the following code cell.

<!-- #endregion -->

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```
<!-- #region hideCode=true hidePrompt=true -->
## 6.1 Robots That Count

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
If we provide *three* arguments, `range(M, N, S)`, it spans a range of integers from $M$ to $N-1$ with a step value $S$ between them:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
M = 0
N = 30
S = 10

list(range(M, N, S))
```

<!-- #region hideCode=true hidePrompt=true -->
If we set $M=0$, $N=30$ and $S=10$, the first value returned from the range is the initial start value, $0$.

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
Although we set the range value as $5$, remember that this means the robot will count, by default, from $0$ in steps of $1$ to $N-1$. So the robot will count $0, 1, 2, 3, 4$, as we can see if we explicitly enumerate the values created by the `range()` statement:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
list(range(5))
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
### 6.1.1 Activity
In the following code cell, create a `range()` statement that will creates a list of numbers from $1$ to $5$ inclusive. Use a `list()` statement to generate a list from the `range()` statement.

Run the code cell to display the result so you can check your answer:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true
# Display a list of values [1, 2, 3, 4, 5] created from a single range() statement

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
We can display a range of values from $1$ to $5$ inclusive by using a range command of the form `range(M, N)` where `M=1`, the initial value, and $N=5+1$, since the the range spans to a maximum value less than or equal to $N-1$:
<!-- #endregion -->

```python hideCode=true hidePrompt=true activity=true hidden=true
list(range(1, 6))
```

<!-- #region hideCode=true hidePrompt=true activity=true hidden=true -->
We can now create a programme that counts from one to five inclusive:
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
## 6.2 Announcing Bands As The Robot Encounters Them

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
### 6.2.1 Activity - Announce When the Robot Has Left a Band

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
#### Answer

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

## 6.3 Creating Your Own Programme From Scratch

You've already seen several robot control programmes in this notebook, and you now you have an opportunity to create your own from scratch.

The following activity includes the skeleton of a programme based on descriptive, non-executed comments that describe what each line of the programme should do.

Using comments in this way provides one way of helping you plan or design a new programme.

As for the lines of code that you will need to write: you have already seen examples of similar lines in the programmes you have already encountered.

Reusing lines of code copied from programmes that have used such lines successfully in previous programmes is a completely valid way of writing your own programmes.

<!-- #region hideCode=true hidePrompt=true activity=true -->
### 6.3.1 Activity - Count the Bands

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
Using the comment skeleton as a plan for the program, we can reuse statements from the previous programmes with just a few additions.

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


# TO DO  - Widget automation and  `-R` switch 

<!-- #region hideCode=true hidePrompt=true -->
## Summary

In this notebook, you have seen how we can use the simulator to load in a particular background and log and chart sensor values captured as the robot moves over the simulator background both within the simulator and in the notebook environment itself.

You have also seen how we can get the robot to count as we iterate through a range of values.

By keeping track of previous and current sensor values, you have seen how the robot can identify when it encounters a new feature in the simulated world, such as entering or leaving a coloured band. Using the speak functionality, the robot can also alert us to when it encounters a new object.

This completes the practical activities for this week.
<!-- #endregion -->
