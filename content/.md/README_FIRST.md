---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,.md//md
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

# Welcome the the TM129 Robotics Block

If you're reading this via the TM129 Virtual Computing Environment (the `TM129VCE`) you should be all set to go.

But first let's do a quick test to check everything's working.

Click in the text box below, which contains a line of programming code, and then click on the *Run* button in the tool bar at the top of the screen to execute the code.

If you don't see an output message, something is broken (but *DON'T PANIC*: check the *Technical Forum* and post a help message there if a relevant advice hasn't already been posted).

If you see a message saying something is missing, go to the section *Installing missing requirements* section below.

```python
from ou_tm129_py import test_install

test_install()
```

## Making the supplied notebook content visible on your computer desktop

The local TM129 VCE runs in a Docker container. If you ran the original `docker run` command with one or more volume mounting `-v` flags, or created the container from he docker Dashboard with shared directory volumes, you will be able to share files and directories between the VCE and your computer desktop.

If you mounted a directory in the container at `/home/jovan/notebooks` you should be able to see


## Installing missing requirements

So it seems that something might be missing. Click in the following code cell to select it, then click the *Run*:

```python
%pip install --upgrade ou-tm129-py
```
