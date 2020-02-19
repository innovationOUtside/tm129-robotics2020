# 4 RobotLab’s simulator remote control



## 4.1 Activity: Remote control


The RobotLab environment allows you to write programs that an autonomous robot will run. As you have seen, RobotLab also provides a simulated robot that appears in the `Simulator` window so that you can test out your programs. Some (real) robots can be controlled by a human using a remote control. In a similar fashion, RobotLab also provides a remote control unit that you can use to control the (simulated) robot directly.

Start RobotLab. (If you already have a program loaded, choose `File &gt; New`.) In this activity, you are not going to program the robot, so you can close or minimise the `Program editor` window. (Do you remember how to do this? If not, refer back to <a xmlns:str="http://exslt.org/strings" href="">Section 1.6</a>.) Open the `Controls` window either by clicking on its restore icon or by choosing `Window &gt; Controls`.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, W, 3</p></div>

The `Controls` window is shown in Figure 4.1. This control panel, also called the *simulator remote control unit*, can be repositioned on any part of the screen. Click and drag on the `Controls` window title to move it to a convenient position beside the `Simulator` window.


![figure ../tm129-19J-images/tm129_rob_p1_f040.jpg](../tm129-19J-images/tm129_rob_p1_f040.jpg)


Figure 4.1 The RobotLab simulator remote control unit


The RobotLab controls window. This is divided into three areas: top left are the direction controls, bottom left are the simulator clock controls, and to the right are the input and output monitors. The direction controls and output monitors will be described in following figures. The clock controls are two buttons representing a clock with ‘play’ and ‘stop’ icons superimposed. The input monitors are three boxes labelled 1, 2, 3. These can either contain numbers representing sensor readings from 0 to 100, or for touch sensors a shape that turns dark when the sensor is pressed.

 To use the simulator remote control unit, you need to have the simulator clock running. You can set it running by using the `Simulator &gt; Start clock` menu,<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+Home</p></div> or more easily from the `Start clock` ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f041.jpg](../tm129-19J-images/tm129_rob_p1_f041.jpg)  button on the remote control unit at the bottom left of the `Controls` window. Click on this button now. 

 The clock remains running until you switch it off using the `Stop clock` menu or  ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f042.jpg](../tm129-19J-images/tm129_rob_p1_f042.jpg)  button.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+End</p></div> Leave it on for the duration of this exercise. 

 At the top of the remote control are several direction buttons (Figure 4.2).<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Shortcuts are given in Table 4.1</p></div> You click on the forward arrow to switch both motors on and drive the simulated robot forwards. You click on the backward arrow to drive it backwards, etc. And you click on the black square in the centre of the direction controls to turn both motors off and stop the robot. 


![figure ../tm129-19J-images/tm129_rob_p1_f043.png](../tm129-19J-images/tm129_rob_p1_f043.png)


Figure 4.2 The direction of the wheels set by the controller 


The direction controls. There are nine buttons laid out in a 3 x 3 grid, each with an arrow pointing in the relevant direction. The directions of each button and their keyboard shortcuts are given in the text below.

Now click on the forward arrow to drive the robot forwards, and then click on the stop button to stop the robot. Next click on the down arrow to drive the robot backwards, and then stop the robot again.

The remote control unit also displays information about the robot’s inputs and outputs. The bottom half of this display shows what is happening to the motors. Above the motor labels A, B and C are several indicators. The top indicators, solid black dots or crosses in a circle, show whether the motor is turned on or off, respectively (Figure 4.3).

The second indicators, up or down arrows, show whether the motor is switched to a forwards or backwards direction. 

The sliders give the power level for each motor, which ultimately corresponds to the speed with which the motor turns. Leave these at their maximum levels for now.


![figure ../tm129-19J-images/tm129_rob_p1_f044.jpg](../tm129-19J-images/tm129_rob_p1_f044.jpg)


Figure 4.3 Controlling the simulated motor power


The output controls and monitor used to control motor power. There are three identical outputs, labelled A, B &amp; C. Above each label is a slider for setting the power from 0 to 8. Above this is an arrow the faces up or down for indicating forward of backward direction. Finally, at the top is an indicator indicating whether the motor is on or off.

By looking at the motor indicators, can you see how the robot is managing to turn? Try driving the robot forwards, backwards and turning in different directions.

 In order to turn the robot, *differential* or *skid* steering is used.

For example, click on one of the curved arrows to rotate the robot about its centre. To turn the robot clockwise about its centre, the left motor (A) is switched on in a forwards direction, and the right motor (C) is switched on in a backwards direction. 
<!--ITQ-->

#### Question

How would you control the motors to turn the robot anticlockwise about its centre?


#### Answer

The right motor needs to run forwards and the left motor to run backwards.
<!--ENDITQ-->
The robot can also turn clockwise or anticlockwise by switching on either motor A or motor C and leaving the other motor switched off.
<!--ITQ-->

#### Question

How would you control the motors to make a slow, gradual turn to one side?


#### Answer

If the motors run at different speeds, the robot will make a gradual turn.
<!--ENDITQ-->
A slow turn (right forwards, left forwards, right backward or left backwards) can be obtained by switching on both motors either forwards or backwards, but running them at different power levels (i.e. at different speeds) using the slider controls. Click on the forward arrow, then experiment by reducing the power levels for motors A and C to 75% and 50% respectively.

