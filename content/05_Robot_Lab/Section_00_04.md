---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
```
# 4 Where am I?


One of the main problems a robot has is locating itself in its environment: the simulated robot doesn't know where it is in the simulated world. Within the simulator, some `x` and `y` co-ordinate values are used by the simulator to keep track of the simulated robot's location, and an angle parameter records its orientation. This information is then used to draw the robot on the background canvas.

Typically when using a simulator, we try not to cheat by providing the robot direct access to simulator state information. That would be rather like you going outside, raising your arms to the sky, shouting *where am I?* and the universe responding with your current location.

Instead, we try to ensure that the information on which the robot makes its decision come from it's own internal reasoning and any sensor values it has access to.

At this point, we could create a magical "simulated-GPS" sensor, that allows the robot to identify its location from the simulator's point of view; but in the real world, we can't always guarantee that external location services are available. For example, GPS doesn't work indoors or underground, or even in many cities, where line of sight access to four or more GPS satellites is not available.

Instead, we often have to rely on other sensors to help us identify our robot's location at least in a relative sense to where it has been previously.

So that's what we'll be exploring in this notebook...


## 4.1 Activity: Logging Motor Tachometer / "Rotation Sensor" Data


We can get a sense of how far the robot has traveled by logging the `.position` of each motor. Inside a real motor, a rotary encoder is used to detect rotation of the motor. When the motor turns in one direction the count goes up, when it turns in the other, it goes down.

We'll be looking at the logged data using notebook tools, so let's take the precaution of clearing the datalog:

```python
roboSim.clear_datalog()
```

As well as each sensor value, we will also capture the simulator "clock time". When running the simulator, you may have noticed that the simulator sometimes seems to slow down, perhaps because your computer processor is interrupted by having to commit resource to some other task. Inside the simulator, however, is an internal clock that counts simulator steps. Depending on how much work the simulator has to do to calculate updates in each step of the simulator run, this may take more or less "real time" as measured by a clock on your wall (or more likely, the clock on your mobile phone!). By logging the simulator step time, we can create a more accurate plot of the sensor values at each step of simulator time, irrespective of how long that step to to calculate in the real world.

<!-- #region tags=["alert-success"] -->
In his book "The New Dark Age", artist James Bridle describes the evolution of weather forecasting based on mathematical models:

>In 1950, a team of meteorologists assembled at Aberdeen in order to perform the first automated twenty-four-hour weather forecast.... For this project, the boundaries of the world were the edges of the continental United States; a grid separated it into fifteen rows and eighteen columns. The calculation programmed into the machine consisted of sixteen successive operations, each of which had to be carefully planned and punched into cards, and which in turn output a new deck of cards that had to be reproduced, collated, and sorted. The meteorologists worked in eight-hour shifts, supported by programmers, and the entire run absorbed almost five weeks, 100,000 IBM punch cards, and a million mathematical operations. But when the experimental logs were examined, von Neumann, the director of the experiment, discovered that the actual computational time was almost exactly twenty-four hours. 'One has reason to hope’, he wrote, that 'Richardson's dream of advancing computation faster than the weather may soon be realised'.

*Historical note: Lewis Fry Richardson was an early pioneer of weather forecasting, whose story is also summarised by Bridle.*

As Bridle observes, the number crunching required to perform a weather forecast requires the solution of lots of complex mathematical equations, so much so that the earliest computers might take days to make a 24 hour weather forecast. If you're in the habit of checking online weather reports just before you set out for the day, they wouldn't be much use if they took the next three days to compute. Although our simulator is a simple one, at times it may still take more computational resource than is available to the programme for it compute a single second of time in the simulated world in less than a second of real world time.

Reference: `BRIDLE, J. (2018). New Dark Age: Technology, Knowledge and the End of the Future. Verso Books.`
<!-- #endregion -->

The following programme logs the position count as we drive the robot forwards, backwards, wait awhile, then turn on the spot slowly one way, quickly the other. I have also instrumented it so that the simulated robot says aloud what it is about to do next as the programme progresses.

With the simulator chart display enabled, and the *Left_wheel* and *Right_wheel* traces selected, download and run the programme.

Observe what happens to the wheel position counts as the robot progresses.

```python
%%sim_magic_preloaded -c -p -b Empty_Map -x 250 -y 550
from playsound import say

