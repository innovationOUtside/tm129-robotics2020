# tm129-robotics2020
Repo to explore the drafting of updated robotics activities for OU module TM129.

[![Binder](https://mybinder.org/badge_logo.svg)](https://gke.mybinder.org/v2/gh/innovationOUtside/tm129-robotics2020/master)

Presentation: [![Binder](https://mybinder.org/badge_logo.svg)](https://gke.mybinder.org/v2/gh/innovationOUtside/tm129-robotics2020/master?filepath=seminar_tm129_robotics_overview.md)

An HTML version of the materials in the repo is available here: [https://innovationoutside.github.io/tm129-robotics2020/](https://innovationoutside.github.io/tm129-robotics2020/). Note that this site may lag the materials in the repo by few days...

This repository defines the computing environment for the practical activities for the 20J update to the OU TM129 robotics block.

A Docker container image built from the repository using `repo2docker` is available on Dockerhub: [`ousefuldemos/tm129-robotics2020`](https://hub.docker.com/repository/docker/ousefuldemos/tm129-robotics2020)

## Getting Started
You can explore the contents of this repository via interactive Jupyter notebooks by clicking the *Binder* button above.

To run the environment on your own computer, you need to do the following:

- install Docker onto your computer; you can download the installation files from the Docker website: [Get Docker](https://docs.docker.com/get-docker/)

- open a terminal / command prompt in your desktop; from the command prompt, do the following:
  - create a working directory / folder to work in by entering the command: `mkdir TM129`;
  - change directory into that fold by running the command: `cd TM129`;
  - launch the docker container by running the command: `docker run --name tm129test -p 8129:8888 -v $PWD:/home/jovyan/notebooks  -e JUPYTER_TOKEN="letmein" ousefuldemos/tm129-robotics2020:latest`
  - stop (hibernate) the container with the command: `docker stop tm129test`
  - restart the container with the command: `docker restart tm129test`
  
When you run the `docker` command, several things will happen:
 
 - first, docker will download the container image from DockerHub (this may take some time but only happens the first time you try to run the container);
 - then, docker will launch the container and a Jupyter notebook server will start running inside it.
 
When the container is running, go to [`localhost:8129`](http://localhost:8129) in your browser (if that doesn't work, try [`127.0.0.1:8129`](http://127.0.0.1:8129)) and you should see a running notebook server there.

Use the token `letmein` to access the server (you should only need to do this once).
 
Any files in the local `TM129` directory on your host computer should appear in the `notebooks` folder in the notebook homepage directory listing.

## Teaching Materials

The repository also contains drafts of the practical activity teaching materials. These materials are "unpublished" and *©The Open University, 2020*; they are posted here purely to support commentary and review during development. The initial draft of the materials is essentially a recasting of the original materials and activities into a form that uses a new user environment (*Jupyter notebooks*) and new simulation environment ([`nbev3devsim`](https://github.com/innovationOUtside/nbev3devsim), based on [`ev3devsim`](https://github.com/QuirkyCort/ev3dev-sim)).
