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

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds
%load_ext nbev3devsim
%load_ext nbtutor
```

# 3 Robot sensors and data logging

In this notebook, you will start to learn about how to work with one of the several sensors that are available in our robot simulator, as well as how to collect data from them for further analysis or visualisation.


## 3.1 Previewing the simulated robot state from a notebook code cell

As well viewing the sensor state via the simulator user interface, we can also review it in the notebook itself.

Run the following command rto create a reference to an object that lets us look up the state of the robot in the default `roboSim` simulator:

```python
robotState = eds.RobotState(roboSim)
```

We now need to synchronise the data by running a command of the following form *in its own code cell*:

```python
robotState.update()
```

and then preview the data via a separate code cell:

```python
robotState.state
```

The data is returned as a Python dictionary which we can reference into to view specific data values. For example, the `x` coordinate: 

```python
robotState.state['x']
```

Try moving the simulated robot in the simulator by dragging it or moving it by changing the x coordinate and clicking the *Move* button. Alternatively, run the follow code cell to reset the *x* coordinate location of the robot:

```python
%sim_magic -x 500
```

If you run the following cell, you will notice that the value as viewed from the notebook has not been updated.

```python
robotState.state['x']
```

Instead, you must run the `eds.sim_get_data(roboSim)` command *in its own code cell* and then run the `eds.sim_data()` *in a sepaarate code cell* to view the updated value.

```python
robotState.update()
```

```python
robotState.state['x']
```

<!-- #region hideCode=true hidePrompt=true -->
## 3.2 Investigating the light sensor

One of the things that distinguishes robot control programmes from many other sorts of programme is that robots typically have a range of *sensors* available to them, and readings taken from these sensors can be referenced from within the robot control programme.

To begin with, you will experiment with a simulated downward light sensor that can take readings from the simulator world background as it drives over it.
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
The simulated sensor we are using is based on the Lego light sensor:

![*A Lego light sensor. This is a custom packaged sensor with a Technic lego connector on the base. Two small lenses are visible in the front face of the sensor brick. A large clear lens is the light sensor itself. Below it is a lens that can be used as a light source to illuminate a surface. The light sensor then measures light reflected from the surface rather than ambient light levels.](../images/ev3_light_sensor.png)

The light sensor measures light across three channels, *red*, *green* and *blue*. The light sensor returns information about the reflected light in various ways.

Some of these are referenced in the robot control programs as follows:

- `.rgb`: as a list of raw values, `[red, green, blue]`, each value represented an integer in the range 0...255;
- `.reflected_light_intensity`: an integer in the range 0...255 representing the red component of the full RGB response;
- `.reflected_light_intensity_pc`: a floating point number in the range 0...100.0 representing the reflected light intensity as a percentage;
- `.full_reflected_light_intensity`: a floating point number in the range 0...100.0 representing the reflected light intensity averaged over all three RGB channels, as a percentage;
- `.color` / `.color_name`: a colour value in the range 1...7 (representing: black, blue, green, yellow, red, white, brown), or the corresponding colour name.

We can remind ourselves how the sensors are defined by previewing the boilerplate code added by the magics:
<!-- #endregion -->

```python
%sim_magic_preloaded -v
```

In this case, we have defined the left color sensor as `colorLeft` so within a robot control program we might lookup a sensor value as `colorLeft.reflected_light_intensity` or `colorLeft.reflected_light_intensity_pc` for example. 


We can also preview the values in the notebook (after data synchronisation) via the `robotState.state` dictionary using the following keys:

- `left_light_raw / right_light_raw` for the raw RGB values
- `left_light / right_light` for the `reflected_light_intensity` values
- `left_light_pc / right_light_pc` for the `reflected_light_intensity_pc` values, and
- `left_light_full / right_light_full` for the `full_reflected_light_intensity` values.

So for example, `robotState.state['left_light']`.

We can also create a simple function to help (you will learn more about functions in a later notebook).

```python
def report_robot_left_sensor():
    """Print a report of the left light sensor values."""
    
    print(f"""
RGB: {robotState.state['left_light_raw']}
Reflected light intensity: {robotState.state['left_light']}
Reflected light intensity per cent: {robotState.state['left_light_pc']}
Full reflected light intensity (%): {robotState.state['left_light_full']}
""")
```

Calling this function displays a report of the currently synchronised sensor values:

```python
report_robot_left_sensor()
```

<!-- #region hideCode=true hidePrompt=true -->
## 3.3 Activity — Getting started with the light sensor

In this activity you will explore the range of values returned by the light sensor.

Load the *Grey_bands* background into the simulator and then click and drag the simulated robot over each coloured band.
<!-- #endregion -->

```python activity=true
%sim_magic -b Grey_bands
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
Alternatively use the simulator magic to move it the various locations `-y 500` and `-x` taking values in `[675, 875, 1275, 1675, 2075]`.