import ev3dev2_glue as glue

tank_steering= MoveSteering(OUTPUT_B, OUTPUT_C)

tank_steering.left_motor.position = str(0)
tank_steering.right_motor.position = str(0)

#tank_steering.on(DIRECTION, SPEED)

import time


def datalogger():
    """Simple datalogging function."""
    print('Wheel_left: {} {}'.format(tank_steering.left_motor.position, glue.get_clock()))
    print('Wheel_right: {} {}'.format(tank_steering.right_motor.position, glue.get_clock()))

#Move forwards quickly
say("Forwards quickly")
tank_steering.on(0, 40)
for i in range(20):
    time.sleep(0.05)
    datalogger()

# Move forwards slowly
say("Forwards slowly")
tank_steering.on(0, 5)
for i in range(40):
    time.sleep(0.05)
    datalogger()

# Move backwards at intermediate speed
say("Backwards medium")
tank_steering.on(0, -20)
for i in range(20):
    time.sleep(0.05)
    datalogger()

#Stop awhile
say("Stop awhile")
tank_steering.on(0, 0)
for i in range(20):
    time.sleep(0.05)
    datalogger()

    
#Turn slowly on the spot
say("On the spot")
tank_steering.on(-100, 5)
for i in range(20):
    time.sleep(0.05)
    datalogger()
    
#Turn more quickly on the spot the other way
say("And back")
tank_steering.on(100, 50)
for i in range(20):
    time.sleep(0.05)
    datalogger()

say("All done")
```

The chart display in the simulator uses "sample number" along the horizontal x-axis to the log the data. This can result in some misleading traces as we can currently only add one sensor value to each sample.

To plot the data more accurately, we need to plot the samples as a proper time series, with the sample timestamp as the x-coordinate.

We can do that by charting the data from the datalog directly in the notebook.

Retrieve the data from the data log, and preview it:

```python
#Grab the logged data into a pandas dataframe
data = roboSim.results_log

#Create a tabular dataframe from the data
df = eds.get_dataframe_from_datalog(data)

#Preview the first few rows of the dataset
df.head()
```

Now we can chart the data:

```python
# Load in the seaborn charting package
import seaborn as sns

# Generate a line chart from the datalog dataframe
ax = sns.lineplot(x="time",
                  y="value",
                  # The hue category defines line color
                  hue='variable',
                  data=df);
```

Here's a stylised impression of what my chart looked like:

![](../images/position_time.png)

You'll notice that I have added some vertical grey lines to my chart to indicate different areas of the chart, as well as some simple labels identifying each area.

Annotating charts can often help us make more sense of them when we try to read read them. In creating such charts there is often a balance between making a "production quality" chart that you could share with other people as a part of a formal report (or formal teaching materials!) and a "good enough for personal use" feel for your own reference. 

In this regard, you may also notice the that the chart shown above has an informal, stylised feel to it. The chart really was created from the data I collected, but I then styled it using an XKCD chart theme to differentiate it from the charts generated within the notebook.

<!-- #region tags=["optional-extra"] heading_collapsed=true -->
#### Create your own annotated chart

*Click on the arrow in the sidebar to reveal how to create the annotated chart*
<!-- #endregion -->

<!-- #region tags=["optional-extra"] hidden=true -->
I used the following code to create the annotated chart. I manually set the horizontal x-axis values where I wanted the the the vertical lines to appear. 
<!-- #endregion -->

```python tags=["optional-extra"] hidden=true
# manually set x-axis co-ordinates for vertical lines
forward_fast = 0.3
forward_slow = 1.6
backwards_medium = 4.1
stop_awhile = 5.5
on_the_spot = 6.7
and_back = 8.0