<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Ctrl+NumPlus or Ctrl+NumMinus</p></div>If you lose sight of the robot in the `Simulator` window, you can zoom the view of the `Simulator` window in or out. Choose `Simulator &gt; Zoom in` or `Simulator &gt; Zoom out`, or click on the zoom  ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f045.jpg](../tm129-19J-images/tm129_rob_p1_f045.jpg)  buttons on the toolbar.

If you happen to leave the robot moving for a long time and can’t find it again, you can reset the simulator by choosing `Simulator &gt; Reset`.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Shift+Ctrl+Home</p></div> If all else fails, just close RobotLab and reopen it.

To move the robot, left-click and hold down the cursor on the robot itself, and drag and drop it within the `Simulator` window. You can also rotate the robot by right-clicking on it and dragging it with the mouse.


## 4.2 Activity: More remote control


In the `Controls` window there is also a set of indicators for each sensor (1, 2, 3) (Figure 4.4). The indicators show the readings provided by sensors connected to the relevant input ports.


![figure ../tm129-19J-images/tm129_rob_p1_f040.jpg](../tm129-19J-images/tm129_rob_p1_f040.jpg)


Figure 4.4 The RobotLab simulator remote control unit


The RobotLab controls window. This is divided into three areas: top left are the direction controls, bottom left are the simulator clock controls, and to the right are the input and output monitors. The direction controls and output monitors will be described in following figures. The clock controls are two buttons representing a clock with ‘play’ and ‘stop’ icons superimposed. The input monitors are three boxes labelled 1, 2, 3. These can either contain numbers representing sensor readings from 0 to 100, or for touch sensors a shape that turns dark when the sensor is pressed.

Open the `Controller_test` program and run it. The robot will not move – the program doesn’t turn the robot’s motors on. Instead, use the controller to drive the robot to go forwards over the grey areas, and note the change in light sensor value. The light sensor is shown by the small blue square on the simulated robot and is connected to input port 2.

Try driving the robot over one of the red blocks. You should find that it stops. This is because red is set to ‘solid’, simulating an obstacle in front of the robot. See what happens to the touch sensors when they touch the red area. The touch sensors are shown as small green squares on the robot and are connected to input ports 1 and 3.

---


### Driving round the red blocks in show-trail mode

Rerun the `Controller_test` program in `show-trail` mode. Choose the `Simulator &gt; Show trail` menu item<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, S, T</p></div> or click on the Show trail  ![inlinefigure ../tm129-19J-images/tm129_rob_p5_f014.jpg](../tm129-19J-images/tm129_rob_p5_f014.jpg)  button in the toolbar. Run the program again to see the robot’s trail.

Drive the robot over the grey areas, and one and half times round the red blocks as shown. It’s more tricky than it looks. My attempt is shown in Figure 4.5.


![figure ../tm129-19J-images/tm129_rob_p1_f046.jpg](../tm129-19J-images/tm129_rob_p1_f046.jpg)


Figure 4.5 Negotiating the red blocks in pen-down mode


A screen shot of RobotLab showing the simulator window with a trace left by the robot as it was driven around the red blocks. The red blocks are arranged at the four corners of a square. In the centre between the blocks is a vertical grey strip divided into four areas of different intensity ranging from pale grey at the top to black at the bottom. The track superimposed shows a straight line up from the start position over the grey strip followed by a couple of laps around the outside of the four red blocks. Each lap is a rough square with rounded corners, although the sides are far from straight and there are wild wobbles in a couple of places. 

You may find it easier to control the robot using the keyboard rather than the mouse. RobotLab uses the keys on the numeric keypad of your computer keyboard as short-cuts for the direction buttons in the remote control window; they are laid out in the same pattern.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 4.1 Remote control short-cut keys</caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f11a.gif](../tm129-19J-images/tm129_rob_p1_f11a.gif) 

Veer left

Ctrl+7
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f12a.gif](../tm129-19J-images/tm129_rob_p1_f12a.gif) 

Forward

Ctrl+8
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f13a.gif](../tm129-19J-images/tm129_rob_p1_f13a.gif) 

Veer right

Ctrl+9
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f14a.gif](../tm129-19J-images/tm129_rob_p1_f14a.gif) 

Spin left

Ctrl+4
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f15a.gif](../tm129-19J-images/tm129_rob_p1_f15a.gif) 

Stop

Ctrl+5
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f16a.gif](../tm129-19J-images/tm129_rob_p1_f16a.gif) 

Spin right

Ctrl+6
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f17a.gif](../tm129-19J-images/tm129_rob_p1_f17a.gif) 

Back left

Ctrl+1
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f18a.gif](../tm129-19J-images/tm129_rob_p1_f18a.gif) 

Backward

Ctrl+2
</td>
<td class="highlight_" rowspan="" colspan="">
 ![inlinefigure ../tm129-19J-images/tm129_rob_p1_f19a.gif](../tm129-19J-images/tm129_rob_p1_f19a.gif) 

Back right

Ctrl+3
</td>
</tr>
</tbody>
</table>

This is the end of Robot Lab Session 1.

---

