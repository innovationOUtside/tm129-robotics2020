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

# 5 Functions

<!-- #region -->
Many of the programmes we have used so far have been quite short programmes with little, if any, reused code.

As programmes get larger, it is often convenient to encapsulate several lines of code within a *function*. The multiple lines of code within the function can then be called conveniently from a single statement whenever they are needed.

Functions are very powerful, and if you have studied other programming courses, you may well be familiar with them.

For our purposes, the following provides a very quick review of some of the key behaviours of Pyhton functions. It should be enough to get you started writing your own functions, without creating too many bad habits along the way.

To see how we can create our own functions, let's consider a really simple example, a function that just prints out the word *Hello*.

The function definition has a very specific syntax:

```python
def FUNCTION_NAME():
     ONE_OR_MORE_LINES_OF_CODE
```

Here are some of the rules relating to the sytactic defintion of a Python function:

- the `FUNCTION_NAME` __MUST NOT__ contain any spaces or punctuation other than underscore (`_`) characters;
- the function name __MUST__ be followed by a pair of brackets (`()`), that may contain something (we'll see what later), followed by a colon (`:`);
- the body of the function __MUST__ be indented using space or tab characters. The level of indentation of the firxt line sets the effective "left-hand margin" for the remaining lines of code in the function;
- the body of the function must include __AT LEAST__ one valid statement / line of code __EXCLUDING__ comments.

It is also good practice to 

```python
def FUNCTION_NAME():
    """"Docstring contain a concise summary of the function behaviour."""
     ONE_OR_MORE_LINES_OF_CODE
```
<!-- #endregion -->

```python
def sayHello():
    print('Hello')
```

The function ....

```python
sayHello()
```

Add an argument:

```python
def sayHelloName(name):
    print(f"Hello, {name}")
```

```python
sayHelloName()
```

```python
sayHelloName("Sam")
```

```python
def sayAndReturnHelloName(name):
    message = f"Hello, {name}"
    print(message)
    return message
```

```python
sayAndReturnHelloName('Sam')
```

```python
_
```

```python
message
```

## Using Functions in Robot Control Programs

We’ll start by considering the simple program we first wrote to make the robot trace out a square. The first thing to do was to write the motor commands needed to drive forward along one edge of the square and then turn through 90°. 


![figure ../tm129-19J-images/tm129_rob_p4_f020.png](../tm129-19J-images/tm129_rob_p4_f020.png)


Figure 7.1 Listing


comment Macro Square

output left_motor on A

output right_motor on C

main

      comment : drive along side and then turn

      forward [left_motor right_motor]

      on [left_motor right_motor] for 200

      backward [right_motor]

      on [left_motor right_motor] for 103

      comment --- end of program

This set of statements carries out a useful single job – to drive along a side and then turn through a right angle. The macro construct lets us give this group of statements a name and then call the macro by name wherever we want to. The listing below shows what this looks like.


![figure ../tm129-19J-images/tm129_rob_p4_f021.png](../tm129-19J-images/tm129_rob_p4_f021.png)


Figure 7.2 Listing: macro_square


comment Macro Square

output left_motor on A

output right_motor on C

macro driveSide

      comment : drive along side and then turn

      forward [left_motor right_motor]

      on [left_motor right_motor] for 200

      backward [right_motor]

      on [left_motor right_motor] for 103

main

      comment do four sides

      repeat 4

            call driveSide

      comment --- end of program

I’ve given the macro the name `driveSide`. You are free to choose any name you want (subject to the usual rules for RobotLab identifiers) when you write a macro; try to choose a meaningful name that helps anyone reading the program know what the macro does. The definition of the macro occurs just once, before the `main` part of the program. Inside the main program, you can invoke or call the macro wherever you want, using the `call` statement. Here I’ve only used it once, but often a macro will be called in several places. Notice that the main part of the program is now very simple to understand.


## 5.1 Activity: Creating a function


In this activity you will use RobotLab to create the program `macro_square` that was used as an example at the beginning of this section.

Start by creating a new program using the New program  ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f022.gif](../tm129-19J-images/tm129_rob_p4_f022.gif)  toolbar button or `File &gt; New` command. <div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+N</p></div>

We add the macro definition by dragging a `macro` statement from the command list. (This statement isn’t in the `Basic` list, so you will have to switch to the `By type` or `By name` lists to find it.) Note that the macro definition must be placed *before* the `main` statement.


![figure ../tm129-19J-images/tm129_rob_p4_f023.jpg](../tm129-19J-images/tm129_rob_p4_f023.jpg)

The new macro will be shown as `macroOne(param1, param2)`. As is usual with RobotLab, the names are default placeholders and we will change them to something meaningful. Inside the brackets are default *parameters*, `param1` and `param2`. A parameter is a way of passing data into the macro. For this example, we won’t be using parameters, but we’ll discuss them in more detail later, in Section 7.2.

With the new macro `macroOne` highlighted in the `Program` window, we can change its details in the `Key–Value` pane. Change the name `macroOne` to `driveSide`. Since we won’t use parameters for this example, simply delete `param1, param2`, as shown below. 


![figure ../tm129-19J-images/tm129_rob_pa4_f7_2b.png](../tm129-19J-images/tm129_rob_pa4_f7_2b.png)

Now we need to define what the macro does. Add suitable motor statements to make Simon drive forward and turn through 90°. Take care when dragging in these statements that they are indented correctly so that RobotLab understands that these statements belong to the macro and not the main sequence. Your macro should look like the following.


![figure ../tm129-19J-images/tm129_rob_p4_f025.png](../tm129-19J-images/tm129_rob_p4_f025.png)


