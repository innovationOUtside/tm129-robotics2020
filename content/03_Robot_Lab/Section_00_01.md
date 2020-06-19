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

# Introduction


Sensors are at the heart of robotics. A machine without sensors cannot be a robot in our terms. The human body is replete with sensors. Our five external senses – sight, hearing, touch, smell and taste – and internal sensing such as balance and proprioception (body awareness) are all marvellously sophisticated.

In Robot Lab Session 4 we are concerned with how a robot can use this sensory information to control its actuators. We will investigate a progression of control strategies:

1. dead reckoning – no sensor input 

2. reflex behaviour – sensors *linked directly* to motors according to the sense–act model

3. deliberative behaviour – actuation depends on *reasoning* about sensor information and other knowledge, according to the sense–think–act model.

The first control strategy, dead reckoning, is "open loop", since it does not use sensor input.

The second is the sense–act control strategy that you encountered in Study week 2, and we will illustrate it using versions of Braitenberg’s vehicles (also introduced in Study week 2).

Finally, there is the most complex control strategy, in which the robot deliberates on the sensor inputs in the context of other knowledge. This involves *reasoning*, as discussed in Study week 3. This corresponds to the way humans solve complex problems and plan actions in the long and short term.

