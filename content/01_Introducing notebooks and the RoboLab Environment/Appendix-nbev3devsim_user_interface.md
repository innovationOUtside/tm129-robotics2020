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


# `nbev3devsim` Setup Examples

This notebook provides a suite of examples demonstrating different views over the `nbev3devsim` simulator, as well as ways of automating code execution within the simulator.

The notebook also serves to act as informal documentation and an informal test suite.


## Load in the the simulator

Running the follow cell should:

- style the notebook with a two column like display, with the notebook shifted to the left column and the pop-up widget (a JQuery dialog widget) floating over the empty space to the right;
- load in simulator widget.
    
The widget should be draggable and resizable, with widget sizing controls available in its top bar.

The notebook column should be resizable: draggable left and right to change the width.

Known issues:

- if the widget is larger than the display port, the scrolling and layout of the notebook breaks. The fix is to resize the widget to something that fits in the browser view, then scroll the notebook. The notebook is also drag resizable in such cases by clicking and dragging the bottom right hand corner of the notebook column.
- sometimes the simulator view inside the widget gets detached from the widget sides and fails to fill the widget panel effectively. The fix is to click the widget *maximize* button and then the *restore* button.

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```

## Overview of the user interface

The user interface is based around a series of separate display panels. It is designed to try to provide ways of minimising how much of the screen is taken up by controls rather than the actual simulator.

Each panel may contain display elements and/or additional display control.

When a panel is displayed, clicking on the panel title will toggle the display of contents within the panel to *collapse* or *reveal* its content.


### *UI controls*

The (unlabelled) *UI controls* area at the top of the widget provides display toggle button controls for displaying display and simulator control panels.

When a display toggle button is pressed, it will show a dark background and the corresponding panel will be displayed. When the display toggle button has a white background, the corresponding panel will be hidden. 

<!-- #region activity=true -->
Click individual *UI controls* buttons to toggle the display of various other control panels on and off.
<!-- #endregion -->

The *UI controls* are always displayed.

The  and *Simulator world* panel are also generally displayed by default.

Within many of the panels are one or more toggle display switches. The emphasised element is the one that is selected:

- if the toggle button is to the left and shaded grey, the corresponding panel is *hidden*;
- if toggle button is to the right and showing green, the corresponding panel is *shown*.

<!-- #region activity=true -->
Use the *Hide/Show* controls in the *UI controls* panel to show/hide the *Display controls* and *Simulator controls* panels.

Click on the panel labels to collapse/reveal the contents of the corresponding panel.
<!-- #endregion -->

### *Display controls* panel

```
Controlled via *UI controls* panel
```

The *Display controls* panel contains controls for showing and hiding a wide range of panels:

- *Settings*: various robot and simulator configuration settings;
- *Output*: logging console for displaying print and error message from simulator program execution;
- *Noise controls*: controls for applying noise to sensors and motors;
- *Instrumentation*: display sensor and motor values;
- *Sensor arrays*: display image sensor array views;
- *Chart*: display realtime chart of instrumented values.


### *Simulator controls* panel

```
Controlled via *UI controls* panel

Keyboard shortcut: H
```

The *Simulator controls* panel displays various controls for working directly with the simulator:

- display world;
- display positioning;
- display code;
- pen up / down;
- run simulator;
- clear trace.


### *Simulator world* panel

```
Controlled via *Simulator* panel

