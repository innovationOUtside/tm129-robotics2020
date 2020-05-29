# 5 Overcoming the edge ambiguity problem


Open the `Noisy_tracker` program. For this program I started from a different perspective. I defined a constant called `T_black_red`, where anything below this threshold is black. Similarly, anything above `T_red_grey` is grey.

My control strategy is based on these thresholds. For dark areas I apply more power to the right motor, for light areas I apply more power to the left motor.

I test for the red bar by counting the number of consecutive readings in the range 49–51%. If the number exceeds six, my program assumes that the red bar has been reached.

I spent quite a lot of time trying to get the speed parameters to work. Even so, my program is not perfect and the simulated robot sometimes goes astray.

If you can write a better control program than mine, attach it to a message and post it to the forum.

