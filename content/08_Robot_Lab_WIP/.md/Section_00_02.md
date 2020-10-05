---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,.md//md
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
---

# 2 Recognising digits

*Using the robot to recognise MNIST digits using MLP and CNN? With part 1 relating to getting data in and out of the simulator and handling the image data?*

*Or should we do MLP brittleness and perhaps CNN in week 6?*

Open the `Simon_recognises_fruit` program from the `week-8` folder. The image in the Simulator window should be similar to Figure 2.1.


![figure ../tm129-19J-images/tm129_rob_p9_f004.jpg](../tm129-19J-images/tm129_rob_p9_f004.jpg)


Figure 2.1 Simon ready to collect data on a pear


The background image for ‘Simon recognises fruit’. This is a composite colour image showing two images each of bananas, oranges, pears and strawberries at random positions and orientations. Simon is also shown superimposed. The robot is configured with a single, downward-facing light sensor mounted in the centre of the robot between the two wheels.

Place Simon in the starting position shown in Figure 2.1; that is, ready to drive forward over the long axis of the image of a pear. Recall that to move Simon around the screen, left-click on the robot, hold down the mouse button and drag to a new position. To rotate Simon, right-click on the robot and drag clockwise or anticlockwise.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: drive Simon using the driving shortcuts (Ctrl + numeric keypad)</p></div> When Simon is in position, run the program. Note that the position of Simon’s downward-facing light sensor (the small blue square) has been moved to the centre of the robot.

You should observe Simon move across the pear until it encounters white pixels of the background again. It makes a measurement while it does this. Next, it moves back half the distance it has just measured, rotates by 90° and moves forward until it detects white pixels. Then it goes backward again until it encounters white pixels, taking another measurement. These two measurements are sent from Simon to the PC.

The configuration for the `Simon_recognises_fruit` program loads a pre-trained neural network called `recfruit.nnd` into RoboLab. It has two inputs for the measurements just made and four outputs – one for each item of fruit. RoboLab uses this network to classify the fruit. Open the RoboLab `Neural net` window from the `Window` menu to see the network in operation.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: Alt, W, 8</p></div>

Try dragging Simon around the various items of fruit to see if it recognises them correctly. Recall from Robot Lab Session 7 that the neural network has been trained with data on the longest and shortest axes of the fruit.

