# Updated docker container

If you __have not__ already downloaded the TM129 Docker container, follow the installation instructions in the Software Guide.


If you __have__ already downloaded and installed the TM129 Docker container, you will need to update it.


## Updating Instructions

(Note that the original image is still available as `ousefulcoursecontainers/ou-tm129:20J`.)

To update the environment, you will need to remove the original container, update the image, and then launch a new container:

```
docker rm -f tm129vce
docker pull ousefulcoursecontainers/ou-tm129:current
docker run -d -p 8129:8888 --name tm129vce -v "$PWD/TM129VCE":/home/jovyan/shared -v "$PWD/TM129VCE":/home/jovyan/shared ousefulcoursecontainers/ou-tm129:current
```

As well as updating the computational environment, including the simulator, the new container includes updated notebooks in the `content` folder.

When you enter the (new) container, you can copy the updated notebook files to a new folder on your computer.

On the notebook homepage, click to select the `content/` folder, then in notebook homepage toolbar select `Rename`, and enter `shared/updates` as the new folder name.

![](.images/shared-rename-updates.png)

You can now work with the updated notebooks in that directory, or move them into the original notebook directories to replace the original files.

If you have already annotated some of your notebooks, you may not want to lose the work contained in them. Rename your annotated notebooks or place them somewhere safe when copying the updated notebooks into the original notebook locations.

### Major changes

The majority of changes to the notebooks are minor corrections (typos etc.).

Significant changes are:

- one new notebook: `01. Introducing notebooks and the RoboLab environment/01.6 Working With Simulators.ipynb` This clarifies some of the odd behaviours you may see when working with the robot in the simulator
- major revisions to `02. Getting started with robot and Python programming/02.1 Robot programming constructs.ipynb` The revisions clarify how the motors operate and describe why the robot may sometimes behave in an unusual way... You really should work through this notebook again even if you've already looked at it
- in notebook `04. Not quite intelligent robots/04.2 Robot navigation using dead reckoning.ipynb`, clarification of what the robot does and doesn't know about it's location in the world (and why!)