# We need some additional tools from matplotlib
import matplotlib.pyplot as plt

# I am using the xkcd theme
# This gives the chart an informal
# or "indicatiive example" feel
with plt.xkcd():
    # Generate a line chart from the datalog dataframe
    ax = sns.lineplot(x="time",
                      y="value",
                      # The hue category defines line color
                      hue='variable',
                      data=df)

    # Move the legend outside the plotting area
    # The prevents it from overlapping areas of the plot
    ax.legend( bbox_to_anchor=(1.0, 0.5))

    o = 0.3 #offset text from line
    line_colour = 'lightgrey'

    def plot_line_label(x, label):
        """Annotate boundaried areas."""
        # Create a vertical line
        plt.axvline(x, c=line_colour)
        # Create a text label
        plt.text(x+o, 20, label)

    # Add lines and labels to the chart
    plot_line_label(forward_fast, 'Fwd\nfast')
    plot_line_label(forward_slow, 'Fwd\nslow')
    plot_line_label(backwards_medium, 'Back\nmed')
    plot_line_label(stop_awhile, 'Stop\nawhile')
    plot_line_label(on_the_spot, 'On the\nspot')
    plot_line_label(and_back, 'And\nback');

    # We can save the image as a file if required
    # Increase the figure size
    #plt.figure(figsize=(12,8))
    # Nudge the margins so we don't cut off labels
    #plt.subplots_adjust(left=0.1, bottom=0.1,
    #                    right=0.7, top=0.8)
    # Save the image file
    #plt.savefig('position_time.png')

```

<!-- #region activity=true -->
### Optional Activity

How do the position counts vary for each wheel if the robot is  driving forwards in a gentle curve, or a tight turn?

For example, we might create such turns using the following steering commands:

```python
# Graceful forwards left
tank_steering.on(-30, 20)

# Tighter turn forwards and to the right
tank_steering.on(-30, 20)
```

Feel free to make your own predictions, or run a program, grab the data and analyse it yourself. If you do run your own experiment(s), remember to clear the datalog before running your data collecting code in the simulator...
<!-- #endregion -->

## Measuring How Far The Robot Has Traveled

The wheel `position` data corresponds to an angular measure, which is to say, how far the wheel has turned.

Use the following programme to drive the robot over a fixed number of rotations and observe how the position count increases. Based on your observations, make a note of what you think the position count actually measures.

```python
%%sim_magic_preloaded

from playsound import say

tank_steering= MoveSteering(OUTPUT_B, OUTPUT_C)

def reporter(last_position=0):
    position = int(tank_steering.left_motor.position)
    diff = position - last_position
    print('Current {}, diff {}'.format(position, diff))
    say('Diff {}'.format(diff))
    return position

tank_steering.on_for_rotations(0, 10, 1)
last_position = reporter()

tank_steering.on_for_rotations(0, 10, 1)
last_position = reporter(last_position)

