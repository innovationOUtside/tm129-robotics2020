# 3 Some features of RoboLab


In this section you will run some other RoboLab programs. The purpose is for you to observe what happens, to see some of the features of RoboLab, and to begin to see how other behaviours are controlled by the programs. This section is intended to give you an overview, and you are certainly not expected to remember the details.


## 3.1 Activity: Keeping a robot in an area

This activity demonstrates how to keep a robot inside a particular area bounded by a boxed area marked out on the floor of the world. 

Load the simulator package and then load and display the simulator widget:

```python
from nbev3devsim import ev3devsim_nb as eds
%load_ext nbev3devsim
```

```python
roboSim = eds.Ev3DevWidget()
display(roboSim)
```

Select the `Loop` background which loads the robot in to the centre of a large rectangle drawn with thick black lines. 

The following `Stay_inside` program causes the robot moves forwards until its light sensor detects the black contour, at which point the robot reverses direction. When it encounters the contour again it changes direction. In this way the robot shuttles backwards and forwards inside the contour indefinitely.

Run the code cell to load the program into the simulator, then click on the simulator *Run* button; hhen you are ready to stop the program, click on the simulator *Stop* button.

```python
%%sim_magic_preloaded roboSim

# Stay inside
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity))
    if colorLeft.reflected_light_intensity < 100:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)
        # drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

At the start of the program, a `#` sign identifies the line as a comment line, in this case giving a very concise statement of the objective of the programme. Comments are "free text" areas that are not exeucted as lines of Python code. As such, they can be used to provide annotations or explanations of particular parts of the programme, or "comment out" lines of code that are unnecessary.

The program starts by using a "tank drive" to drive the robot forwards at about half it's full speed (the left wheel and the right wheen are both powered on at 50% of their maximum speed).

The `while True:` command means *do everything that follows for ever (or until the user stops the program)*. The `:` is *required* and it defines what to do if the tested condition evaluates as true.

The next line is indented, and starts the definition of a code block, each line of which will be executed in turn. The lines of code that define the code block are indented to the same level. If the condition evaulated by the `while` statement was not true, then the code block would not be executed.

The `print('Light_left: ' + str(colorLeft.reflected_light_intensity))` command prints the current value of the left light sensor, which is reading the "reflected light intensity" to the output display window. As you will see later, this value can also be viewed via a dynamically updated chart, as well as analysed "offline" in the Python notebook when the simulation run has finished.

The next line in the code block, `if colorLeft.reflected_light_intensity < 40:`, compares a specific sensor reading, interpreted in a particular way, to a particular value (100). If the value is below that threshold, as it is when the robot is over the black like, the programme moves on to a new code block defined by lines of code that are further indented.

