# 5 Optional challenges



```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

## 5.1 Where’s Tiggy?


Open the program `Wheres_tiggy`. The green foliage of some trees will appear in the Simulator window. Run the program to make Tiggy and her pink ball appear (<a xmlns:str="http://exslt.org/strings" href="">Figure 5.1</a>).


![figure ../tm129-19J-images/tm129_rob_p7_f017.jpg](../tm129-19J-images/tm129_rob_p7_f017.jpg)


Figure 5.1 Searching for Tiggy


*What was the original intention of this activity? Can we use some of new sensors for a new, equivalent activity?*

A simulator background of dark green leaves, on which appears a picture of Tiggy, a black Labrador, and her bright pink ball. The area outside the leaves is a plain white background.

The program that I have written, shown in <a xmlns:str="http://exslt.org/strings" href="">Figure 5.2</a>, is actually a ‘stub’; that is, it loads the images but does nothing else.


![figure ../tm129-19J-images/tm129_rob_p7_f018.jpg](../tm129-19J-images/tm129_rob_p7_f018.jpg)


Figure 5.2 Listing: `Wheres_tiggy`


comment : Where's Tiggy?

output left_motor on A

output right_motor on C

sensor light_sensor on 2 is light as percent

macro load_image

      comment : Load images at random

      randomize

      local i = 1 + random 4

      if i = 1

            then

                  background "dog_1.bmp"

      if i = 2

            then

                  background "dog_2.bmp"

      if i = 3

            then

                  background "dog_3.bmp"

      if i = 4

            then

                  background "dog_4.bmp"

      if i = 5

            then

                  background "dog_5.bmp"

main

      comment Add statements here...

      call load_image

      send 82

      wait 200

      comment add your code here

The challenge here is to write a program that enables Simon to find Tiggy while staying inside the trees. You can start off by using the stub, which assumes there are five positions for Tiggy. *Hint*: find Tiggy by locating her ball.

If you want to see my solution, open `Find_tiggy` and run the program to see how well it works. My approach to finding Tiggy, using a scanning technique (<a xmlns:str="http://exslt.org/strings" href="">Figure 5.3</a>), is rather simplistic. Can you think of a better way of doing it?


![figure ../tm129-19J-images/tm129_rob_p7_f019.jpg](../tm129-19J-images/tm129_rob_p7_f019.jpg)


Figure 5.3 Finding Tiggy by scanning


A simulator background of dark green leaves with a Tiggy and her bright pink ball. The path of the robot is shown. It starts at bottom left, goes up the left edge until it reaches the top, turns through 180° and returns parallel to its first track. At the bottom, it once again turns through 180° to start a third parallel sweep, and continues this pattern across the background. Each sweep is separated by approximately the diameter of Tiggy’s ball.


## 5.2 Block challenges


There are three block challenges. They involve writing programs to make Simon navigate from the start to the finish (home) for each of the courses shown in <a xmlns:str="http://exslt.org/strings" href="">Figure 5.4</a>. They are progressively more difficult, and unless you have a lot of time it is recommended that you don’t attempt them all.


![figure ../tm129-19J-images/tm129_rob_p7_f021.jpg](../tm129-19J-images/tm129_rob_p7_f021.jpg)


 Figure 5.4 The bitmap files for the block challenge: (a) block_challenge_1.bmp, (b) block_challenge_2.bmp and (c) block_challenge_3.bmp


The background images for the block challenge. They have a cream background on which there are red block obstacles. Two mid-grey panels are labelled ‘Start’ and ‘Home’, placed at the bottom and top. 

 In the first challenge, the start at the bottom and the home at the top are connected by a black line. One red block straddles the line; the others flank the home panel. 

 The second challenge also has the start at the bottom and the home at the top but they are no longer connected by a black line. The obstacles are positioned in the same way: one blocking the direct line from start to home, the others flanking the home panel. The background remains cream at the top, but is light grey at the bottom. The first obstacle is on the grey background; the home panel and other two obstacles are on the cream background. 

The final challenge reverts to a cream background throughout; the start and home panel are at bottom and top as before. There are two flanking obstacles near the home panel, and another half way between, but offset to the right. There is now a further obstacle immediately in front of the start panel which is now in the bottom left corner; this would force the robot to head to the right on leaving the start. In addition, there are now blue lines drawn which the robot could follow, but these do not form complete paths. One leaves the start panel heading east and then curves round to the northwest; it ends in a white circular patch. The second starts a little beyond this; it forms a complete circle, out of which a tangent leads in a curve which heads north, finishing in another white circular patch just to the south of the home panel and between the flanking obstacles.

You will need to create a new program using the `New` ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f022.gif](../tm129-19J-images/tm129_rob_p4_f022.gif)  toolbar button or the `File | New` menu item.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: press Ctrl+N</p></div> Save your new stub program with a sensible name such as `block challenge 1`. 

Then you will need to set background image to one of the files shown above. Choose `Simulator | Configure` and then find and select the appropriate image file. Check that the `Wall` colour is set to red.

The idea behind these challenges is that the lines and shaded backgrounds give you some information for the robot to orient itself. Use the Controls window in conjunction with dragging Simon around the screen to find out how the light and touch sensors respond to the various background colours and the red blocks. Recall that to set the initial position of Simon, you drag it to the desired start position and orientation, and save the program.
<!--ITQ-->

#### Question

Would you like a hint about how the robot can detect its goal?


#### Answer

The grey ‘Home’ block is the goal; the light sensor reading over this can be used to detect the goal.
<!--ENDITQ--><!--ITQ-->

#### Question

Would you like some hints about the obstacles?


#### Answer

The red blocks are obstacles: Simon will not drive through them. But they can be detected using the touch sensors. You can avoid them by the strategy we’ve previously seen: back off, turn slightly and try again.

Can the blocks near the goal be used to help? A robot avoiding the blocks to the side of the goal might be guided towards the goal. 
<!--ENDITQ--><!--ITQ-->

#### Question

Would you like some hints about navigation techniques?


#### Answer

Dead reckoning is one option, but wouldn’t help if the environment was changed slightly or if the robot had noisy components. 

Black and blue lines are provided which can be followed using the line-following methods we have covered. But these may be blocked or missing in parts, so you may have to resort to dead reckoning to deal with these local problems. The ends of lines are marked with a white circle.

Your program may need to alternate between different ‘modes’ of driving. If it finds a line, follow it. If it bumps into an obstacle, avoid it. If it comes to the end of a line, carry on and hope for the best.
<!--ENDITQ-->
This is the end of Robot Lab Session 6.

