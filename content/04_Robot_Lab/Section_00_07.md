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
# 6 The RoboLab Grand Prix Challenge

The aim of this challenge is to create a program that makes the simulated robot go round a race track as quickly as possible. You can do this either by writing your own program or by modifying mine.

To complete this challenge, you should use the *Small_Robot* configuration.

The race track itself is modelled on the [Thruxton motor racing circuit](https://thruxtonracing.co.uk/) in Hampshire. It was generated from an SVG representation of the circuit taken from Wikimedia Commons. One of the fastest UK motor racing circuits, the track comprises a closed a loop, with a series of gentle curves and long straight sections. The track is modelled as a black line on a white background, with a light grey bar across it at one point to represent the start and finish line. Two small red flags identify the (clockwise) direction of travel round the circuit.

If your program is appreciably faster than mine<font color='red'>JD: OK, but what *is* your program?</font>, or uses an interesting control strategy, then share it via your Cluster group forum.
<!-- #endregion -->

<!-- #region student=true -->
*Your design notes here.*
<!-- #endregion -->

```python student=true
%%sim_magic_preloaded --background Thruxton_Circuit -r Small_Robot

# YOUR CODE HERE
```

Try not to spend more than ten or fifteen minutes on this challenge. Identify one or two possible approaches that you would like to try out that you think might improve the performance of the robot and try them out.

As well as identifying new control strategies, changing parameter values within a control strategy you have already identified may also lead to performance improvements.

Good luck... :-)