tank_steering.on_for_rotations(0, 10, 1)
reporter(last_position)
```

<!-- #region student=true -->
*Based on your observations of position counts for number of wheel rotations traveled, what do you think the position value measures. Bear in mind that the simulation, like the real world, may have sources of noise that affect the actual values recorded, rather than "ideal" ones.*

*Record your impressions here.*
<!-- #endregion -->

<!-- #region activity=true -->
### My Observations

*Click the arrow in the sidebar to reveal my observations.*
<!-- #endregion -->

When I ran the programme, I got counts between 365 and 380 for each rotation, depending in part on the speed I set the wheels to run at.

The simulator actually runs in steps, with 30 steps per simulated second. This means that at 20% speed, the wheel will turn approximately 6 to 7 degrees each step. By the time the simulator detects that the wheel has reached *at least* 360 degrees (i.e. completed one rotation), it may already have exceeded that amount of turn; so the stopping condition for the `.on_for_rotations` function, which is based on observing the turned angle, may actually stop the motors after more than one rotation.

So notwithstanding the values we get for the position count after a single rotation, the position is actually measured in degrees.

<!-- #region activity=true -->
## Activity — Are We There Yet?

In this activity, you will experiment with driving the robot over a fixed distance.

Nominally, the wheel diameter is set in the robot configuration file to `56`, which is to say, `56mm`, so just under six centimetres, or in old money(?!), just over two inches.

What this means is that we can drive the robot forward a specified distance.

The bands shown on the *Coloured_bands* background are 60cm high.

See if you can write a programme that drives the robot exactly the length of one of the bands by monitoring the `position` value of a one of the motors as the robot drives in a straight line.

How accurately can you cover the distance? (Don't panic, or waste too much time, if you can't...). Comment on your results.

__Hint: how many degrees will the wheel need to turn for the wheel to turn 60cm?__

__Warning: if you use a loop, put something in it that uses up simulator time and progresses the clock, or you may find that your simulator Python programme get stuck and hangs the browser. __

*Note: the `.position` value is returned as a string and should be converted to an `int` if you want to use it numerically.*
<!-- #endregion -->

<!-- #region student=true -->
*How many degrees does the wheel need to turn? Record you calculation and result here.*

*Remember, you can use a code cell as a interactive calculator... You can access pi as a number by importing `from math import pi`.*
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Coloured_bands -p -x 1100 -y 200 -a 90

# Your code here
```

<!-- #region student=true -->
*Record your notes and observations here about how effectively the robot performed the desired task.*
<!-- #endregion -->

<!-- #region activity=true heading_collapsed=true -->
### My Answer

*Click on the arrow in the sidebar to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true hidden=true -->
The `position` counter reports number of degrees turned by the wheel, so let's start by finding out how many degrees we need to turn the wheel to travel 60cm.

Recall, the wheel diameter is 56mm.
<!-- #endregion -->

```python activity=true hidden=true
from math import pi

distance = 60 #cm

# 56mm is 5.6cm
circumference = 5.6 * pi

no_of_turns = distance / circumference
no_of_degrees = no_of_turns * 360

int(no_of_degrees)
```

<!-- #region activity=true hidden=true -->
We can use this calculation in a programme that drives the robot forward until that wheels have turned by the desired amount, and then stops.

Note that the speed of the robot may affect how accurately the robot can perform the task, bearing in mind the comment earlier about how the simulator uses quite crude discrete time steps to animate the world.
<!-- #endregion -->

```python activity=true hidden=true
%%sim_magic_preloaded -b Coloured_bands -p -x 1100 -y 200 -a 90
from time import sleep

tank_steering= MoveSteering(OUTPUT_B, OUTPUT_C)

# Go Forwards
DIRECTION = 0
SPEED = 20

tank_steering.on(DIRECTION, SPEED)


# Do the math...
from math import pi

distance = 60 #cm

# 56mm is 5.6cm
circumference = 5.6 * pi

no_of_turns = distance / circumference
no_of_degrees = no_of_turns * 360


while int(tank_steering.left_motor.position) < no_of_degrees:
    sleep(0.01)
    print("Position: {}".format(tank_steering.left_motor.position))
```

<!-- #region activity=true hidden=true -->
When I ran the programme, it did pretty well, running between the lines and stopping maybe just a fraction too long.
<!-- #endregion -->

## Measuring the Width of a Coloured Track