On the first line of code in that new code block, the robot drives *backwards* at half speed for 2 rotations of the wheels (`tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)`). (According to the [documentation](https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#ev3dev2.motor.MoveTank.on_for_rotations), *if the left speed is not equal to the right speed (i.e., the robot will turn), the motor on the outside of the turn will rotate for the full rotations while the motor on the inside will have its requested distance calculated according to the expected turn*).

After the robot moves backwards, there is a comment line suggesting what the next executed line of code does (`# drive in a turn for 2 rotations of the outer motor`) and then the robot turns on the spot (`tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)`).

Finally, the robot is set to drive forwards again (`tank_drive.on(SpeedPercent(50), SpeedPercent(50))`) and the sequence is repeated, with the programme control flow looping back to the while statement and then working through each step in turn again. While the sensor reading is above 100, the robot keeps going. Every time it "sees" the black contour it reverses the direction of the motors, and then turns ebfore driving forwards again. In this way the simulated robot shuttles backwards and forwards, staying inside the area defined by the contour.

How do you think the simulated robot in this activity compares with a real robot?


### Viewing the stay inside test on a real robot

<br/><br/>
<div class='alert-danger'>TO DO: the programmes should work on an EV3 running [`python-ev3dev`](https://python-ev3dev.readthedocs.io/). A [Visual Studio Code extension for browsing ev3dev devices](https://github.com/ev3dev/vscode-ev3dev-browser) seems to provide an environment for running the `python-ev3dev` code on a real robot which is perhaps something worth exploring. *Note that VS Code can also run notebooks, although I'm not sure if the simulation widget will run in that environment.*</div>
<br/><br/>

The following video clip shows a simple Lego robot executing the `Stay_inside` program discussed above. 
<!--MEDIACONTENT--><!--ENDMEDIACONTENT-->
You will notice that the real robot does not shuttle backwards and forwards as precisely as the simulated robot. Real robots are ‘noisy’, but not just in terms of the sound they make. There is also ‘noise’ in their mechanical gearing and control: the motors don’t go at precisely the expected speed, the gears may not mesh perfectly, the wheels may slip or skid, and the sensors do not give instantaneous or perfect readings.

In other words, real robots may have sloppy and relatively unpredictable mechanisms so that the same control commands from the same initial position may result in a variety of outcomes. For this reason, the RobotLab simulator has a noise feature that allows you to set random variations to the motor speeds and sensor readings. This ‘noise’ makes the simulated robot behave more realistically. It will be used in later Robot Lab sessions. 




## Using Less Magic...

In the previous program, the `tank_drive` and `tank_turn` elements are predefined by our use of the `%%sim_magic_preloaded` magic. This really is a bit like magic, because it allows us to write Python code that would not ordinarliy be valid code. The magic itself defines some essential Python code that is *prepended* (that is, added to the start of) out programme code before it is downloaded to the simulated robot.

The following code cell uses a slightly less powerful magic, `%%sim_magic_imports`, that still masks some of the complexity in creating a valid Python programme although in this case it does require you to define the `tank_turn` and `tank_move` statements in turns of slightly lower level building blocks.

As with the `Move_a_robot` programme, the `MoveSteering` and `MoveTank` commands are commands provided the `ev3dev` Python package and then configured to use particular outputs on the (simulated) robot (`OUTPUT_B` and `OUTPUT_C`).

In addition, the light sensor is defined using the `ColorSensor` command to confgure the sensor attached to `INPUT_2` as a colour sensor. The light sensor is shown as small white circle contained within a grey square on the simulated robot.

```python
%%sim_magic_imports roboSim

# Stay inside
tank_turn = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

colorLeft = ColorSensor(INPUT_2)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity))
    if colorLeft.reflected_light_intensity < 100:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)
        # drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

<!-- #region -->
## A Complete Python Programme


The following code cell shows a fully defined Pyhton program. In this case, a series of "package import" statements appear at the start of the programme. Python packages are code libraries written to support particular activities.

The core Python language includes a variety of packages that are distributed as part of the Python language, but additional packages can be written using core Python langauge elements, *or* Python commands imported from other additional packages, to build every moe powerful commands.

In particular, the Python `ev3dev` package provides a range of language constructs that allow us to write a Python programme that can work with a Lego EV3 brick running the `ev3dev` operating system, or our `nbev3devsim` simulated robot.

As you can see from the code cell below, which uses the minimal `%%sim_magic` magic to download just the contents of the cell to the simulator, in this case we `import` the custom elements we need `from` the `ev3dev` Python package that we then make use of in our programme. 
<!-- #endregion -->

```python
%%sim_magic roboSim

# Stay inside
from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor

tank_turn = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
colorLeft = ColorSensor(INPUT_2)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Light_left: ' + str(colorLeft.reflected_light_intensity))
    if colorLeft.reflected_light_intensity < 100:
        tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)
        # drive in a turn for 2 rotations of the outer motor
        tank_turn.on_for_rotations(-100, SpeedPercent(75), 2)
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))
```

## 3.2 Activity: Investigating sensors


In this activity you will experiment with a light sensor.

<br/><div class='alert-success'>To make it easier to see what's going on, click on the code cell that is used to display the simulator and use the notebook toolbar up/down arrows to move the cell down to this part of the notebook, closer to the code cells we will be using to download new programmes into the simulator.</div>

<br/><div class='alert-warning'>We need to think about making a more workable UI, within the constraints of limited time and skill available to spend on that issue right now... Which is to say, suggestions are welcome, but without PRs, they may may well `> /dev/null`...</div>


This is similar to the Lego light sensor:

TO DO image: *A Lego light sensor. This is a blue Lego brick, 4 x 2 studs in size with a wire emerging from one end. At the other end, two small lenses are visible. One is clear – this is the light sensor itself. Next to it is a red LED which can be used as a light source to illuminate a surface so that the sensor measures light reflected from the surface rather than ambient light levels.*


In the simulator, load in the *Grey bands* backgorund, which displays a white background overlaid by four grey bars of different in intensity, ranging from a pale grey to black.


The simulated robot drives over the background, logging the light sensor data as it does so.

Here's the complete programme:

```python
%%sim_magic roboSim
# Sensor_sim
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor


tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
colorLeft = ColorSensor(INPUT_2)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Colour: ' + str(colorLeft.reflected_light_intensity ))
```

We can also use the `%%sim_magic_preloaded SIMULATOR` magic to preload the drive and sensor configurations and references to minimise the clutter in *our* code, whilst remembering that it is still required for the programme to run, and will be loaded in automatically by the magic:

```python
%%sim_magic_preloaded roboSim
# Sensor_sim preloaded

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Colour: ' + str(colorLeft.reflected_light_intensity ))
```

Download either variant of the program to the simulator and run it, stopping the programme when the robot has gone passed the final black line.

As the programme runs, you should notice that that a sequence of logged data values from the sensor are displayed in the output window. If you scroll up through the display in that window you should notice that the sensor values changed as the robot crossed over each grey line.


### SAQ TO DO

What value does the sensor give when the robot is placed on the white background? What sensor values are returned for when the light sensor is over the light grey, medium grey, dark grey and black bands?

Do you notice anything strange about the sensor values, particularly when the robot encounters or leaves a particular band?


#### Answer

*Click the arrow in the sidebar to reveal the answer.*


I get the following readings for the reflected light intensity readings from the light sensor:

- white background: `255`
- light grey band: `220`
- medium grey band: `211`
- dark grey band: `128`
- black band: `0`

There is some "noise" in the form of intermediate values as the robot goes into and leaves the band. This is becuase the sensor has a "width" so it may be averaging readings where part of the sensor is over the white background and part of it is over the coloured band.

<!-- #region -->
## Activity - Viewing the Logged Data - The Simulator Datalog Chart Display

As well as displaying the logged data values using the output display, the print messages are parsed and used to extract data values so that they can be displayed on a dynamically updated line chart.

Enable the data charter by clicking the *Show chart* check box in the simulator and then check the *Colour* trace checkbox.

*TO DO - need a better way to set and handle traces?*


Reset the start location of the robot either by dragging it back to the start or clicking the *Move* button to reset the original location for the current simulator setup.

Run the simulator programme again until the robot has crossed over all the lines, observing how the chart is updated with the live sensor values. Can you see where the robot encounters the different coloured bands? What values are recorded for each band?

From the chart, can you read off the values for each band?
<!-- #endregion -->

### Answer

*Click the arrow in the sidebar to reveal the answer.*

<!-- #region -->
The following diagram shows the result of showing the real time data logging chart:

![The simulator Data log window, with a graph showing sensor data. The graph has a vertical axis with a scale that runs from 0 to 250, and a horizontal axis that runs from 0 to 400. A line chart is plotted showing successive sensor readings. Reading the graph from left (the first sensor reading) to right (the last sensor reading), the line is horizontal at a y-value of 255 until an x value of about 100, followed by a drop to about 220 until about x=145, at which point it climbs steeply back up to y=255, remaining at that level until about x=190. There is a further sharp drop to about (x, y) equal to (190, 210), then back up to to 255 at about x=225, until another edge at about x=280 down to (280, 130); the chart then goes back up from about (320, 130) to (321, 255), then down to y=0 at about x=360, staying then until x is almost 410, at which point the line climbs back up to 255 , satys there for a short while, and the trace ends.](../images/Section_00_03_-_charting.png)


As the robot progresses across the bands, the bars that it encounters get progressively darker, so the sensor readings reduce. Between the bands, as the robot crosses the white background, the sensor reading go back up to their initial, maximum reading.

If you hover your cursor over the chart, all the recorded trace values at that x-position on the chart are displayed. These are the values that were revorded and displayed, taken from the midpoint of the chart, when I ran the experiment.


- white background: `255`
- light grey band: `220`
- medium grey band: `211`
- dark grey band: `128`
- black band: `0`

*(You may have noticed that the simulation running in a slightly more "stuttery" way than when the chart is not displayed as your computer has to do more work in terms of dynamically updating the chart.)*

*TO DO - I think the chart may also be checking all the sensor values and perhaps forcing them to be calculated? Need to optimise this to only calculate and plot values that are actually being logged.*

*TO DO - should we experiment with generating text descriptions of charts, eg as per [Automatically Generating Accessible Text Descriptions of Charts](https://blog.ouseful.info/2016/04/29/first-thoughts-on-automatically-generating-accessible-text-descriptions-of-ggplot-charts-in-r/)?*
<!-- #endregion -->

## Viewing the Logged Data - Uploading the Logged Data to the Notebook

As well as inspecting the data log values in the simulator output window and via the embedded datalog chart, we can also export the logged data from the simulator into the Python enviornment used by the notebook. This then allows us to analyse and chart the data within a complete Python environment.

*TO DO - should we have some magic to get data out of the datalog?*

The following code cell shows how to access the datalog from the simulator in the notebook's Python environment. The *pandas* package is a very powerful package for working with tabular data.

*You can learn more about using pandas from the OpenLearn unit ["Learn To Code For Data Analysis"](https://www.open.edu/openlearn/science-maths-technology/learn-code-data-analysis/content-section-overview-0?active-tab=description-tab) or as part of the Open University module [Data management and analysis (TM351)](http://www.open.ac.uk/courses/modules/tm351).*

Run the following code cell to grab the data from the datalog as a tabular dataset and preview the first few rows from it:

```python
#roboSim.results_log
import pandas as pd