Record the sensor values displayed in each case. You can identify these values:

- from the simulator widget user interface by enabling the *Show sensor values* control;
- from the simulator widget output window if you run a program to print the values there;
- from a notebook code cell by synchronising the robot state and then displaying the required data values.

What value does the sensor give when the robot is placed on each of the white background? What sensor values are returned for when the light sensor is over the light grey, medium grey, dark grey and black bands?
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Grey_bands -y 500 -x 875 -R

print('RGB', colorLeft.rgb)
print('Reflected light intensity', colorLeft.reflected_light_intensity)
print('Reflected light intensity per cent', colorLeft.reflected_light_intensity_pc)
print('Full reflected light intensity (%)', colorLeft.full_reflected_light_intensity)
print('Color', colorLeft.color)
print('Color name', colorLeft.color_name)

```

<!-- #region activity=true -->
We can also retrieve and display sensor values from the `robotState.state` dictionary and then display a corresponding report:
<!-- #endregion -->

```python activity=true
robotState.update()
```

```python activity=true
report_robot_left_sensor()
```

<!-- #region student=true -->
*Double click this cell to edit it and add your recorded sensor values here:*

- white background:
- light grey band: 
- medium grey band:
- dark grey band: 
- black band: 
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
Now load the *Rainbow_bands* background into the simulator and then click and drag the simulated robot over each coloured band (or move it to the various locations `-y 500` and `-x` taking values in `[675, 875, 1075, 1275, 1475, 1675, 1875, 2075]`.
<!-- #endregion -->

```python activity=true
%sim_magic -b Rainbow_bands
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
What value does the sensor give when the robot is placed on each of the coloured backgrounds?
<!-- #endregion -->

<!-- #region student=true -->
*Double click this cell to edit it and add your recorded sensor values here:*

- white background:
- light grey band: 
- medium grey band:
- dark grey band: 
- black band: 
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
#### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
I get the following readings for the reflected light intensity readings from the light sensor:

- white background: `100`
- light grey band: `~86`
- medium grey band: `~82`
- dark grey band: `~50`
- black band: `0`

There is some "noise" in the form of intermediate values as the robot goes into and leaves the band. This is because the sensor has a "width" so it may be averaging readings where part of the sensor is over the white background and part of it is over the coloured band.
<!-- #endregion -->


Do you notice anything strange about the sensor values, particularly when the robot is close to the edge of a particular band?

<!-- #region hideCode=true hidePrompt=true -->
## 3.4 Logging data from the light sensor

In the simulator, the *Grey_bands* background displays a white background overlaid by four grey bars of different in intensity, ranging from a pale grey to black.

The following program could be used to drive the simulated robot over the background, logging the light sensor data as as it does so:

```python
# import require components
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor

# Create tank drive and color sensor references
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

# Run the following loop forever
while True:
    # Log the colour sensor data
    print('Colour: ' + str(colorLeft.reflected_light_intensity_pc ))
```

We can also use the `%%sim_magic_preloaded` magic to preload the drive and sensor configurations and references to minimise the clutter in *our* code, whilst remembering that it is still required for the programme to run, and will be loaded in automatically by the magic.
<!-- #endregion -->

```python hideCode=true hidePrompt=true
%%sim_magic_preloaded --background Grey_bands -p

# Start the robot driving forwards using the preloaded tank_drive definition
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

while True:
    print('Colour: ' + str(colorLeft.reflected_light_intensity_pc ))
```

As well as controlling program execution in the simultor  using the simulator user interface controls, we can also control program execution via the simulator magics. For example, if we include a `--autorun/-R` switch when downloading a program, it will automatically run in the simulatot once it has been downloaded.

