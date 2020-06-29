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
%load_ext nbtutor
```

<!-- #region activity=true -->
# 7 The RobotLab Grand Prix Challenge

The aim of this challenge is to create a program that makes the simulated robot go round a race track as quickly as possible. You can do this either by writing your own program or by modifying mine.

To complete this challenge, you should use the *Small_Robot* configuration.

The race track itself is modeled on the [Thruxton motor racing circuit](https://thruxtonracing.co.uk/) in Hampshire, UK and generated from an SVG representation of the circuit taken from Wikimedia Commons. One of the fastest Uk motor racing circuits, the  track is comprised of a closed a loop, with a series of gentle curves and long straight sections. The track itself is a black line on a white background, with a light grey bar across it at one point to represent the start and finish line. Two small red flags identify the (clockwise) direction of travel round the circuit.

If your program is appreciably faster than mine, or uses an interesting control strategy, you are encouraged to attach the file to a Cluster Group forum message to share with other students and your tutor.
<!-- #endregion -->

<!-- #region student=true -->
*Your design notes here.*
<!-- #endregion -->

```python student=true
%%sim_magic_preloaded --background Thruxton_Circuit -r Small_Robot

# YOUR CODE HERE
```

Try not to spend more that ten or fifteen minutes on this challenge. Identify one or two possible approaches that you would like to try out that you think might improve the performance of the robot and try them out.

As well as identifying new control strategies, changing parameter values within a control strategy you have already identified may also lead to performance improvements.

Good luck...:-)