def get_dataframe_from_datalog(datalog):
    """Generate a datafrome from simulator datalog."""
    df = pd.DataFrame(datalog)
    if not df.empty:
        df = df.melt(id_vars='index').dropna()
        df['index'] = pd.to_timedelta(df['index']-df['index'].min())
    return df

#Grab the logged data into a pandas dataframe
df = get_dataframe_from_datalog(roboSim.results_log)

#Preview the first few raows of the dataset
df.head()
```

With the data in a *pandas* dataframe, we can then use a variety of tools to generate our own charts from it.

One approach is to use the *seaborn* Python package to create a line chart directly from the dataframe.

By convention, *seaborn* is loaded in and referred to as `sns`. The line plot charting function is selected (`sns.lineplot()`) and passed the dataframe (`data=df`). The *index* column values in the dataframe are assigned to the *x*-axis (`x="index"`) and the *value* column values to the *y*-axis (`y="value"`). The line colour is generated from unique values identified in the *variable* column (`hue='variable'`).

If we had additional sensors identified using different *variable* values, such as *ultrasonic*, each sensor would have it's own coloured line trace.

```python
import seaborn as sns
ax = sns.lineplot(x="index", y="value", hue='variable', data=df)
```

Note that in passing parameter values to the `lineplot()` function, we can use either single or double quotes to identify the column name as a string value. So for example, both `hue='variable'`, using single quotes (`'`) and `hue="variable"`, using double quotes (`"`), are equally valid.