Keyboard shortcut: W
```

The *World* panel is the simulator world view where the simulated robot performs its actions.

*Known issues: the styling of this is broken. A fix to the layout in `EV3devSim.js` may also be required.*


### *Positioning* panel

```
Accessed via *Simulator* panel
Magics: --positioning / -X
Keyboard shortcut: X
```

The *Positioning* panel provides controls for displaying and positioning the simulated robot within the world view.


### *Code display* panel

```
Accessed via *Simulator* panel
Magics: --code / -D
Keyboard shortcut: D
```

The *Code display* panel will show the program currently downloaded into the simulator.

*Known issues: if you download a new program to the simulator when the `Code display` is open the code is not updated. Closing and opening the display should display the updated program.*


### *Settings* panel

```
Magics: --settings / -Z
Keyboard shortcut: Z
```

The *Settings* panel includes controls for setting:

- robot configuration;
- simulator background (map);
- obstacles configuration;
- collaborative mode (*experimental*).


### *Output* panel

```
Magics: --output / -O
Keyboard shortcut: O
```

The *Output* panel is a terminal display window for viewing printed output and error messages when a program is run.


### *Noise controls* panel

```
Magics: --noisecontrols / -z
Keyboard shortcut: z
```

The *Noise controls* panel displays controls for managing motor and sensor noise that is applied to the robot.


### *Instrumentation* panel

```
Magics: --instrumentation / -i
Keyboard shortcut: i
```

The *Instrumentation* panel displays sensor and motor readings.

*Known issue: I think this is continually updated. It would make sense to only update it if it is visible.*


### *Sensor arrays* panel

```
Magics: --array / -A
Keyboard shortcut: A
```

The *Sensor arrays* panel displays the view of the sensor image arrays.

*Known issue: I think this is continually updated. It would make sense to only update it if it is visible.*


### *Chart* panel

```
Magics: --chart / -c
Keyboard shortcut: c
```

The *Chart* panel displays a realtime updated chart.

*Known issues: need to check that this is only updated if it is displayed.*


### *Robot configurator* panel

```
Accessed via *Settings* panel
```

The *Robot configurator* panel allows you to view, edit, save and load robot configuration files.



### *Obstacles configurator* panel

```
Accessed via *Settings* panel
```

The *Obstacles configurator* panel allows you to:

- edit, save and load obstacle configuration files;
- control display of the walls around the simulated world;
- control display of ultrasound rays.

*Know issues: I don't think the walls are sized/ rendered correctly. Also, the walls don't seem to block robot progress?*

<!-- #region -->
## Magic controls

The notebook code cells are use to pass code to, and control the behaviour of, the widget using several magics:

```python
%sim_magic / %%sim_magic
%%sim_magic_imports
%%sim_magic_preloaded
```

The `%sim_magic` line magic can be used to configure the simulator and display various help messages.

When operating as a cell magic, the magic:
    - inspects and act on magic switches;
    - downloads code from the code cell into the simulator.

The `%%sim_magic_imports` and `%%sim_magic_preloaded` magics generally operate as cell magics, with the exception of running as a line magic to display the code that they use to automatically prefix any code downloaded to the simulator.

For example, a full list of switches can be displayed  by passing the `--help / -h` flag:
<!-- #endregion -->

```python
%sim_magic --help
```

<!-- #region activity=true -->
Run the follow code cells to preview the boilerplate code prepended by the corresponding magic.
<!-- #endregion -->

```python
%sim_magic_imports --preview
```

```python
%sim_magic_preloaded --preview
```

Successfully downloading a program to the simulator is rewarded with an audible alert. To suppress the audible alert, pass the `--quiet / -q` flag in the magic command.

<!-- #region activity=true -->
Download a dummy program with some boilerplate code automatically prepended to it by running the following code cell. Then preview the code downloaded to the simulator via the *UI controls — Simulator controls — Show code* display button.
<!-- #endregion -->

```python
%%sim_magic_imports
pass
```

*Known issues: the `--stop / -s` flag is currently broken.*


One really handy switch is the `--background / -b` switch which lets us load in one of the pre-bundled backgrounds. We *could * selecting these from the settings menu:

```python
%sim_magic --settings
```

Or instead we can select and load a background via a magic switch:

```python
%sim_magic -b MNIST_Digits
```

## Keyboard shortcuts

The long term aim is to duplicate the boolean magic commands using keyboard shortcuts using the same single letter command.

Simulator keyboard shortcuts are only enabled when the mouse cursor is within the bounds of the simulator widget.

At the moment, the following keyboard shortcuts are supported:

- `R` : run the currently loaded program in the simulator;
- `S` : stop the currently running program in the simulator;
- `p` : toggle pen up / down;
- `X` : toggle display of positioning controls.
- `A` : toggle display of sensor image array panel;
- `O` : toggle display of output panel;
- `c` : toggle display of chart panel;
- `i` : toggle display of instrumentation panel;
- `W` : toggle display of simulator world panel;
- `z` : toggle display of simulator noise controls;
- `Z` : toggle display of simulator configuration controls;
- `D` : toggle display of code panel;
- `H` : toggle display of simulator run controls.

*Known issues: the `-S` operation to stop the currently running simulator program does not work.*

For example, in the magic, by default the pen is up but we can set the pen down mode:

```python
%sim_magic --pendown
```

If you move the mouse cursor over the simulator widget, you should also be able to toggle the pen up / pen down mode by pressing the *p* key.

You should be able to toggle the various panel displays by pressing the appropriate keyboard shortcut key whilst the mouse cursor is over the widget.


## Controlling the simulator user interface configuration

If you inspect the simulator interface, you will see it contains a range of controls for hiding and revealing various parts of the user interface (the *Hide/Show* toggle buttons).

By default, the *Simulator controls* and *Simulator World* are displayed:

```python
%sim_magic
```

Several magic switches are defined that control the display of simulator display panels, typically using the same single character shortcut as the keyboard shortcut controls:

- `--output / -O`: Show output;
- `--chart / -c`: Show chart;
- `--instrumentation / -V`: Show sensor and motor values;
- `--array / -A`: Show sensor array;
- `--noisecontrols / -z`: Show sensor and motor noise controls;
- `--positioning / -X`: Show positioning controls
- `--worldcontrols / -Z`: Show world controls
- `--hide / -H`: Hide simulator controls
- `--world / -W`: Hide world

So for example, we can configure the simulator to show only the world display among the optional display elements by suppressing the display of the simulator controls (all other panels are hidden by default):

*Known issues: if the obstacles or robot config panels were opened manually, they will remain open.*

```python
%sim_magic -H
```

We can hide the world display (at the bottom of the widget), by passing just the `-W` flag:

```python
%sim_magic -W
```

We can pass multiple flags separately (`-W -H`) or compounded (`-WH`):

```python
%sim_magic -WHZ
```

The display switches thus provide us with a means of scripting how the simulator widget controls are displayed for any given activity.

For example, we might want to configure the simulator to show the sensor image array and the noise controls, but hide most of the other show/hide controls to free up screen real estate (note that the world is displayed unless we explicitly hide it):

```python
%sim_magic -Az
```

Run the following code cell to toggle through the various cell displays:

```python
import time

