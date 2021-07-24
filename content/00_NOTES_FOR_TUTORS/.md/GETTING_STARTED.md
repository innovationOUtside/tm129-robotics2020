---
jupyter:
  jupytext:
    formats: ipynb,.md//md
    notebook_metadata_filter: rise
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  rise:
    enable_chalkboard: true
    scroll: true
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Getting started

Welcome to the TM129 Robotics block practical activities.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
The practical activities are delivered through a new environment, *RoboLab*, that replaces the *RobotLab* application used in presentations prior to 2020J. *RoboLab* is an example of an `Open Computing Lab (OCL)` environment configured specifically to support the TM129 Robotics activities.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
The `Open Computing Lab` approach is being trialled on several Open University modules and aims to provide a common approach to delivering complex software and computing envronments on personal computers as well as via remotely hosted online servers.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
To install the environment, use the installation instructions that are provided for students.
<!-- #endregion -->

<!-- #region tags=["alert-danger"] -->
During the production process, and between module presentations, the Docker image used to distribute the robotics activity software may have been updated since you last used it. The online MyBinder <!-- JD: is MuyBinder still being used? --> run version of the environment will use the latest version of the environment as a matter of course. If you have previously downloaded the Docker container image to your own computer, you should regularly check to see whether it needs updates by running the command: `docker pull ousefuldemos/tm129-robotics2020:latest`.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## The Jupyter notebook environment

The teaching and learning materials used to support the activities are provided as Jupyter notebooks. 
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
Jupyter notebooks have been used to deliver practical activities in TM351 *Data management and analysis*, the OU-produced FutureLearn/OpenLearn unit *Learn to Code for Data Analysis*, materials which are also used in S818 *Space science*, and to support a brief, optional set of activities in TM112.

They will also be used in several modules currently in production including M269 *Algorithms, data structures and computability*, TM358 *Machine learning and artificial intelligence* and M348 *Applied statistical modelling*.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Originally developed to support computational research activities, Jupyter notebooks provide a cell-based web-based read-write-execute document editor that blends rich text, executable code and code outputs.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
Within text areas, code can by highlighted in a language sensitive way:
<!-- #endregion -->

<!-- #region -->
```python
def sayHello():
    print('Hello World')
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Code is executed in a ‘kernel’ shell environment running on a backend server.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
Kernels for a [wide variety of programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) are available; in TM129, we will be using a full Python kernel, as well as a simple in-browser Skulpt Python environment that runs code inside a simple in-browser 2D robot simulator.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
When a code cell is run, outputs can be printed or displayed, and any value returned by the last object in the cell object will be displayed as cell output.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
def sayHello():
    print('Hello World')
    return "done..."
    
sayHello()
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Using notebooks to support learning

The read-write-execute nature of Jupyter notebooks provides us with a medium that can be used to develop a wide range of active learning materials. Students are encouraged to take ownership of the notebooks, use them as guided materials, as well as in a curiosity driven, exploratory way, and annotate them as they would print materials.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
For example, students can:
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
- run simple interactive applications in the notebook
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
- run provided code examples and inspect code outputs
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
- edit and run their own code and produce their own code outputs
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
- edit the module text, from fixing minor typos as they work through the materials, to annotating the materials with their own comments and clarifications
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
- add predictions about what they expect a code fragment to do when it is executed, record their observations when it does, and reflect on how well their predictions matched their observations, and what they learned as a result. 
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Using notebooks to support direct teaching and tutorials

The Jupyter notebook environment we have provided includes a slideshow extension, [RISE](https://rise.readthedocs.io/en/stable/), that allows you to turn individual Jupyter notebooks into interactive slideshow presentations.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
As with the notebooks themselves, each slide includes editable text and code cells, can display interactive applications, and can be used to execute code fragments and display the resulting code output (including error messages...).

Notebooks are configured as slides through the addition of cell tags that control whether, and how, each cell in the notebook is to be treated in presentation mode.

Several of the notebooks, including this one, have been marked up as presentations. To run the slideshow, click once on the top cell in the notebook to select it as the starting point of the presentation, then click on the *Enter/Exit RISE Slideshow* icon (it looks like a bar chart) on the notebook toolbar. 
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Slides themselves are interactive in other ways.

For example, this notebook supports the presentation [chalkboard](https://rise.readthedocs.io/en/stable/customize.html#enable-chalkboard-capabilities) which allows you to draw on the slide directly.

(Click the pens in the bottom left corner of the slide to toggle the chalkboard mode.)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "skip"} -->
## What next?

If you are not familiar with Jupyter notebooks, please spend some time familiarising yourself with them.

We believe they provide a powerful tool to support teaching and learning and it’s still early days for us in finding out how to make most effective use of them.

If you have any ideas about how we can improve our current use of the notebooks, or make more effective use of them, please let us know.
<!-- #endregion -->
