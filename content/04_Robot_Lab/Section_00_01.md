# Introduction

<font color='red'>JD: As in Week 3, I think this introduction would be better as an unnumbered introduction and this notebook should be combined with the following notebook (this better matches Weeks 1 and 2).</font>

In this session you will explore a range of simulator environments and sensor and motor drive noise settings, as well as modifying the robot configuration by changing the height of the simulated light sensor.

Through your experiments, you will investigate the way the sensors behave and how this information can be used to control the robot.

## The simulator environment as a laboratory

Let’s just recap how we might be able to use the simulator as an experimental laboratory.

When the robot simulator screen is displayed, a blank background image is shown by default. You can configure the simulator to use different background images by selecting the desired background from the drop-down list in the simulator or by specifying the background to be used via the `-b` or `--background` parameter when defining a `sim_magic` code cell.

Background images can also be loaded from a file. If you create your own background images they should be PNG or JPEG images 2362&nbsp;pixels wide and 1143&nbsp;pixels high. Python code for generating some of the background images using the Python PIL package can be found in the notebook [`backgrounds/Background Image Generator.ipynb`](../backgrounds/Background%20Image%20Generator.ipynb).

Loading in a background from the default list can also determine the starting location and orientation of the simulated robot, and even the configuration of the robot and any obstacles present in the world.

At the current time, robot configuration updates *cannot* be associated automatically with uploaded simulator backgrounds. However, it is possible to update both the robot and obstacle configuations via pop-up dialogues that can be opened using the simulator *Configure Robot* and *Obstacles...* buttons as well as passing in certain pieces of configuration data via the `sim_magic` parameters.

More generally, the RoboLab simulator provides the following controls:

- load background
- configure robot
- configure obstacles
- pen up / pen down
- clear trace (that is, clear pen trace)
- show chart
  - select trace(s) (colour, left light, right light, ultrasonic, gyro, left wheel, right wheel)
- clear chart
- set light sensor noise value [TO DO: at the moment this is one slider for all sensors, rather than a per input basis;]
- set motor/wheel noise value [TO DO: at the moment this is one slider for all motors, rather than one per output;]
- set the X and Y co-ordinates and the Angle or orientation of robot; reset the robot’s position to these values via the *Move* button; the X and Y values are updated when the robot is dragged across the canvas; the *Reset* button resets the robot’s location and orientation to the default for that background (if set). 

<font color='red'>JD: The following need resolving:</font>

*TO DO: need some way of adding keyboard shortcuts to simulator items.*

*TO DO: slow down the frame rate; show clock / counter; zoom in / out on canvas or stop robot going off the edge of the world; show robot motor status and sensor values; show robot current location; support measuring on canvas (I think that may still be there from original ev3devsim).*

*TO DO: should we provide a simple drawing tool on the canvas so students can modify a blank canvas, and perhaps save it? eg http://www.williammalone.com/articles/create-html5-canvas-javascript-drawing-app/ *

