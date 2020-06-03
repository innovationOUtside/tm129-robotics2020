---
jupyter:
  jupytext:
    notebook_metadata_filter: rise
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  rise:
    enable_chalkboard: true
    scroll: true
---

<!-- #region slideshow={"slide_type": "slide"} -->
# TM129 Robotics Refresh

Tony Hirst

Computing and Communcations

`tony.hirst@open.ac.uk`

`blog.ouseful.info`

`github.com/innovationOUtside`
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Not Demos

### `https://github.com/innovationOUtside/`

### and then:

### simulator package: `nbev3devsim`

### draft materials : `tm129-robotics2020`

Note: these are works in progress; I try to ensure that the current `master` works, but:

1. can't guarantee it...
2. my current WIP may be several days ahead of `master`
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## In The Beginning...

- T184 Robotics and the Meaning of Life (2003-2011)
  - 10 points, Relevant Knowledge / Technology short course programme
  - 50% online VLE teaching material, 50% computer desktop practicals
  
- TM129 Technologies in Practice (2013-)
  - Robotics module: T184, slightly revised
  - introduction to programming remit
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## RobotLab Practical Activities


![](presentation_images/robotlab_1.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Accessing Legacy Windows Apps Via a Browser


https://github.com/ouseful-demos/jupyter-desktop-server

![](presentation_images/JupyterLab_robotLab.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# TM129 Update — Replacing RobotLab

- T176 Engineering: professions, practice and skills 1
  - week long residential school
  - four day long activities including Robotics
  - robot activity originally used RobotoLab with Lego Mindostorms RCX robot
  - revised robot activity uses lego software with Lego EV3 robot

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Moving to Python

Python wrapper to Lego `ev3dev` Linux operating system

![](presentation_images/EV3DEV_Python_Simulator.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Updated Activity Model

![](presentation_images/tm129_environment.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## ev3devsim

- runs in the browser
- uses Skulpt
- implements a cut-down version of `ev3dev-py` as a Skulpt package

BUT

- no access to full SciPy stack;
- how do we provide instruction?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## The Naive Jupyter Way

- embed `ev3devsim` in a Jupyter notebook or JupyterLab IFrame window

Disadvantages:

- very loose coupling between teaching materials eg in notebook and simulator
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Naive Integration Example
<!-- #endregion -->

```python
from IPython.display import IFrame
IFrame('https://www.aposteriori.com.sg/Ev3devSim/index.html', width='100%', height=800)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Integrated Jupyter Way - `nbev3devsim`

![](presentation_images/nbev3devsim_model.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
Code entered into a magicked code cell is downloaded to the simulator when the code cell is run. The code is then executed / run in the simulator.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
##  `nbev3devsim` Widget

`jp_proxy_widget` wrapped version of `ev3devsim`

![](presentation_images/nbev3devsim_full.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nbev3devsim` Controls

![](presentation_images/nbev3devsim_controls.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nbev3devsim` Output Area

![](presentation_images/nbev3devsim_display.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nbev3devsim` Sensor View

![](presentation_images/nbev3devsim_sensor.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nbev3devsim` Code Display

![](presentation_images/nbev3devsim_show_code.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## `jp_proxy_widget` == `ipywidget` wrapper

- supports state transfer between notebook Python kernel and Javascript
- code is "downloaded" to the simulator from a magicked notebook cell
- simulator state, robot state and robot datalog contents are aviailbale to notebook Pyhton kernel

![](presentation_images/grabbed_data.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Virtual Machines All The Way Down

![](presentation_images/ev3-jupyter-arch.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
The VM situation is actually a little bit more complicated than that:

- there is a state return path *from* the `nbev3devsim` simulator running in the browser Javascript context back to the Jupyter mediated Pyton environment;
- the Jupyter Python environment, and the Jupyter server are running on a Linux o/s in a Docker container;
- the Docker applciation *might* be running on the host o/s, or it might be remote and being access over an intervening network.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Delivery Model — Open Computing Lab (OCL) — Aims

https://github.com/innovationOUtside/Open_Computing_Lab_Guide

-  provide module specific computational environments capable of running:
  - locally on students' own computers;
  - on OU hosted onlines servers;
  - on remote third party servers;
  - on personal home servers (eg Raspberry Pi).
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Delivery Model — Open Computing Lab (OCL) — Approach

- Docker containers
  - package and distribute arbitrary computational environments running arbitrary applications;
  - OU controls the computational environment (Docker runs "anywhere");
- Jupyter services:
  - providing single and multi-user access to browser accessed applications and environments;
  - support interactive and reflective read-write-execute activities.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Building the Tools of Production

- convert original materials to notebooks
  - OU-XML to markdown (TH OU-XML processor;
    - OpenLearn example: https://github.com/psychemedia/openlearn-publish-test
  - markdown to Jupyter notebook (`jupytext`)
- evolving the simulator throughout the update
- generating diagrams and simulator backgrounds
- quality tests
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### OU-XML Processing

Pipeline for:

- grabbing OU-XML
- parsing XML
- identifying and downloading image assets
- converting parsed XML into markdown or Jupytext-markdown
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Generating Simulator Backgrounds

![](presentation_images/generating_backgrounds.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Notebook Quality Checks

![](presentation_images/simple_nb_viz.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Evolving the Pedagogy

- notebooks are medium that support interactive *teaching* as well as *active and reflective learning*
- the medium is a computational medium and as such is malleable in our hands
  - _"everyone should learn to code..."_
  - custome notebook magics and extensions
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Activities

![](presentation_images/jupyter_answer_reveal.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Highlight Tutor Feedback

![](presentation_images/notebook_tutor_feedback.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Example Magics

- `nbev3devsim` magic
- flowchart diagram magic
- cell difference magic
- (TM351 entity relation diagram magic)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nbev3devsim` Magic

- `--background / -b`: specify the background option to load into the simulator; 
- `--robotSetup / -r`: define the pre-configured robot template to use;
- `--xpos / -x`: specify initial, default x-coordinate of robot for this activity;
- `--ypos / -y`: specify initial, default y-coordinate of robot for this activity;
- `--angle / -a`: specify initial, default angle of robot for this activity.

Flags (pass the following to force the specified behaviour):

- `--quiet / -q`: suppress the audio alert that from a successful download to the simulator (default: audible download alert);
- `--obstacles / -o`: enable obstacles(default: no obstacles; takes arg corresponding to predefined obstacle config (`Central_post`, `Square_posts`, `Wall`);
- `--ultrasound / -u`: show ultrasound rays (default: no rays);
- `--pendown / -p`: set the pen in the pen down position (default: pen up).
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## `flowchart.js` Widget and Magic

![](flowchart_js_magic.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `nb_cell_diff` Magic

https://github.com/innovationOUtside/nb_cell_diff

![](presentation_images/nb_cell_diff.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Example Extensions

- `empinken`
- *Tensorflow Playground* widget
- two column code cell
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `empinken` Extension — Toolbar Buttons

https://github.com/innovationOUtside/nb_extension_empinken

![](presentation_images/empinken_buttons.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### `empinken` Extension — nbExtension Configurator

![](presentation_images/empinken_config.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Tensorflow Playgrund Widget (WIP)

![](presentation_images/tensorflow_playground_widget.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Two Column Display

![](presentation_images/two_column_display.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Future Possible Developments (1)

- standalone browser experience
  - no use of Python shell
  - copy code to simulator vis JS or copy/paste
  - initially, no "extension" activities BUT possibility of using pyodide?
  
Advantages:

- presented without Jupyter dependency
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Future Possible Developments (2)

- extend range of how `nbev3devsim` is used in notebook
  - stripped down simulator window output as code cell output?
  - ...
- improved quality checks / support
  - command-line / interactive spellchecker
  - code quality checks
  - automated in-notebook code tests
<!-- #endregion -->
