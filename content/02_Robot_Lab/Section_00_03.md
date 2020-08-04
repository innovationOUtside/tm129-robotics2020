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

# 3 RoboLab challenges


Here you are given a number of challenges to do. These challenges are a bit different from the activities you did earlier in RoboLab sessions. We leave you to work out the challenges for yourself, although you are encouraged to use the forums if you need help or if you want to share or discuss any of your ideas with other students.

The purpose of the challenges is to allow you to try your hand at writing your own RoboLab programs. Don’t spend too much time on this work. If you get stuck, take a break: it’s surprising how often a solution to a programming problem comes to mind if you take a few minutes away from the screen and the keyboard and do something completely different instead.

The challenges in the next notebook are more difficult and are completely optional. They generally require you to have had some computer programming experience before you started this module.

In the meantime, once you have finished this notebook, I suggest you take a well-earned break before going back to the website to complete Study week&nbsp;2.


### Challenge – Moving the simulated robot forwards

Write a program to make the simulated robot move forwards for two seconds. Download your program to the simulator and run it to check that it performs as required.

Remember to prefix the code cell with a magic command that will download the code to the simulator.

```python

```

### Challenge – Fitness training

Write a program to make the simulated robot move forwards a short distance and then reverse to its starting point, repeating this action another four times (so five traverses in all). Download your program to the simulator and run it to check that it performs as required.

Optionally, extend your program so that it speaks a count of how many traverses it has completed so far each time it gets back to the start.

<font color='red'>JD: The following need to be resolved.</font>

__TO DO - the original material specified a portfolio activity at this point (draw a triangle); that challenge has been dropped. Do we need a replacement challenge?__
    
__TO DO: tutor notes / examples on how to solve these challenges.__


```python

```

### Challenge – Making a countdown program

Write a program to make the simulated robot speak aloud a count down from 10 to 0, finishing by saying ‘OK’. Download the program to the simulator and run it to check that it performs as required.

```python

```

### Challenge – Fitness training take&nbsp;2

In the first fitness training challenge, the robot had to cover the same distance backwards and forwards five times.

In this challenge, the robot should only do three forwards and backwards traverses, but in a slightly different way. On the first, it should travel forward and backward a short distance; on the second, it should travel twice as far forward and backward as the first; on the third, it should travel three times as far forward and backward as the first.

Download your program to the simulator and run it to check that it performs as required.

```python

```