Figure 7.3 Listing: macro_square; driveSide


macro driveSide

      comment : drive along side and then turn

      forward [left_motor right_motor]

      on [left_motor right_motor] for 200

      backward [right_motor]

      on [left_motor right_motor] for 103

When you have input the macro, you may find it helps to minimise it so that statements can be easily added to the `main` part of the program. Do this by clicking on the box containing the minimise [-] icon:<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Left cursor key or NumMinus</p></div>

Now you are ready to input the main part of the program.


![figure ../tm129-19J-images/tm129_rob_p4_f026.png](../tm129-19J-images/tm129_rob_p4_f026.png)


Figure 7.4 Listing: macro_square; main program


comment Macro Square

output left_motor on A

output right_motor on C

[+] macro driveSide

main

      comment do four sides

      repeat 4

            call driveSide

      comment --- end of program

To call or *invoke* the macro, we use the `call` command. Drag a `call` command into the body of a `repeat` loop, as shown above. 

When you drag a new `call` command into your program, it will be created with default names. Use the `Key–Value` window to change the name of the macro being called to `driveSide`. To make sure you don’t make any typing slips, use the Expression builder.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+Enter</p></div> Click the  ![inlinefigure ../tm129-19J-images/tm129_rob_p2_f036a.gif](../tm129-19J-images/tm129_rob_p2_f036a.gif)  button to open the Expression builder, delete the current name, find `driveSide` in the list and drag it into the expression.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Use Tab and cursor keys to select; press Space to add; press Enter to finish</p></div> Click `OK` when you have finished.


![figure ../tm129-19J-images/tm129_rob_p4_f028.png](../tm129-19J-images/tm129_rob_p4_f028.png)

Finally, delete the parameters since you are not using any here.


![figure ../tm129-19J-images/tm129_rob_p4_f029.png](../tm129-19J-images/tm129_rob_p4_f029.png)

Run your program. Does it do what you expect? Make sure you can follow the path of execution in the program. Turn on the trace (use `Run &gt; Trace`) and use `Pause` ![inlinefigure ../tm129-19J-images/tm129_rob_rl_pause.gif](../tm129-19J-images/tm129_rob_rl_pause.gif)  and `Step` ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f012.gif](../tm129-19J-images/tm129_rob_p4_f012.gif)  to follow the way the macro is called in the main program, the body of the macro is executed, and then control returns to the main program.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: F7, F6</p></div>

My version of the program code is given in the program `macro_square` in the `week-4` folder. Try running that if you have problems. 

Notice in passing that my program doesn’t use named constants such as `turnTime` and `forwardTime`. Previously I suggested that using named constants rather than literal numeric values was good practice, so why haven’t I followed my own advice? Using named constants is particularly useful when the same value is used in many places, as when we had several `on…for` statements used to rotate Simon by the same amount. But with the `driveSide` macro, each literal number occurs in a single place only, so there is less need for a named constant.


## 5.2 Activity: Creating a function with a parameter


In this activity, we’ll modify the program you have just written so that it can draw rectangles with two long sides and two short sides. To do this, we’ll change the definition of `driveSide` so that it can draw sides of different length.

Open the `macro_square` program you wrote in the previous activity. Use `File &gt; Save As…` to save a new copy of this called `macro_rect`;<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, F, A</p></div> we’ll work on this version and leave the original `macro_square` unchanged.

Highlight the `macro` statement that defines `driveSide`. We will leave the name of the macro unchanged, but now we want to add a parameter to control how long the side will be. We will call this `forwardTime`. Click in the `params` field and type `forwardTime`; press Enter when done. 

Now change the literal number in the `on…for` statement to use the new parameter `forwardTime`.

The macro definition should now be as follows:


![figure ../tm129-19J-images/tm129_rob_p4_f030_from_au.png](../tm129-19J-images/tm129_rob_p4_f030_from_au.png)


Figure 7.5 Listing: macro_rect; driveSide


macro driveSide(forwardTime)

      comment : drive along side and then turn

      forward [left_motor right_motor]

      on [left_motor right_motor] for forwardTime

      backward [right_motor]

      on [left_motor right_motor] for 103

[+] main

We must also change the call to supply a value for the time. Highlight the `call driveSide` statement and enter 200 in the `params` field. This should now appear as:

`call driveSide(200)`

Test the program so far – it should draw a square. Notice that `forwardTime` in the `driveSide` macro will take on the value of whatever value is used in the `call` statement. 

As yet, the program only draws squares. Modify it so that it draws a rectangle with long and short sides. 
<!--ITQ-->

#### Question

Would you like a hint?


#### Answer

You will need two calls to `driveSide` with different values of the parameter.
<!--ENDITQ--><!--ITQ-->

#### Question

Would you like to see my code?


#### Answer

You will need to change the loop as follows

`      repeat 2`

`            call driveSide(300)`

`            call driveSide(100)`

My version of the program code is given in the program `Macro_rect_solution` in the `week-4` folder. Try running that if you have problems. 
<!--ENDITQ-->

## 5.3 Functions: a summary


You have seen that a RobotLab *macro* is a named sequence of commands that can be ‘called’ or invoked from anywhere in the main program or from another macro. Macros offer four advantages:

* they allow a piece of program functionality to be ‘encapsulated’ in a clear and detached way

* they allow the functionality to be used many times from anywhere in the program

* they simplify the program, making it easier to understand

* they make programs less prone to error.

Other programming languages have similar features to macros that offer additional benefits. Depending on the language, these may be known as *functions*, *methods*, *procedures* or *subroutines*. 

This is the end of Robot Lab Session 4.

