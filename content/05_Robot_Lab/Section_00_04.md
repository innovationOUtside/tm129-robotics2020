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

<!-- #region -->
One of the main problems a robot has is locating itself in its environment: the simulated robot doesn't know where it is in the simulated world. The `x` and `y` co-ordinates are values used by the simulator to keep track of its location and to draw the robot on the canvas. Typically when using a simulator, we try not to cheat by providing the robot with direct access to simulator state information. That would be like you going outside, raising your arms to the sky, shouting *where am I?* and the universe responding with your current location.

Instead, we try to ensure that the information on which the robot makes its decision come from it's own internal reasoning and any sensor values it has access to.

At this point, we could create a magical "simulated-GPS" sensor, that allows the robot to identify its location from the simulator's point of view; but in the real world, we can't always guarantee that external location services are available. For example, GPS doesn't work indoors or underground, or even in many cities, where line of sight access to four or more GPS satellites is not available.


Instead, we often have to rely on other sensors to help us identify our robot's location at least in a relative sense to where it has been previously.
<!-- #endregion -->

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

## 4.1 Activity: Logging Motor Tachometer / "Rotation Sensor" Data


Open the program `Get_rotation_data`. In the Simulator window you should see a graduated grey background that is black at the bottom and white at the top. The program code, which makes Simon rotate and logs the light sensor readings as it does so, is shown in <a xmlns:str="http://exslt.org/strings" href="">Figure 4.1</a>.

Use `Linear_grey`; what's the poing of the grey?

```python
%%sim_magic_preloaded
import time
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

gyro = GyroSensor(INPUT_4)


tank_drive.on(SpeedPercent(50), SpeedPercent(30))
time.sleep(0.1)

#print('left_motor_count'+tank_drive.left_motor.position_sp)
while int(tank_drive.right_motor.position)<1000:
    time.sleep(0.1)
    print('left_motor_count'+str(tank_drive.left_motor.position))
    print('right_motor_count'+str(tank_drive.right_motor.position))

```

In `ev3dev`, we can get hold of tacho count data from each wheel, for example in the steering drive, we can call something like `steering_drive.left_motor.position` (eg via `print('left_motor_count'+str(steering_drive.left_motor.position))`.


![figure ../tm129-19J-images/tm129_rob_p7_f010.png](../tm129-19J-images/tm129_rob_p7_f010.png)


Figure 4.1 Listing: `Get rotation data`


comment : Get rotation data

output left_motor on A

output right_motor on C

sensor light_sensor on 2 is light as percent

var count = 0

main

      comment Add statements here...

      clear data 110

      forward [left_motor right_motor]

      power [left_motor right_motor] 2

      on [left_motor right_motor]

      while light_sensor =100

            comment Add statements here...

            wait 10

      while light_sensor &lt; 50

            comment Add statements here...

      direction [left_motor] [right_motor]

      while (light_sensor &lt;&gt; 100) &amp;&amp; (count &lt; 110)

            comment Add statements here...

            log light_sensor

            set count = count + 1

            wait 8

Run the program. When you upload the data and display the data log, you should see a graph similar to <a xmlns:str="http://exslt.org/strings" href="">Figure 4.2</a>.


![figure ../tm129-19J-images/tm129_rob_p7_f011.jpg](../tm129-19J-images/tm129_rob_p7_f011.jpg)


Figure 4.2 Graph of logged light sensor data


A data log graph. The vertical scale runs from 25 to 50; the horizontal scale plots just over 100 readings. These readings form something like a sine wave, starting high around 50, dropping in a smooth curve to a minimum of 25 and then rising back up to a maximum of 50 again.

What these data clearly show is that the sensor readings vary smoothly between bright greyscale (around 50%) and dark greyscale (around 25%) as the robot rotates. Since the lightest reading must be at the top (north) and the darkest reading at the bottom (south), this provides a way of orienting the robot. First the robot has to find minimum and maximum sensor readings when rotating in its current position, and then it can look for these readings as it rotates.


## 4.2 Activity: Detecting orientation


Open the program `North_south`. Run the program. Simon will start to rotate. After a short delay while it calibrates itself, Simon will begin saying ‘north’ when it points up and ‘south’ when it points down. The program code is shown in <a xmlns:str="http://exslt.org/strings" href="">Figure 4.3</a>.


Perhaps do a gyro experiment here?

```python
%%sim_magic_preloaded
import time
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

gyro = GyroSensor(INPUT_4)


tank_drive.on(SpeedPercent(50), SpeedPercent(30))
time.sleep(0.1)
#print('left_motor_count'+tank_drive.left_motor.position_sp)
while int(tank_drive.right_motor.position)<1000:
    time.sleep(0.1)
    print('Gyro'+str(gyro.angle_and_rate))

```

![figure ../tm129-19J-images/tm129_rob_p6_f04_03.png](../tm129-19J-images/tm129_rob_p6_f04_03.png)


Figure 4.3 Listing: `North and South`


comment : Detect North and South

output left_motor on A

output right_motor on C

sensor light_sensor on 2 is light as percent

const NORTH = 76

const SOUTH = 77

var count = 0

const max_count = 100

var max_grey = 0

var min_grey = 100

var grey = 1

var no_change = 1

main

      comment : Move to a random starting point

      randomize

      power [left_motor right_motor] 2

      direction [left_motor] [right_motor]

      on [left_motor right_motor] for random 500

      forward [left_motor right_motor]

      on [left_motor right_motor] for 200

      comment : Spin on the spot, reading light levels

      direction [left_motor] [right_motor]

      on [left_motor right_motor]

      while count &lt; max_count

            set grey = light_sensor

            if min_grey &gt; grey

                  then

                        set min_grey = grey

            if max_grey &lt; grey

                  then

                        set max_grey = grey

            wait 10

            set count = count + 1

      forever

            while light_sensor &lt; max_grey

                  comment : Keep spinning

            send NORTH

            while light_sensor &gt; min_grey

                  comment : Keep spinning

            send SOUTH


## Gyro turn

Simple turning with gyro - cf. square

```python
%%sim_magic
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor

# Sequential program with gyro turn

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

time_1s = 1

# Set the left and right motors in a forward direction
# and run for 1 second
tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), time_1s)


gyro = GyroSensor(INPUT_4)

target_angle = gyro.angle + 90
tank_drive.on(SpeedPercent(50), SpeedPercent(-50))
while gyro.angle < target_angle:
    pass
```

## 4.3 Challenge: East and west


Try modifying the `North and South` program to make the robot say ‘okay’ (send code 81) when it points east or west.
<!--ITQ-->

#### Question

Would you like a hint?


#### Answer

What light reading would you expect the robot to detect when it is pointing east or west? Tip: deciding between east and west is more difficult!
<!--ENDITQ--><!--ITQ-->

#### Question

With this background image, can you suggest a way of finding the robot’s location?


#### Answer

The greyscale gradient runs from 0 in the south to 100 in the north, so the light sensor reading could be used to locate the robot’s position between north and south. However, there is no information to help determine its position from west to east.
<!--ENDITQ-->
Of course, the technique we used here depends on the robot being in a special environment as represented by the greyscale gradient background. However, the gradient of light intensity could represent some other potential field, for example the strength of signal picked up from a location beacon. The techniques can therefore be generalised to other situations.

