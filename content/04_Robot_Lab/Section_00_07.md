```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

# 7 The RobotLab Grand Prix challenge

<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">

![figure DCTM_FSS\content\Teaching and curriculum\Modules\T Modules\TM129\TM129 materials\Linux e2\_Assets\tm129_portfolio_activity_32.jpg](DCTM_FSS\content\Teaching and curriculum\Modules\T Modules\TM129\TM129 materials\Linux e2\_Assets\tm129_portfolio_activity_32.jpg)

Please note that you must complete and submit the following practical activity as part of your ePortfolio.
</div>

Open the `Grand_prix` program. Run the program and watch the simulated robot 'race' around the track (Figure 7.1).

The challenge is to create a program that makes the simulated robot go round the race track faster. You can do this either by writing your own program or by modifying mine.

If your program is appreciably faster than mine, or uses an interesting control strategy, you are encouraged to attach the file to a Cluster Group forum message to share with other students and your tutor.


TO DO - use Thruxton circuit map from Wikimedia Commons

![figure ../tm129-19J-images/tm129_rob_p6_f024.jpg](../tm129-19J-images/tm129_rob_p6_f024.jpg)


Figure 7.1 The RobotLab Grand Prix circuit


__TO DO: could we time this in some way? Perhaps as number of simulaor steps as well as real time? Hmmm... Could we do more general simulator performance / timing comparisons across different student computers?__

The RobotLab Grand Prix circuit. The track is a loop, with a series of curves and a long straight section. The track is a mid-grey line on a white background, with a dark grey bar across it at one point to represent the start and finish line. The light sensor registers 50% for the mid-grey line and 25% for the dark grey bar. A chequered flag and silver cup decorate the background at the top..

