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

# Introduction to robot sensors and code functions

Sensors are at the heart of robotics. A machine without sensors cannot be a robot in our terms. The human body is replete with sensors. Our five external senses – sight, hearing, touch, smell and taste – and internal sensing such as balance and proprioception (body awareness) are all marvellously sophisticated.

In this week’s practical activities, we are concerned with how a robot can use sensory information to control its actuators. We will investigate a progression of control strategies:

1. dead reckoning – no sensor input

2. reflex behaviour – sensors *linked directly* to motors according to the sense–act model

3. deliberative behaviour – actuation depends on *reasoning* about sensor information and other knowledge, according to the sense–think–act model.

The first control strategy, dead reckoning, is an ‘open-loop’ control approach, since it does not use sensor input.

The second is an example of a ‘sense–act’ control strategy that you encountered earlier in the block; we will illustrate this control strategy using simulated implementations of simple Braitenberg vehicles.

Finally, there is the most complex control strategy, in which the robot deliberates on the sensor inputs in the context of other knowledge using an approach we refer to as ‘sense–think–act’. This involves *reasoning* and corresponds more closely to the way humans solve complex problems and plan actions in the long and short term.

But before we do that, we’ll have a look in a bit more detail at another powerful idea in computer programming: *functions*. You’ve already met some of these, but without much explanation. So now let’s introduce you to them for real.


# 1 Functions

Many of the programs we have used so far have been quite short with little, if any, reused code.

As programs get larger, it is often convenient to encapsulate several lines of code within a *function*. The multiple lines of code within the function can then be called conveniently from a single statement whenever they are needed.

Functions are very powerful, and if you have studied other programming courses then you may well be familiar with them.

For our purposes, the following provides a very quick overview of some of the key behaviours of Python functions. Remember that this isn’t a Python programming module per se; rather, it’s a module where we explore how to use Python to get things done. What follows should be enough to get you started writing your own functions, without creating too many bad habits along the way.

To see how we can create our own functions, let’s consider a really simple example: a function that just prints out the word *Hello*.

The function definition has a very specific syntax:

```python
def FUNCTION_NAME():
     ONE_OR_MORE_LINES_OF_CODE
```

Here are some of the rules relating to the syntactic definition of a Python function:

- the `FUNCTION_NAME` __MUST NOT__ contain any spaces or punctuation other than underscore (`_`) characters
- the function name __MUST__ be followed by a pair of brackets (`()`), that may contain something (we’ll see what later), followed by a colon (`:`)
- the body of the function __MUST__ be indented using space or tab characters; the level of indentation of the first line sets the effective ‘left-hand margin’ for the remaining lines of code in the function
- the body of the function must include __AT LEAST__ one valid statement or line of code __EXCLUDING__ comments; if you don’t want the function to do anything, but need it as a placeholder, use `pass` as the single line of required code in the function body.

It is good practice to annotate your function with a so-called ‘docstring’ (*documentation string*) providing a concise, imperative description of what the function does.

```python
def FUNCTION_NAME():
    """"Docstring containing a concise summary of the function behaviour."""
     ONE_OR_MORE_LINES_OF_CODE
```

Run the following code cell to define a simple function that prints the message *Hello*:

```python
def sayHello():
    print('Hello')
```

When we *call* the function, the code contained within the function body is executed.

Run the following cell to call the function:

```python
sayHello()
```

Functions can contain multiple lines of code, which means they can provide a convenient way of calling multiple lines of code from a single line of code.

Functions can also be used to perform actions over one or more *arguments* passed into the function. For example, if you want to say hello to a specific person by name, we can pass their name into the function as an argument, and then use that argument within the body of the function.

We’ll use a Python f-string as a convenient way of passing the variable value, by reference, into a string:

```python
def sayHelloName(name):
    """Print a welcome message."""
    print(f"Hello, {name}")
```

Let’s call that function to see how it behaves:

```python
sayHelloName("Sam")
```

What happens if we forget to provide a name?

```python
sayHelloName()
```

Oops... We have defined the argument as a *positional* argument that is REQUIRED if the function is to be called without raising an error.

If we want to make the argument optional then we need to provide a *default value*:

```python
def sayHelloName(name='there'):
    """Print a message to welcome someone by name."""
    print(f"Hello, {name}")
    
sayHelloName()
```

If we want to have different behaviours depending on whether a value is passed for the name, then we can set a default such as `None` and then use a conditional statement to determine what to do based on the value that is presented:

```python
def sayHelloName(name=None):
    """Print a message to welcome someone optionally by name."""
    if name:
        print(f"Hello, {name}")
    else:
        print("Hi there!")

sayHelloName()
```

Sometimes, we may want to get one or more values returned back from a function. We can do that using the `return` statement. The `return` statement essentially does two things when it is called: firstly, it terminates the function’s execution at that point; secondly, it optionally returns a value to the part of the program that called the function.

<!-- #region activity=true -->
### 1.1 Activity — Defining a simple function

Run the following code cell to define a function that constructs a welcome message, displays the message *and returns it*:
<!-- #endregion -->

```python activity=true
def sayAndReturnHelloName(name):
    """Print a welcome message and return it."""
    message = f"Hello, {name}"
    print("Printing:", message)
    return message
```

<!-- #region activity=true -->
What do you think will happen when we call the function?
<!-- #endregion -->

<!-- #region student=true -->
*Write your prediction here about what you think will happen when the function is run here __before__ you run the code cell to call it.*
<!-- #endregion -->

