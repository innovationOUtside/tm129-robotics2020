# 3 Runaround


In the story ‘Runaround’ in *I, Robot* there is an interaction between the potential due to the instruction given to collect selenium (Second Law: obey a human), and Speedy’s strong self-preservation potential (Third Law: protect its own existence). In this section you are going to see how such conflicting potentials interact in practice.

TO DO - use potential field background. I thought I had a programme for this somewhere? Hmm... in the Braitenberg case maybe? So how does that relate to this case? Should we do a finesse and have another layer - eg a light layer, that generates a gradient based layer that is invisible to viewer but visible to robot? Then we could reveal what the world looks like under that illumination?

Open the program `Runaround`. Ensure the robot is running in pen-down mode. You may also want to turn off the program trace by choosing the `Run | Trace` menu option. If this is on, RobotLab highlights the line of code currently being executed, but this can be distracting with a long program like this.

<a xmlns:str="http://exslt.org/strings" href="">Figure 3.1</a> illustrates the selenium pool, which is represented by the area coloured bright red in the centre of the image. The area of danger to the robot around the selenium pool is represented by the contour lines centred on the pool. The degree of danger is proportional to the amount of red. This decreases the further you are from the centre of the pool.


![figure ../tm129-19J-images/tm129_rob_p7_f008.jpg](../tm129-19J-images/tm129_rob_p7_f008.jpg)


Figure 3.1 The robot moving round the selenium field


The simulator background for the ‘Runaround’ program. The background is black with a bright red central patch representing the selenium pool, which grades into black. The robot’s start position was at bottom right and its trail shows that it first headed for the selenium pool. Then, as it approached first it veered away to one side, then curved back again. Its trail gradually settled into a circular path at a more or less constant distance around the pool. The robot appears considerably smaller than the standard configuration; the simulator is showing events at a different scale from normal.

The robot is sent out from the mining centre at the bottom right-hand corner of the image. In the story, the instruction to get selenium was rather casual, so in the program this is represented by the variable `strength_of_command`, which is set to 25%.

This command interacts with the threat to self-preservation potential, which increases as the robot gets closer to the selenium pool. In the simulation, the potentials reach an equilibrium, which results in the robot going round in a circle.
<!--ITQ-->

#### Question

What would happen if you increase the strength of command slightly, for example from 25% to 30%?


#### Answer

Try resetting the variable `strength_of_command` to 30%, and rerun the program. I would expect the robot to get closer to the pool, but eventually circle it at the new equilibrium distance.
<!--ENDITQ--><!--ITQ-->

#### Question

What would happen if you increase the strength of command greatly?


#### Answer

Try resetting the variable `strength_of_command` to 75%, and rerun the program. 
<!--ENDITQ-->
Explore the code to see how Asimov’s laws have been modelled. You will see that the program as written doesn’t include Asimov’s First Law (protect human life), so it is not possible to break the impasse in the way that Powell did in Asimov’s story.
<!--ITQ-->

#### Question

Does the simulated robot obey Asimov’s laws of robotics?


#### Answer

My answer would be ‘yes and no!’ 

There is code that models Asimov’s Second and Third Laws and the Second Law has priority over the Third Law, so this certainly complies with Asimov’s Laws, at least in part. There is no mention of the First Law in the code, but it would not be too difficult to extend the code to model the First Law in a similar way to the others. We would have to also invent a ‘human in danger detector’ that could provide potential values to model the strength of the First Law.

However, the robot doesn’t have a positronic brain and it is a long way from the sort of intelligent, adaptable robot that Asimov envisaged. A ‘human in danger’ detector doesn’t sound feasible.

Perhaps the best we can say is that, given the limitations of its sensors and capabilities, this robot’s behaviour is compatible with Asimov’s laws

What do you think? You might like to post your thoughts in the forums.
<!--ENDITQ-->
