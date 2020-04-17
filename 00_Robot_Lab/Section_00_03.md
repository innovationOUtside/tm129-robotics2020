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

On the first line of code in that new code block, the robot drives *backwards* at half speed for 2 rotations of the wheels (`tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2)`). (According to the [documentation](https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#ev3dev2.motor.MoveTank.on_for_rotations), *"if the left speed is not equal to the right speed (i.e., the robot will turn), the motor on the outside of the turn will rotate for the full rotations while the motor on the inside will have its requested distance calculated according to the expected turn"*).

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


This is similar to the Lego light sensor in Figure 3.3.


![figure ../tm129-19J-images/tm129_rob_p1_f029.jpg](../tm129-19J-images/tm129_rob_p1_f029.jpg)


Figure 3.3 The Lego light sensor (shown next to a pound coin for scale)


A Lego light sensor. This is a blue Lego brick, 4 x 2 studs in size with a wire emerging from one end. At the other end, two small lenses are visible. One is clear – this is the light sensor itself. Next to it is a red LED which can be used as a light source to illuminate a surface so that the sensor measures light reflected from the surface rather than ambient light levels.

Open the `Sensor_sim` program. You should see the robot over a background of four grey bars in the `Simulator` window, as shown in Figure 3.4. 


![figure ../tm129-19J-images/tm129_rob_p1_f030.jpg](../tm129-19J-images/tm129_rob_p1_f030.jpg)


Figure 3.4 Grey bars in the environment


The simulated robot over a white background across which are drawn four broad grey bands. These are different in intensity, from a pale grey to black.

The program code is:

```javascript
speechSynthesisInstance.cancel();
```

![figure ../tm129-19J-images/tm129_rob_p1_f031.jpg](../tm129-19J-images/tm129_rob_p1_f031.jpg)

```python
%%sim_magic roboSim
# Sensor_sim
from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor

#import playsound

tank_turn = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)

tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#prev = colorLeft.reflected_light_intensity
while True:
    print('Colour: ' + str(colorLeft.reflected_light_intensity ))

    #if prev!=colorLeft.reflected_light_intensity:
        #Note that the simulator continues as the utterance is made
        # and multiple utterances may be queued up.
    #    playsound.say("Changed...")
    #prev = colorLeft.reflected_light_intensity
```

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

df = get_dataframe_from_datalog(roboSim.results_log)
df.head()
```

```python
import seaborn as sns
ax = sns.lineplot(x="index", y="value", hue='variable', data=df)
```

```python
import matplotlib.pyplot as plt

g = sns.FacetGrid(df, row="variable", height=5, aspect=2, sharey=False)
g = g.map(plt.plot, "index", "value", marker=".");
```

Figure 3.5 Listing: `Sensor_sim`


comment :  LIGHT SENSOR SIMULATION

sensor light_sensor on 2 is light as percent

output left_motor on A

output right_motor on C

const number_of_readings = 50

const delay = 10

main

      comment :  set up datalog &amp; move robot forward

      clear data number_of_readings

      forward [left_motor right_motor]

      on [left_motor right_motor]

      repeat number_of_readings

            comment :  repeatedly log the light_sensor value

            log light_sensor

            wait delay

      off [left_motor right_motor]

After the comment in the first line of the program, the next three lines configure the light sensor and motors as before. 

 The constant `number_of_readings` is set to 50, meaning that 50 readings of the light sensor will be taken. 

The constant `delay` is set to 10 hundredths of a second, or 1/10 of a second. This will be the time interval between sensor readings. During this time a robot like the Lego ones seen previously would move a millimetre or two.

 The main program begins by defining and clearing a *data log*. This is a very powerful mechanism for storing the data collected by a robot. 

The `forward` command sets the `left_motor` and `right_motor` to go forwards, and the `on` command switches the motors on, making the simulated robot go forwards.

 The `repeat number_of_readings` command means ‘do the following 50 times’, since `number_of_readings` was set to 50. 

As the robot moves forwards, the `log light_sensor` command puts the current value of the `light_sensor` into the simulated robot’s data log. The data log is a list of numbers stored by the robot for future use. 

The `wait` command then waits for 1/10 of a second, and the repeat command makes the whole cycle happen all over again. 

In this way 50 samples of the light sensor measurement are stored in the data log.

---


### Uploading the data log to draw a graph

Run the program. When the robot stops, click on the Upload  ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f032.jpg](../tm129-19J-images/tm129_rob_p1_f032.jpg)  button in the toolbar (or choose the `Connect &gt; Upload data log` menu).<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, C, U</p></div> Then open the `Data log` window by clicking on its `Restore` ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f017.jpg](../tm129-19J-images/tm129_rob_p1_f017.jpg)  button or by choosing the `Window &gt; Data log` menu.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, W, 4</p></div> You should get a graph similar to that shown in Figure 3.6.


![figure ../tm129-19J-images/tm129_rob_p1_f033.jpg](../tm129-19J-images/tm129_rob_p1_f033.jpg)


Figure 3.6 The sensor data logged during the simulation


The RobotLab Data log window, with a graph showing sensor data. The graph has a vertical axis with a scale that runs from 0 to 100, and a horizontal axis that runs from 0 to 50. Fifty points are plotted showing successive sensor readings. Reading the graph from left (the first sensor reading) to right (the last sensor reading), the first half-dozen values are all 100, followed by a drop to 75 for a few values. The readings then go back to 100, before dropping to 50 for four or five readings. The readings again return to 100, drop once more, this time to 25, return to 100, drop to zero, and finally return to 100 for the remaining 15 or so readings.

The `Graph` tab shows the graph in Figure 3.6. It is also possible to see a table of the readings by clicking on the `Data` tab.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Use Tab and Shift+Tab to switch between tabs</p></div>

Starting from the left-hand side, each green point represents a sensor reading. The white background from the grey bars environment shows as 100% and the solid black line shows as 0%.

As the robot progresses up the screen, the bars that it encounters get progressively darker, so the sensor readings reduce. 

---


## 3.3 Activity: Robots that speak

As well as moving about the simulated world, the robot can also affect the state of the world by making a noise it. In particular, we can get the robot to speak.

Open the program `I_can_count`. This program has the following code. 


![figure ../tm129-19J-images/tm129_rob_p1_f034.jpg](../tm129-19J-images/tm129_rob_p1_f034.jpg)

```python
%%sim_magic roboSim
# I can count...
import playsound

for i in range(5):
    playsound.say(str(i))
```

Figure 3.7 Listing: `I_can_count`


comment :  I CAN COUNT

var N = 1

main

      wait 100

      while N &lt; 10

            comment : send number N to be spoken

            send N

            wait 120

            set N = N + 1

Run the program; you should hear the system counting from 1 to 9.

The program works as follows. The expression `var N = 1` declares a *variable* called N. This is a ‘slot’ in computer memory that can store a number. The declaration also assigns the initial value 1 to the variable. There will be more about variables in Study week 2. 

As usual, `main` tells the computer that the main part of the program is about to start. The expression `while N &lt; 10` tells the computer to execute all the code below, while the value of N is less than 10. 

 The key to this program is the command `send N` which sends a message from the (simulated) robot back to the computer. RobotLab receives this message and responds by ‘speaking’ words or phrases that corresponds to the numerical code sent by the program using the `send` command. 

Simple robots like the Lego robots simulated by RobotLab are limited in the features that they offer, and they would not normally be able to ‘speak’ to us. In fact, such simple robots have very few ways in which they can communicate with humans at all. However, most do have some form of communication, either between robots or between robot and computer. Here we are getting the robot to send a simple message back to a computer and allowing the computer to translate that into speech for us to understand. The LEGO Mindstorms RCX robots can send messages using an infrared transmitter/receiver like that found in a TV remote control handset. The message itself is limited to a simple numeric code. 

RobotLab is set up to receive these simple numeric messages, either from a real robot with appropriate hardware or from a simulated robot. Open the `Messages` window using the `Window &gt; Messages` menu and run the program again to see the messages arrive. By default, RobotLab is also set up to translate these simple numeric messages into spoken words and phrases. It does this by playing a pre-recorded audio file corresponding to each numeric code. 

The same program could be used on a real Mindstorms RCX robot. The send command will transmit an infrared message and RobotLab will receive it, and play the corresponding audio message in the same way.

Using this technique it is possible to get a very simple (real or simulated) robot to talk. 

__Changing the program to play other sounds__

You can change this program so that it plays other sounds.

For example, click on the line of code `while N &lt; 10` in the `Program` window, and it will appear in the `Key-Value` pane at the bottom left of the `Program editor` (Figure 3.8). Click on the expression `N &lt; 10` in the `Key-Value` pane, and change it to N &lt; 20. To do this, just place the cursor between the 1 and the 0, backspace to delete the 1, and type 2 to make 20. If you’ve typed this correctly, press Enter to accept the change; otherwise press Escape to start again.

Now when you run the program it should count from 1 to 19.


![figure ../tm129-19J-images/tm129_rob_p1_f035.jpg](../tm129-19J-images/tm129_rob_p1_f035.jpg)


Figure 3.8 Changing numbers using the `Key-Value` pane


Screen dump of the RobotLab program editor displaying the ‘I_can_count’ program listed above. The statement ‘while N &lt; 10’ is highlighted in the editor, and the key–value window displays the key ‘condition’ and the value ‘N &lt; 10’.

 You can change the initial value of `N` in a similar way. Click on the declaration `var N = 1` in the program, and it will appear in the `Key-Value` pane. Try changing the value from 1 to 10, to make this line of code into `var N = 10`. Then when you run the program it will count from 10 to 19. 
<!--ITQ-->

#### Question

How would you change this program so that it counts from 15 to 20?


#### Answer

You would need to change the initial value of `N` by editing the declaration to read `var N = 15`.

You would also need to change the test condition to read `N &lt; 21`.

You might have been tempted to write the test as `N &lt; 20`. Can you see why this would not include the value ‘20’ in the numbers that the robot counts?
<!--ENDITQ-->

## 3.4 Activity: Testing your reflexes


Open the program `Test_reflexes`. The `Simulator` window will appear as Figure 3.9. 


![figure ../tm129-19J-images/tm129_rob_p1_f036.jpg](../tm129-19J-images/tm129_rob_p1_f036.jpg)


Figure 3.9 The `Simulator` window for the reflex testing program 


The Simulator window with the robot positioned at its centre over a grey circle. At the top are three squares of colour (grey, blue and green) and three more at the bottom (black, red and yellow).

For this program you need to click and drag the robot using your mouse. Click and hold the left mouse button over the robot, drag it to a new location and release. Try this now.
<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Note on accessibility-->
You may not be able to carry out this activity if you have difficulty using a mouse. A video showing a similar program executed on a Lego robot is included below.
</div>
When you run the reflex testing program, it will call out a colour. You have to move the robot into the square of the corresponding colour, then back inside the grey circle as quickly as you can. The light sensor on the front of the robot must be inside the square to score a hit. 

The program will then call out another colour name at random, and you have to move the robot a second time. This will be repeated ten times in total. After this, the program will announce your mean (average) response time in tenths of a second.

Run the program now to test your response time.

 Click on the upload  ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f037.jpg](../tm129-19J-images/tm129_rob_p1_f037.jpg)  button (or choose `Connect &gt; Upload data log`)<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, C, U</p></div> and the data collected by the program will be uploaded. Then click on the `Window &gt; Data log` menu (Figure 3.10) to open the Data log window (Figure 3.11). 


![The RobotLab window menu showing the item ‘4 Data log’ highlighted.](../tm129-19J-images/tm129_rob_p1_f038.jpg)


Figure 3.10 Opening the `Data log` window



![figure ../tm129-19J-images/tm129_rob_p1_f039.jpg](../tm129-19J-images/tm129_rob_p1_f039.jpg)


Figure 3.11 Displaying the `Data log` window


The Data log window. This shows nine sensor readings whose values range from 10 to 18; the most common value is 12 with four readings. The last two readings are 12.

The `Data log` window shows the time taken to respond to each of the 20 calls. The last two readings give the mean (average) response time.

This activity may not work perfectly the first time you try it. If it doesn’t, just try again.

---


### Advanced challenge

The reflex program does not test to see if you have selected the right colour. Suggest a way that it might do this. Don’t try to program your idea at the moment.

---

---


### Viewing the reflex test on a real robot
<!--MEDIACONTENT--><!--ENDMEDIACONTENT-->
This video clip shows a Lego robot being used for a reflex test, using contact switch sensors mounted on its right and left sides. 

---