We can also use the same flag on its own with the `%sim_magic` line magic: `%sim_magic -R` or `%sim_magic --autorun`.

Calling the line magic with the `--stop/-S` flag will stop any program currently running in the simulator.

```python
# Start the program running in the simulator
%sim_magic -R
```

```python
# Stop the program running in the simulator
%sim_magic --stop
```

<!-- #region hideCode=true hidePrompt=true -->
Run the previous code cell to download the program to the simulator and then run it in the simulator, stopping the program using the simulator *Stop* button when the robot has gone past the final black line.

As the programme runs, you should notice that that a sequence of logged data values from the sensor are displayed in the output window. If you scroll up through the display in that window you should notice that the sensor values changed as the robot crossed over each grey line.
<!-- #endregion -->

## Viewing the Logged Data Using a Chart Display

As well as taking the sensor readings directly, we can also read them from a chart created in real time from the logged data.

By monitoring the output display for print messages that log sensor outputs using a particular message format, particular messages can be automatically parsed and used to extract data values so that they can be displayed on a dynamically updated line chart.

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Activity

Enable the inline interactive simulator data charter by clicking the *Show chart* check box in the simulator and then ensure that the the *Colour* trace checkbox.

Also reset the start location of the robot either by dragging it back to the start or clicking the *Move* button to reset the original location for the current simulator setup.

The following magic commands will also reset the simulator (the `--chart/-c` switch displays the chart; the `--move/-m` switch moves the robot) before also running the program.
<!-- #endregion -->

```python
%sim_magic -c -m
```

<!-- #region hideCode=true hidePrompt=true activity=true -->
Run the simulator programme again until the robot has crossed over all the lines, observing how the chart is updated with the live sensor values. Can you see where the robot encounters the different coloured bands? What values are recorded for each band?
<!-- #endregion -->

```python activity=true
# Start the program running in the simulator
%sim_magic -R
```

```python activity=true
# Stop the program running in the simulator
%sim_magic -S
```

<!-- #region activity=true -->
From the chart, can you read off the values for each band?
<!-- #endregion -->

<!-- #region student=true -->
*Double click this cell to edit it and add your recorded sensor values here:*

- white background:
- light grey band: 
- medium grey band:
- dark grey band: 
- black band: 
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
### Answer

*Click the arrow in the sidebar or run this cell to reveal the answer.*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true activity=true -->
The following diagram shows the result of showing the real time data logging chart:

![The simulator Data log window, with a graph showing sensor data. The graph has a vertical axis with a scale that runs from 0 to 250, and a horizontal axis that runs from 0 to 400. A line chart is plotted showing successive sensor readings. Reading the graph from left (the first sensor reading) to right (the last sensor reading), the line is horizontal at a y-value of 255 until an x value of about 100, followed by a drop to about 220 until about x=145, at which point it climbs steeply back up to y=255, remaining at that level until about x=190. There is a further sharp drop to about (x, y) equal to (190, 210), then back up to to 255 at about x=225, until another edge at about x=280 down to (280, 130); the chart then goes back up from about (320, 130) to (321, 255), then down to y=0 at about x=360, staying then until x is almost 410, at which point the line climbs back up to 255 , stays there for a short while, and the trace ends.](../images/Section_00_03_-_charting.png)


As the robot progresses across the bands, the bars that it encounters get progressively darker, so the sensor readings reduce. Between the bands, as the robot crosses the white background, the sensor reading go back up to their initial, maximum reading.

If you hover your cursor over the chart, all the recorded trace values at that x-position on the chart are displayed. These are the values that were recorded and displayed, taken from the midpoint of the chart, when I ran the experiment.


- white background: `100`
- light grey band: `86.27451`
- medium grey band: `82.7451`
- dark grey band: `50.19608`
- black band: `0`

*(You may have noticed that the simulation running in a slightly more "stuttery" way than when the chart is not displayed as your computer has to do more work in terms of dynamically updating the chart.)*