One of the activities in the Open University [*T176 Engineering* residential school](http://www.open.ac.uk/jobs/residential-schools/modules/modules-summer-schools/txr120-engineering-active-introduction) is a robotics challenge to recreate a test track that depicts several coloured bands of various widths purely from data logged by an EV3 Lego robot.

Let's try a related, but slightly simpler challenge: identifying the width of the track that is displayed on the *Loop* background.

<!-- #region activity=true -->
### Using Logged Data to Take Measurements From the Simulated World

In this activity, you will use data logged by the robot to learn something about the structure of the world it is operating in.

Clear the data from the datalog:
<!-- #endregion -->

```python activity=true
roboSim.clear_datalog()
```

<!-- #region activity=true -->
and then download and run the following program in the simulator to drive the robot over the test track.
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -b Loop
from ev3dev2_glue import get_clock
import time

tank_steering= MoveSteering(OUTPUT_B, OUTPUT_C)

# Define a light sensor
colorLeft = ColorSensor(INPUT_2)

def datalogger():
    """Simple datalogging function."""
    print('Wheel_left: {} {}'.format(tank_steering.left_motor.position, get_clock()))
    print('Light_left: {} {}'.format(colorLeft.full_reflected_light_intensity, get_clock()))

tank_steering.on(0, 20)
while int(tank_steering.left_motor.position)<1000:
    time.sleep(0.05)
    datalogger()

```

<!-- #region activity=true -->
From a chart display of the data, such as the one that is generated if you run the code cell below, how might you identify the width of the black line?

*Hint: in the interactive plotly chart, if you hove over the chart to raise the plotly toolbar, you can select the `Compare data on hover` to report the line values for a particular x-axis value; the `Toggle Spike Lines` view will also show dynamic crosslines highlighting the current and y values.*
<!-- #endregion -->

```python activity=true
import pandas as pd
pd.options.plotting.backend = "plotly"

#Grab the logged data into a pandas dataframe
data = roboSim.results_log

#Create a tabular dataframe from the data
df = eds.get_dataframe_from_datalog(data)

# Generate a line chart from the datalog dataframe
df.plot( x = 'time', y = 'value', color='variable')
```

<!-- #region student=true -->
*How can you use the logged data displayed in the chart above, or otherwise, to work out how wide the black line is? What other information, if any, do you need in order to express this as a distance in (simulated) meters?*

*Record your observations here.*
<!-- #endregion -->

<!-- #region activity=true -->
### Answer
*Click on the arrow in the sidebar to reveal my answer.*
<!-- #endregion -->

<!-- #region activity=true -->
The chart shows the increasing trace from the position sensor and a another trace for the light sensor. The light sensor value dips from 100 to 0 as the robot goes over the black line, then back to 100.

The horizontal x-axis is simulator time. If we take the position count reading at the same time the robot detects the black line, and again at the same time the robot crosses back onto the white background, we can subtract the first position value from the second to give use the distance travelled by the robot.

To convert this to simulated meters, we would need to know what distance is traveled for a motor position increment value of 1.

If the position count is an angular measure (for example, degrees of wheel turn), then we could calculate the distance travelled as:

`wheel_circumference * degrees_turned / 360`

since the distance travelled by the wheel in one complete turn is the same as its circumference.

We could calculate the circumference as:

`wheel_circumference = 2 * wheel_radius * pi`

or:

`wheel_circumference = wheel_diameter * pi`

both of which could be measured from the robot *if* we had physical access to it.
<!-- #endregion -->

## Which Way Did You Say We Were Going, Again?


As well as keeping track of how much the wheels have turned, and estimating location on that basis, we can also use the robot's gyroscope — often referred to as a "gyro" — sensor to tell us which direction it is facing.

In the following activities, you will see how the gyroscope and position sensors can be used to keep track of where the robot has been, as well as helping it get to where it needs to go.

<!-- #region activity=true -->
### Activity: Detecting orientation

The following programme defines a simple edge follower that allows the robot to navigate its way around the shape described in the *Two_shapes* background, logging the gyro sensor as it does so.

Show the chart display, enable the gyro trace, and download and run the programme. Purely by observation of the chart view of the gyro data, do you think you would be able to the  shape corresponding to the the path followed by the robot?
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -c -b Two_shapes -x 400 -y 700 -a -90

colorRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_4)

while True:  
    
    #Get the gyro value
    print('Gyro: '+str(gyro.angle))
    
    intensity_right = colorRight.reflected_light_intensity_pc
    if intensity_right > 70:
        left_motor_speed = SpeedPercent(0)
        right_motor_speed = SpeedPercent(20)
    else:
        left_motor_speed = SpeedPercent(20)
        right_motor_speed = SpeedPercent(0)
    tank_drive.on(left_motor_speed, right_motor_speed)
```

<!-- #region student=true -->
*Add your observations about the gyro data trace as the robot follows the boundary of the provided shape. To what extent can you use the data to identify the shape of the route taken by the robot? How might you identify the path more exactly?*
<!-- #endregion -->

<!-- #region activity=true -->
### My Observations

*Click on the arrow in the sidebar to reveal my observations.*
<!-- #endregion -->

<!-- #region activity=true -->
The gyro sensor values follow a stepped trace in the chart, dropping by 90 or so every time the robot turns a corner, corresponding to a right angled turn counter-clockwise. The values oscillate as the robot proceeds, wiggling as it follows the edge of the line. The width (as measured along the x-axis) of each step is roughly the same, so the robot is describing a square.

I also note that the angle count is not a direction; it seems to be an accumulated count of degrees turned in a particular direction. If the robot were to turn the other way I would expect the count to go down. I even did a little experiment to check that.
<!-- #endregion -->

```python activity=true
%%sim_magic_preloaded -c

# ev3dev2 now has sound...
from ev3dev2.sound import Sound
speaker = Sound()
def say(txt):
    """Don't block on speech."""
    speaker.speak(txt, play_type=1)

gyro = GyroSensor(INPUT_4)

say('Turnn one way')
tank_drive.on(SpeedPercent(20), SpeedPercent(0))
while gyro.angle < 90:
    print('Gyro: '+str(gyro.angle))
    
say('and the other')
# Turn the other way
tank_drive.on(SpeedPercent(0), SpeedPercent(20))
while gyro.angle > 0:
    print('Gyro: '+str(gyro.angle))

say('all done')
```

<!-- #region activity=true -->
## Challenge - Navigating to a Specifed Location

The *WRO_2018_Regular_Junior* challenge background has several coloured areas marked on it at (350, 580), (1180, 960) and (2000, 580).

From the starting location of the robot at (1180, 150, 90), see if you can write a program that drives the robot using dead reckoning — that is, using just the motor `position` and the gyro `angle` values — to drive the robot to one of those locations. Then see if you can get it to drive to one of the other locations.

The background co-ordinates give locations in millimetres relative to a fixed origin.

Once you have got your programme to work reasonably reliably, try adding some noise to the motors using the *Wheel noise* slider in the simulator. Does this have any effect on the performance of your control programme?
<!-- #endregion -->

<!-- #region student=true -->
*You may find it helpful to do some sums to calculate how far the robot has to travel. Make some notes on that here...*
<!-- #endregion -->

```python student=true
# Maybe try our some sums here?
```

```python student=true
%%sim_magic_preloaded -p -x -1180 -y 150 -a 90 -b WRO_2018_Regular_Junior

# YOUR CODE HERE

```

<!-- #region student=true -->
*Comment on how well your robot performed the task here. What strategy did you use to come up with your solution?*

*Describe what affect, if any, adding noise to the motors does the the performance of the robot in completing this dead reckoning task.*
<!-- #endregion -->

## Summary

In this notebook you have seen how the motor `position` tachometer can be used to record how far, in degrees, each motor has turned, and the gyroscope `angle` value to keep track of the accumulated directional turns, in degrees, it has turned. In each case, turning one way increases the count, turning the other decreases it.

Tacho counts and gyro angles are very useful at providing an indicative feel for how a robot has traveled, but they may not be overly accurate. As with many data traces, *trends* and *differences* often tell us much of what we need to know.

Through working with the motors an sensors at quite a low level, you have also learned how the implementation of the simulator itself may affect the performance of our programmes. In certain cases, we may even have to do things in the programme code that are there simply to accommodate some "feature" of the way the simulator is implemented that would not occur in the real robot. In the physical world, time flows continuously of its own accord, in real time! In the simulator, we simulate it in discrete steps, which may even take longer to compute than the amount of time the step is supposed to represent.