As well generating charts using just the *seaborn* package, we can build up charts from several layers of data display. The following chart is constructed from a seaborn `FacetGrid` chart, which generates one line chart per sensor (as identifed from the `row="variable"` parameter), and then overplots individual `x` markers, one per datapoint, using the a `matplotlib` plotting function.

<br/>
<div class="alert-warning"><em>matplotlib</em> is a relatively low level charting library that gives us more control over simple items that make up a chart. The <em>seaborn</em> package is itself built up from simpler <em>matplotlib</em> components.</div>

```python
import matplotlib.pyplot as plt

g = sns.FacetGrid(df, row="variable", height=5, aspect=2, sharey=False)
g = g.map(plt.plot, "index", "value", marker="x");
```

Starting from the left-hand side, each blue `x` point represents a sensor reading. The white background from the grey bars environment shows as 255 and the solid black line shows as 0.


TO DO - how do we clear the datalog [[related issue](https://github.com/innovationOUtside/nbev3devsim/issues/7)]:

- just on the py side?
- on the py side and the js side just from the py side?
- just on the js side from the simulator?
- on both js and py side from the simulator?


## Robots that speak

As well as moving about the simulated world, the robot can also affect the state of the world by making a noise it. In particular, we can get the robot to speak by using a function from the `playsound` package (created as a custom package for use in this module in the javascript Skulpt/Pyhton environment): `playsound.say()`.

Run the following code cell to download the programme to simulator and then run it in the simulator. Does it say hello?!

```python
%%sim_magic roboSim
# Say hello
import playsound

your_name = "TM129 student"
playsound.say("Hello there," + your_name)
```

See if you can modify the name string so that the robot says something that sounds more like *tee, em, one, two, nine* rather than *one hundred and twenty nine*. Run the modified code cell to download the programme to the simulator, and then run the programme there to test it.

Can you also get the robot to say hello to you using your own personal name?


## Robots That Count

That's a good start to gettig the robot to speak, but can we do something more elaborate?

How about counting up from 1 to 5?

The Python `range()` function can be used to generate a iterator over a series of integers that cover a certain range:

```python
range(5)
```

We can use a `for` loop to iterate through the range, displaying each value within the range using a `print()` statement:

```python
for i in range(5):
    print(i)
```

We can also inspect the values by casting the range interator to a list:

```python
list(range(0,5))
```

If we supply just a single value to the `range()` function, as in `range(N)`, it defines a range that spans from $0$ to $N-1$.

```python
M = 5

list(range(M))
```

If we provide two arguments, `range(M, N)`, it defines a range from $M$ to $N-1$:

```python
M = 5
N = 10

list(range(M, N))
```

If we provide *three* arguments, `range(M, N, S)`, it spans a range of integeres from $M$ to $N-1$ with a step value $S$ between them:

```python
M = 0
N = 30
S = 10

list(range(M, N, S))
```

If we set $M=0$, $N=30$ and $S=10$, the first value returned from the range is the intial start value, $0$.

We then add a step of $10$ to get the next value ($10$).

Adding another step of $10$ gives us the next number in the range: $20$.

If we now try to add another $10$, that gives us a total of $30$, which is *outside* the upper range of $N-1$, and so that number os not returned as within the range.


Now let's see if we can get our robot to count up to five in the simulator.

Note that the `playsound.say()` function accepts a *string* value, so if we want it to speak a number aloud we must first cast it to a string; for example, `str(5)`.

*TO DO: maybe define a "say_number()" function? Or may say more robust and error trap / cast non-strings to string values? [Related issue](https://github.com/innovationOUtside/nbev3devsim/issues/37).*

Run the following code cell to download the programme to the simulator and then run it in the simulator. What happens? Does the robot count up to five? 

```python
%%sim_magic roboSim
# I can count...
import playsound

for i in range(5):
    playsound.say(str(i))
```

Although we set the range value as $5$, remember that ths means the robot will count, by default, from $0$ in steps of $1$ to $N-1$. So the robot will count $0, 1, 2, 3, 4$:

```python
list(range(5))
```

### Activity TO DO
In the following code cell, create a `range()` statement that will creates a list of numbers from $1$ to $5$ inclusive. Use a `list()` statement to generate a list from the `range()` statement.

Run the code cell to display the result so you can check your answer:

```python
# Display a list of values [1, 2, 3, 4, 5] created from a single rannge() statement

# YOUR CODE HERE
```

Now create a programme that will cause the simulated robot to count from 1 to 5 inclusive.

Run the cell to download the programme to the simulator, and then run it in the simulator. Does it behave as you expected?

```python
%%sim_magic roboSim
# Count from 1 to 5 inclusive

# ADD YOUR CODE HERE
```

Can you modify your program so that it counts from ten to one hundred, inclusive, in tens (so, *ten, twenty, ..., one hundred*)?


#### Answer

*Click the arrow in the sidebar to reveal the answer.*


We can display a range of values from $1$ to $5$ inclusibe by using a range command of the form `range(M, N)` where `M=1`, the initial value, and $N=5+1$, since the the range spans to a maximum value less than or equal to $N-1$:

```python
list(range(1, 6))
```

We can now create a programme that counts fom one to five inclusive:

```python
%%sim_magic roboSim
# I can count from one to five inclusive...
import playsound

start_value = 1
# To get the desired final value, it must be within the range
# So make the range one more than the desired final value
end_value = 5 + 1

for i in range(start_value, end_value):
    playsound.say(str(i))
```

To count from ten to one hundred in tens, we need to add an additional step value as well as the range limit values:

```python
%%sim_magic roboSim
# I can count from ten to one hundred in tens...
import playsound

start_value = 10
end_value = 100 + 1
step_value = 10

for i in range(start_value, end_value, step_value):
    playsound.say(str(i))
```

## Announcing Bands As The Robot Encounters Them

One of the ways we can use the `playsound.say()` function is to count out the bands as we come across them. To do this, we need to identify when we cross from the white background onto a band.

We can detect the edge og a band by noticing when the sensor value goes from white (a reading of $255$) to a lower value. The following program will detect such a transition and say that it has crossed onto a band, also displaying a print message to announce the fact too.

Reset the robot location in the simulator, run the following cell to download the program to the simulator, and then run it in the simulator. Does it behave as you expected?

```python
%%sim_magic_preloaded roboSim
# Onto a band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity ))
    current_value = colorLeft.reflected_light_intensity
    if previous_value==255 and current_value < 255:
        print('Onto a band...')
        playsound.say("New band")

    previous_value = current_value
```

The programme starts by turning the motors on to drive the robot forward (`tank_drive.on(SpeedPercent(50), SpeedPercent(50))`) and then taking a sample of the light sensor reading (`previous_value = colorLeft.reflected_light_intensity`).

The `while True:` statement creates a loop that repeats until the programme in the simulator is manually stopped. Inside the loop, a new sample is taken of the light sensor reading (`current_value = colorLeft.reflected_light_intensity`). If the robot was on the white background on the previous iteration (`previous_value==255`) and on a band in this iteration ( and then compared to the previous value (`current_value < 255`) then declare that the robot has moved onto a band, via the output display window (`print('Onto a band...')`) and audibly (`playsound.say("New band")`).

The previous value variable is then updated to the current value (`previous_value = current_value`) and the programme goes round the loop again.


You may notice that there is a slight delay between the robot encountering a band and saying that it has done so. This is because it takes some time to create the audio object. If we were to speed up the robot's forward motion, it would quite possibly leave one band and encounter the next before it had finished saying it had entered the first band.

*TO DO: if we queue too many audio messges, things get painful and we need to clear the speech buffer (maybe reload the page?) See [related issue](https://github.com/innovationOUtside/nbev3devsim/issues/8) for how we might start to fx this.*


### Activity - Announce When the Robot Has Left a Band

In the code cell below, the previous robot control program has been modified so that the robot says "on" when it goes onto a band. Modify the programme further so that it also says, "off" when it goes from a band and back onto the white background.

Reset the robot location, donwload the program to the simulator and run it there. Does it behave as you expect?

```python
%%sim_magic_preloaded roboSim
# On and off band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity ))
    current_value = colorLeft.reflected_light_intensity
    if previous_value==255 and current_value < 255:
        print('Onto a band...')
        playsound.say("On")
    
    #YOUR CODE HERE
    
    
    previous_value = current_value
```

### Answer

*Click the arrow in the sidebar to reveal the answer.*


To detect when the robot has left a band, we can check to see if it was on a band on the previous iteration of the `while True:` loop (`previous_value < 255`) and back on the white background on the current iteration (`current_value == 255`).

```python
%%sim_magic_preloaded roboSim
# On and off band...
import playsound

# Drive the robot slowly
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

previous_value = colorLeft.reflected_light_intensity

while True:
    #Uncomment the following line if you want to see the trace of sensor values
    #print('Colour: ' + str(colorLeft.reflected_light_intensity ))
    current_value = colorLeft.reflected_light_intensity
    if previous_value==255 and current_value < 255:
        print('Onto a band...')
        playsound.say("On")
    
    if previous_value < 255 and current_value == 255:
        print('Off a band...')
        playsound.say("Off")
    
    previous_value = current_value
```

### Activity - Count the Bands

Using the previous programmes as inspiration, see if you can write a program that counts each new line as it encounters it, displaying the count to the output window and speaking the count number aloud.

Reset the location of the robot, download your program to the simulator and run it there. Does it work as you expected?

*Hint: you may find it useful to create a counter, initially set to 0, that you increment whenever you enter a band, and then display it and speak it aloud.*

*Another hint: remember, the `playsound()` function must be passed a string, rather than an integer, value.*

```python
%%sim_magic_preloaded roboSim
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

### Answer

*Click the arrow in the sidebar to reveal the answer.*


Using the comment skeleton as a plan for the program, we can reuse statements from the previous programmes wwith just a few additions.

In the first case, we need to add a counter (`count = 0`). Inside the loop, when we detect we are on a new band, increase the counter (`count = count + 1`), display it (`print(count)`) and after casting the count to string value, speak it aloud (`playsound.say(str(count))`).

Note that we could make out output display message a little bit more elaborate by constructing an output message string, such as `print("Band count is" + str(count))`. *(Unfortunately, the simulator does not support the rather more elaborate Python "f-string" formatting method.)*

```python
%%sim_magic_preloaded roboSim
# Count the bands aloud

# Import necessary package(s)
import playsound

# Start the robot moving
tank_drive.on(SpeedPercent(10), SpeedPercent(10))

# Initial count value
count = 0

# Initial sensor reading
previous_value = colorLeft.reflected_light_intensity

# Create a loop
while True:

    # Check current sensor reading
    current_value = colorLeft.reflected_light_intensity
    
    # Test when the robot has entered a band
    if previous_value==255 and current_value < 255:
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

## Summary

In this notebook, you have seen how we can use the simulator to load in a particular background and log and chart sensor values captured as the robot moves over the simulator background both within the simulator and in the notebook environment itself.

You have also seen how we can get the robot to count as we iterate through a range of values.

By keeping track of previous and current sensor values, you have seen how the robot can identify when it encounters a new feature in the simulated world, such as entering or leaving a coloured band. Using the speak functionality, the robot can also alert us to when it encounters a new object.

