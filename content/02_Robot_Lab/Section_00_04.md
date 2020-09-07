---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
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

# 4 Optional challenges


These challenges are more difficult, so we’ve made them optional. If you want more programming experience before tackling these challenges, then you can always come back to this section later in the block.


## Configuring the Simulator

To download code to the simulator, use one of the simulator magics.

For example, prefix a code cell with the `%%sim_magic_preloaded` block magic as the first line to download the code in the cell to the simulator.

You may also find the following switches useful when configuring the simulator via the magic:

- `-b BACKGROUND_NAME`: load in a particular background file;
- `-x X_COORD`: specify the initial x-coordinate value for the simulated robot;
- `-y Y_COORD`: specify the initial y-coordinate value for the simulated robot;
- `-a ANGLE`: specify the initial rotation angle for the simulated robot;
- `-p`: specify pen-down mode;
- `-C`: clear pen-trace.


### Challenge – Fitness training take&nbsp;3

Modify the program you developed for the *Fitness training take&nbsp;2* challenge so that the robot travels the same distance as the first traverse on the third and final traverse, and double the first distance on the second traverse.

Download your program to the simulator and run it to check that it performs as required.

<!-- #region student=true -->
*Make any notes to help you complete the task here.*
<!-- #endregion -->

```python student=true
# Add your code here...
# Remember to start the cell with some appropriate magic to downloc code to the simulator

```

<!-- #region student=true -->
*Make any notes / observations about how your programmed worked, or any issues associated with getting it to work, etc, to help you complete the task here.*
<!-- #endregion -->

### Challenge – Fitness training take&nbsp;4

Modify the program you developed for the *Fitness training take&nbsp;3* challenge so that the robot can easily be tasked with performing any number of traverses. On odd numbered traverses it should travel a short distance; on even numbered traverses it should travel twice that distance.

Download your program to the simulator and run it to check that it performs as required.

<!-- #region student=true -->
*Make any notes to help you complete the task here.*
<!-- #endregion -->

```python student=true
# Add your code here...
# Remember to start the cell with some appropriate magic to downloc code to the simulator

```

<!-- #region student=true -->
*Make any notes / observations about how your programmed worked, or any issues associated with getting it to work, etc, to help you complete the task here.*
<!-- #endregion -->