```python activity=true
sayAndReturnHelloName('Sam')
```

<!-- #region activity=true -->
Run the above cell to call the function. Did you get the response you expected?
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
#### Discussion

*Click on the arrow in the sidebar or run this cell to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
In the first case, a message was *printed* out in the cell’s print area. In the second case, the message was returned as the value returned by the function. As the function appeared on the last line of the code cell, its value was *displayed* as the cell output.
<!-- #endregion -->

### Setting variables to values returned from a function

As you might expect, we can set a variable to the value returned from a function:

```python
message = sayAndReturnHelloName('Sam')
```
<!-- #endregion -->
If we view the value of that variable by running the following cell, what do you think you will see? Will the message be printed as well as displayed? 

<!-- #region student=true -->
*Write your prediction about what you think will happen when the function is run here __before__ you run the code cell to call it.*
<!-- #endregion -->

```python
message
```

Only the value returned from the function is displayed. The function is not called again, and so there is no instruction to *print* the message.

To return multiple values, we still use a single `return` statement:

```python
def sayAndReturnHelloName(name):
    """Print a welcome message and return it."""
    message = f"Hello, {name}"
    print("Printing:", message)
    return (name, message)

sayAndReturnHelloName('Sam')
```

Finally, we can have multiple return statements in a function, but only one of them can be called from a single invocation of the function:

```python
def sayHelloName(name=None):
    """Print a message to welcome someone optionally by name."""
    if name:
        print(f"Hello, {name}")
        return (name, message)
    else:
        print("Hi there!")
    return

print(sayHelloName(), 'and', sayHelloName("Sam"))
```

<!-- #region -->
Generally, it is *not* good practice to return different sorts of object from different parts of the same function.


There is quite a lot more to know about functions, particularly in respect of how variables inside the function relate to variables defined outside the function, a topic referred to as *variable scope*. But for a treatment of that, you will need to refer to a module with a heavier emphasis on teaching programming.
<!-- #endregion -->

## 1.2 Using functions in robot control programs

We’ll start by considering the simple program we wrote to make the robot trace out a square.

If you recall, our first version of this program explicitly coded each turn and edge movement, and then we used a loop to repeat the same action several times.

To get things set up correctly, load the simulator into the notebook:

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```


Move the robot to the bottom left-hand corner of the simulator window, run the following code cell to download the program to the simulator and then run the programme in the simulator.

Tweak the function argument settings until the robot approximately traces out the shape of a square.

```python
%%sim_magic_preloaded -x 500 -y 500 -a 0 -p -C

SIDES = 4

# Try to draw a square, ish...
STEERING = -100
TURN_ROTATIONS = 1.6
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 4

for side in range(SIDES):
    #Go straight
    # Set the left and right motors in a forward direction
    # and run for the specified number of forward rotations
    tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                                STRAIGHT_SPEED_PC,
                                STRAIGHT_ROTATIONS)

    #Turn
    # Set the robot to turn on the spot
    # and run for a certain number of rotations *of the wheels*
    tank_turn.on_for_rotations(STEERING,
                               SpeedPercent(TURN_SPEED),
                               TURN_ROTATIONS)
```

We could can extract this code into a function that allows us to draw a square whenever we want. By adding an optional `side_length` parameter we can change the side length as required.

Download the following program to the simulator and run it there.

Can you modify the program to draw a third square with a size somewhere between the size of the first two squares?

```python
%%sim_magic_preloaded

SIDES = 4

# Try to draw a square
STEERING = -100
TURN_ROTATIONS = 0.826
TURN_SPEED = 40

STRAIGHT_SPEED_PC = SpeedPercent(40)
STRAIGHT_ROTATIONS = 6

def draw_square(side=STRAIGHT_ROTATIONS):
    """Draw square of specified side length."""
    for side in range(SIDES):
        #Go straight
        # Set the left and right motors in a forward direction
        # and run for the number of rotations specified by: side
        tank_drive.on_for_rotations(STRAIGHT_SPEED_PC,
                                    STRAIGHT_SPEED_PC,
                                    #Use provided side length
                                    side)

        #Turn
        # Set the robot to turn on the spot
        # and run for a certain number of rotations *of the wheels*
        tank_turn.on_for_rotations(STEERING,
                                   SpeedPercent(TURN_SPEED),
                                   TURN_ROTATIONS)
        
        
# Call the function to draw a small size square
draw_square(4)

# And an even smaller square
draw_square(2)
```

<!-- #region activity=true -->
### Optional activity

Copy the code used to define the `draw_square()` function, and modify it so that it takes a second `turn` parameter that replaces the `TURN_ROTATIONS` value.

Use the `turn` parameter to tune how far the robot turns at each corner.

Then see if you can use a `for...in range(N)` loop to call the square-drawing function several times.

Can you further modify the program so that the side length is increased each time the function is called by the loop?

Share your programs in your Cluster group forum.
<!-- #endregion -->

## 1.3 Functions: a summary

You have seen that a Python function is a *named* sequence of commands that can be ‘called’ or invoked from anywhere in the main program or from another function. Functions offer four advantages:

- they allow a piece of program functionality to be ‘encapsulated’ in a clear and detached way
- they allow the functionality to be used many times from anywhere in the program
- they simplify the program, making it easier to understand
- they make programs less prone to error.

Other programming languages have similar features to functions that offer additional benefits. Depending on the language, or the context in which they are defined, these may be known as *macros*, *methods*, *procedures* or *subroutines*. 