*TO DO - should we experiment with generating text descriptions of charts, eg as per [Automatically Generating Accessible Text Descriptions of Charts](https://blog.ouseful.info/2016/04/29/first-thoughts-on-automatically-generating-accessible-text-descriptions-of-ggplot-charts-in-r/)?*
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
## Viewing the Logged Data - Uploading the Logged Data to the Notebook

As well as inspecting the data log values in the simulator output window and via the embedded datalog chart, we can also export the logged data from the simulator into the Python enviornment used by the notebook. This then allows us to analyse and chart the data within a complete Python environment.

__TO DO - should we have some magic to get data out of the datalog?__

The following code cell shows how to access the datalog from the simulator in the notebook's Python environment. The *pandas* package is a very powerful package for working with tabular data.

*You can learn more about using pandas from the OpenLearn unit ["Learn To Code For Data Analysis"](https://www.open.edu/openlearn/science-maths-technology/learn-code-data-analysis/content-section-overview-0?active-tab=description-tab) or as part of the Open University module [Data management and analysis (TM351)](http://www.open.ac.uk/courses/modules/tm351).*

Run the following code cell to grab the data from the datalog as a tabular dataset and preview the first few rows from it:
<!-- #endregion -->

```python hideCode=true hidePrompt=true
#Grab the logged data into a pandas dataframe
data = roboSim.results_log

#Create a tabular dataframe from the data
df = eds.get_dataframe_from_datalog(data)

#Preview the first few rows of the dataset
df.head()
```

<!-- #region hideCode=true hidePrompt=true -->
With the data in a *pandas* dataframe, we can then use a variety of tools to generate our own charts from it.

One approach is to use the *seaborn* Python package to create a line chart directly from the dataframe.

By convention, *seaborn* is loaded in and referred to as `sns`. The line plot charting function is selected (`sns.lineplot()`) and passed the dataframe (`data=df`). The *index* column values in the dataframe are assigned to the *x*-axis (`x="index"`) and the *value* column values to the *y*-axis (`y="value"`). The line colour is generated from unique values identified in the *variable* column (`hue='variable'`).

If we had additional sensors identified using different *variable* values, such as *ultrasonic*, each sensor would have it's own coloured line trace.
<!-- #endregion -->

```python hideCode=true hidePrompt=true
# Load in the seaborn charting package
import seaborn as sns

# Generate a line chart from the datalog dataframe
ax = sns.lineplot(x="index",
                  y="value",
                  # The hue category defines line color
                  hue='variable',
                  data=df)
```

<div class='alert alert-warning'>If you have run the robot programme several times, the datalog will contain data from each of the runs. To ensure the datalog only contains data from a particular run, run the command `roboSim.clear_datalog()` in a notebook code cell before running the programme in the simulator, run the programme in the simulator to collect the data, and then grab them data into a datframe</div> 

```python
# Running this code cell will clear the robot's datalog
roboSim.clear_datalog()
```

<!-- #region hideCode=true hidePrompt=true -->
Note that in passing parameter values to the `lineplot()` function, we can use either single or double quotes to identify the column name as a string value. So for example, both `hue='variable'`, using single quotes (`'`) and `hue="variable"`, using double quotes (`"`), are equally valid.
<!-- #endregion -->

<!-- #region hideCode=true hidePrompt=true -->
As well generating charts using just the *seaborn* package, we can build up charts from several layers of data display. The following chart is constructed from a seaborn `FacetGrid` chart, which generates one line chart per sensor (as identifed from the `row="variable"` parameter), and then overplots individual `x` markers, one per datapoint, using the a `matplotlib` plotting function.

<br/>
<div class="alert-warning"><em>matplotlib</em> is a relatively low level charting library that gives us more control over simple items that make up a chart. The <em>seaborn</em> package is itself built up from simpler <em>matplotlib</em> components and provides "higher level" charting functions that allow us to create different chart types in a natural way from *pandas* dataframes..</div>
<!-- #endregion -->

```python hideCode=true hidePrompt=true
import matplotlib.pyplot as plt

# A FacetGrid is a facetted display arranged in a grid
g = sns.FacetGrid(df,
                  row="variable", 
                  height=5,
                  # Set the aspect ratio of the grid
                  aspect=2,
                  # Declare whether we want common y-axes
                  sharey=False)

g = g.map(plt.plot, "index", "value", marker="x");
```

<!-- #region hideCode=true hidePrompt=true -->
Starting from the left-hand side, each blue `x` point represents a sensor reading. The white background in the grey bars environment shows as 100 and the solid black line shows as 0.
<!-- #endregion -->