for i in "HOcVAzZW":
    %sim_magic -$i
    time.sleep(2)
```

We can also script values for the various numerical sliders that appear in the simulator user interface:

- `--xpos, -x`: x co-ord config;
- `--ypos, -y`: y co-ord config;
- `--angle, -a`: Angle config;
- `--sensornoise, -N`: Sensor noise, 0..128;
- `--motornoise, -M`: Motor noise, 0..500.



We can set just a single co-ordinate value:

```python
%sim_magic --positioning -y 450
```

Or multiple values:

```python
%sim_magic -X -x 200 -y 700 -a 150
```

## Downloading programs to the simulator

We can download a program to the simulator by prefixing the code cell with one of the simulator magics. The different magics prepend various bits of boilerplate code to the program before downloading it.

When a program is downloaded, there is an audible alert:

```python
%%sim_magic
pass
```

We can download and run a program automatically (`--autorun / -R`). Note that the run status indicator changes colour from red (not running) to green (running) as the program runs and then back to red when the program completes.

```python
%%sim_magic -R
import time
time.sleep(3)
```

We can view the downloaded code by opening the *Code display* panel:

```python
%sim_magic -D
```

Trying to run a broken program in the simulator will give an audible warning:

*Known issue: there is no way to disable this at the moment.*

```python
%%sim_magic -R -q -O

broken
```

We can print to the *Output* display panel.

For example, let's hide the *Simulator controls* and *Simulator world* panels but display the *Output* window and then download and run a program that writes to it:

```python
%%sim_magic -OHW -R
import time
for i in range(3):
    print("Hello number {}".format(i))
    time.sleep(1)
```

We can get a downloaded program to talk...

```python
%%sim_magic_preloaded -R

say("hello")
```

When driving the robot, we can enable a "pen down" feature to leave a trace showing the path followed by the robot.

For example, drive forward a short way without the pen down:

```python
%%sim_magic_preloaded -x 100 -y 800 -R 

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)

