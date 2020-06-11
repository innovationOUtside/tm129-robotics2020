```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

# 3 Sensor noise


My line-following program in the previous activity seems to work reasonably well. However, it is actually rather a poor program because it is not robust in the presence of *noise*. Recall from an earlier session that noise is due to random variations of the electrical signals recording the level of light sensed. In a real world setting, it might also include random environmental noise, such as fluctuating light levels from shadows or as the sun tracks across the sky or goes behind a cloud.

The *Lollipop* background image used for the line following activity was made with a Python drawing package (see the `backgrounds/Background Image Generator.ipynb* notebook), and the colours are all very precise, with no variation. Real images are not like this.

If it is not already loaded, open the `Line follower` program. Click on `Simulator | Configure` menu item, as you did before (Figure 1.1). Click on `Browse` and this time select `scanned_lines.bmp` as the background image. Close the Configure simulation dialogue. To make this image, I printed `track.bmp` on a colour printer, and scanned it using a flatbed scanner. Figure 3.1 shows an enlargement by a factor of 8 of two portions of the image containing the red and yellow bars, the black line and the grey background.

The following image shows a highly magnified view of two portions of a scanned version of a image. Each pixel is visible, but there is considerable variation in colour, for example the black line appears as many shades of dark grey, and some pixels of the pale grey background have noticeable pink, green or blue casts.



![figure ../tm129-19J-images/tm129_rob_p6_f009.jpg](../images/tm129_rob_p6_f009.jpg)

A scanner can be viewed as a kind of sensor, analogous to the robot acquiring data from a camera. As you can see, the scanned image, when loaded into RobotLab, looks okay. However, when viewed under the magnifying glass, it’s evident that the colours have been distorted considerably by the scanner sensor. For example, when viewed on screen there are areas of yellow, green and brown above the red bar. This is quite normal and occurs with all imaging sensors, including digital cameras and video recorders. It is due to electrical noise in the devices collecting the information.

The original scanned image is lost, but we can recreate a similar effect using a range of inage processing techniques (see the `backgrounds/Background Image Generator.ipynb` notebook for examples).

Human vision is very adaptable and can usually overcome these irregularities. If you have normal colour vision you should be able to pick out the red, yellow, black and grey areas in this image easily, but it is much more difficult for a machine to do this. Poor machine vision is a major problem in the development of robots.

If you try to run the line-follower program now, it won’t work because the colours have changed, and the way that Simon’s sensor reads the colours has also changed. So, back to the drawing board.


We could also introduce noise effects in robot sensors themselves.



Open the control panel and drag Simon around the screen as you did before, taking five readings for each of grey, yellow, red and black, as shown in Table 3.1. For each colour, make a note of the lowest and highest readings.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 3.1 Light sensor readings</caption>
<tbody>
<tr>
<th>Reading (%) </th>
<th> grey</th>
<th> yellow</th>
<th> red</th>
<th> black</th>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">1 </td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">2</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">3 </td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">4 </td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">5 </td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">lowest</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">highest</td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
<td class="highlight_" rowspan="" colspan=""></td>
</tr>
</tbody>
</table>

When I did this I got the following results: grey 83–90%, yellow 71–77%, red 49–51% and black 26–31% (Figure 3.2). This suggests a good colour separation.


![figure ../tm129-19J-images/tm129_rob_p6_f010.jpg](../tm129-19J-images/tm129_rob_p6_f010.jpg)


Figure 3.2 The observed colour ranges


A scale from 0 to 100% on which are shown the ranges for different nominal colours: black 26-31%, red 49-51%, yellow 71-77%, pale grey 83-90%.

Using these data to separate the colours, I defined thresholds as shown in Table 3.2.
<table xmlns:str="http://exslt.org/strings">
<caption>Table 3.2 Thresholds</caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan="">
black–red
</td>
<td class="highlight_" rowspan="" colspan="">
40%
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
red–yellow
</td>
<td class="highlight_" rowspan="" colspan="">
60%
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
yellow–grey
</td>
<td class="highlight_" rowspan="" colspan="">
80%
</td>
</tr>
</tbody>
</table>

In other words, I assumed that a sensor reading less than 40% would indicate black, 40–59% would be red, 60–79% yellow, and above 80% grey.

These values were used in my first version of `Noisy_line_follower`. Open this program and run it a few times. You should find that when you run this program Simon gets stuck before completing the route. If it keeps going, try rerunning the program until Simon does get stuck. 
<!--ITQ-->

#### Question

What do you think has gone wrong?


#### Answer

See the discussion in the next section.
<!--ENDITQ-->