```

Now drive forward with the pen down (`--pendown / -p`):

```python
%%sim_magic_preloaded -x 100 -y 820 -R -p

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)
```

If we drive forward again, the trace will remain in place.

For example, change the pen colour ( `--pencolor / -P`) and drive forwards again:

```python
%%sim_magic_preloaded -x 100 -y 840 -R -p -P green

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)
```

*Known issue: the pen colour selector widget is not enabled if the pen down toggle is selected from the magic.*


Alternatively, we can clear the trace (`--clear / -C`) and then drive forward, again with the pen down and a selected color:

```python
%%sim_magic_preloaded -x 100 -y 800 -R -p -C -P orange

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)
```

You can suppress the audible download alert by passing the `--quiet, -q` switch:

```python
%%sim_magic -q
pass
```

### Using the *Simulator controls*

```
Magics: --hide / -H
Keyboard shortcut: H
```

The *simulator controls* panel provides manual user interface controls for controlling the simulator and managing the display of several panels related to simulator operation:

- toggle display of the simulator world;
- toggle display of the positioning controls;
- toggle display of the code panel showing the currently downloaded program;
- toggle the pen up / pen down state;
- select the pen color;
- clear pen traces from the current simulator world view;
- start (*Run*) / stop the execution of the program currently downloaded to the simulator in the simulator; a status light (*red* on stop, *green* when running) displays the current run state;

```python
%sim_magic -W
```

### Viewing sensor and motor *Instrumentation*

```
Magics: --instrumentation / -i
Keyboard shortcut: i
```

The *Instrumentation* panel provides information regarding sensor and motor readings.

- `LeftMotor` / `RightMotor` report tachometer counts for each motor;
- `Sensor1` / `Sensor2` report left and right light sensor values as follows: reflected light percentage for the red component range 0..100; average reflected light percentage over all three RGB components range 0..100; 3-tuple of RGB values, each in range 0..255;
- `Ultrasonic`: distance reading to obstacle;
- `Gyro`: the *angle* in degrees since the sensor was initialised and the *rate* at which the sensor is rotating, in degrees/second.

```python
%sim_magic -i -WH
```

Run the following code cell to drive the robot over the *Testcard* background and see how the sensor values update as the robot moves.

```python
%%sim_magic_preloaded -i -HR -b Testcard

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)
```

### Using *Sensor arrays*

```
Magics: --array / -A
Keyboard shortcut: A
```

The sensor image arrays provide a view of what the sensor can see at the pixel level.

Displaying the sensor arrays and hiding the world provides opportunities for exploration style robot programming challenges.

```python
%sim_magic -A -WH -b MNIST_Digits
```

### Using *Noise controls*

```
Magics:
    --noisecontrols / -z 
    --sensornoise / -N  [0..128]
    --motornoise / -M  [0..500]
    
Keyboard shortcut: z
```

The *Noise controls* provide a numerical slider to set the noise level across both motors (range 0..500) and both light sensors (range 0..128).

```python
%sim_magic -z -WR
```

Noise levels can be set on the light sensors via the `--sensornoise / -N` switch:

```python
%sim_magic -zWR --sensornoise 100
```

```python
%sim_magic -zWR --motornoise 100
```

<!-- #region activity=true -->
Drag and drop the robot around the plain white background, observing the light sensor instrumentation values and the sensor array view for different levels of light sensor noise.
<!-- #endregion -->

```python
%%sim_magic_preloaded -iAHR -x 100 -b Empty_Map -N 100
```

<!-- #region activity=true -->
Run the following code cell to download a program that will drive the robot forward a short way:
<!-- #endregion -->

```python
%%sim_magic_preloaded -HR -R -x 100 -y 700 -M 0

tank_drive.on_for_seconds(SpeedPercent(50),
                          SpeedPercent(50), 2)
```

<!-- #region activity=true -->
Now run the program several times in the presence of sensor noise:
<!-- #endregion -->

```python
import time
%sim_magic -RC -x 100 -y 700 -M 100 -p -P red
time.sleep(3)

%sim_magic -R -x 100 -y 700 -M 200 -p -P orange
time.sleep(3)

%sim_magic -R -x 100 -y 700 -M 300 -p -P green
```

### Using the Live *Chart*

```
Magics: --chart / c
Keyboard shortcut: c
```

The live *Chart* panel displays a dynamic line chart that can be configured to display selected instrumentation data traces logged to the output in a specific way.

Supported chart traces:

- *colour*;
- *Left light* and *Right light* sensor values;
- *Ultrasonic* distance;
- *Gyro* angle;
- *Left wheel* and *Right wheel* tacho counts.

```python
%sim_magic -c -WH
```

