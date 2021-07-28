Robotics Software Guide
=======================

Introduction
------------

The TM129 robotics block uses a virtualised computing environment (VCE) running inside a Docker container to simplify software deployment. The VCE is composed of a Linux machine that runs a range of pre-installed software applications and services necessary for the block that you can access via a recent web browser. The VCE can be installed on any computer capable of running the Docker applications.

The software installed in the VCE includes an interactive Python programming environment (Jupyter notebooks), various required Python packages and a simple two-dimensional web-based robot simulator.

The versions of the software and programming libraries used for this presentation of the module may not correspond to the most recent versions available as you study the module. You should not need to update the software contained within the virtual computing environment: in fact, doing so may break some of the activities. If urgent software updates are required, you will be informed how to perform these via messages posted to the Technical help forum and announced via a module News item.

### Outline structure of this guide

The TM129 _Robotics Software Guide_ contains the following information:

*   information on where you can find additional support, and guidance on where to look for or ask for help
*   a short introduction to the TM129 virtual computing environment
*   installing the virtual computing environment on your own computer – including testing your installation
*   backing-up your work
*   using other software with the shared folder content
*   working with your own datasets
*   getting started with the Docker terminal/command-line interface
*   how the Jupyter notebook server works
*   troubleshooting.

1 Before you start
------------------

### 1.1 Hardware requirements

The virtual computing environment can be installed onto any computer that can run the Docker application, such as a desktop operating system (Microsoft Windows, macOS, Linux) but not tablet computers or most Chromebooks. To run the virtual computing environment, you will need a 64-bit computer processor and at least 4 GB of memory. You will also need at least 20 GB of free disk space to store the virtual computing environment and the data files you will be working with as part of the block.

### 1.2 Browser requirements

You will be accessing several of the applications that run inside the virtual computing environment via a web browser. The robotics block makes considerable use of Jupyter notebooks that can be accessed using recent versions of Chrome, Firefox or Safari browsers; Internet Explorer and Microsoft Edge are _not_ officially supported and notebooks may not work correctly if you use them. For more information, see the official documentation: [Jupyter notebooks – browser compatibility](http://jupyter-notebook.readthedocs.org/en/latest/notebook.html#browser-compatibility).

### 1.3 Handling errors – don’t panic!

Hopefully, you should not see any error messages when installing or running the software provided for the practical sessions. On completion of each step everything should be working.

If it isn’t working, try to read through the error messages and see if you can tell what didn’t load properly. Most importantly of all, **don’t panic**.

You should try to make sure you have the virtual computing environment up and running at the beginning of the block so that if there are any problems then there is plenty of time to solve them.

Please remember when raising software issues that posting error logs can really help others to try to solve the problem. Saying ‘My software’s broken/doesn’t work/prints scary red or purple messages out’ is not helpful, although sharing those scary messages probably is! Most importantly of all, **don’t be embarrassed** about sharing error messages: they often contain the key to the solution of whatever problem caused them.

If you do encounter a problem, the next section ‘Where to go for additional support’ describes a general strategy for working through the problem and how to ask for help. A later section, [Troubleshooting](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=8), provides more specific guidance for working through particular sorts of issues with the different software applications.

#### Where to go for additional support

If you encounter any problems installing the VCE or accessing the services that it provides, or have problems running provided code or your own code, the first thing to remember is **don’t panic**: in many cases, you may be able to fix the problem yourself; in others, a readily available helping hand should be able to resolve your problem.

In general, you may find it useful to work through the problem in the following way:

*   First, check any error messages, if appropriate. Error messages often contain a clue as to what caused them, a common one being a command not being recognised because of a typographical error. Computers are very literal in what they do, so a misplaced comma or a single character out of place may be all that needs fixing.
    
*   Second, check the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum to see if there are any official announcements relating to the same problem, or whether any other students have posted similar issues. This forum is moderated and the forum moderators will answer any questions they can, or pass them on to the module team if they can’t. Appropriate responses will then be posted to the forum.
    
*   Third, if a problem similar to yours has already been reported, but the suggested solution does not work for you, reply to the suggestion. In your reply, explain what you tried and what did or did not happen, including any error messages, if available, either as copied text or as a screenshot. Provide details of your operating system, if relevant. Sometimes you might find that trying to explain the issue identifies the solution. In such a case, if you think the problem may be a common one, you may want to post a message to the forum explaining the error you encountered and how you fixed it.
    
*   Fourth, if your problem has not already been identified, post a message to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum. Give the message a clear title that identifies the problem. Include in the body of the message a description of what you did and what did or did not happen, including any error messages, if available, either as copied text or as a screenshot. Once again, provide details of your operating system and/or browser, if appropriate. As before, you may find that trying to explain the problem reveals the solution. If you think that sharing the issue – and the solution you discovered – may be of some help to others, please do so via the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum.
    
*   Fifth, if you are struggling with identifying what the problem is and would find it useful to talk to someone, get in contact with:
    
    *   the [OU Computing Helpdesk](https://help.open.ac.uk/asking-for-help-with-it), for general IT and software installation enquiries
        
    *   your tutor, by phone or email or other agreed contact method for issues specifically about taught content and practical activities within the module.
        

To give yourself the best chance of resolving any issue in a timely fashion, _plan ahead_. The assignments require you to make use of the VCE, so don’t leave it until the last minute to try the VCE for the first time.

More specific guidance for working through issues related to particular software elements can be found in [Section 8 Troubleshooting](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=8).

### 1.4 Updates and upgrades

In putting together the VCE, we have tried to ensure that all the software packages and their interconnections run smoothly. Some of the configuration is software version specific. So, you are strongly encouraged not to update or upgrade any of the software packages installed within the TM129 VCE unless instructed to do so by the module team. Software updates and upgrades occasionally introduce changes that result in undesirable software behaviour, sometimes known as ‘breaking changes’, that cannot always be predicted in advance. Information regarding any critical updates or changes recommended by the module team will be distributed via the module forums.

### 1.5 Creating your own version of the TM129 virtual computing environment

The TM129 virtual computing environment incorporates several inter-dependent software packages and applications. The self-contained virtual computing environment Docker container has been developed to provide a ‘ready-to-use’ environment that contains all the software you need to complete the robotics block.

If you want to build you own version of the environment, **which is _not_ required for the module, and is _not_ recommended in most cases**, the original environment definition files can be found in [this GitHub repository](https://github.com/innovationOUtside/tm129-robotics2020/).

As well as installing the required Python packages via the [ou-tm129-py](https://github.com/innovationOUtside/ou-tm129-py) requirements package, the repository also contains scripts that install a range of Jupyter notebook extensions and sundry other packages.

Note that the module team are unlikely to be able to support students creating their own environments. Community support may be solicited by raising issues directly via the original GitHub repositories.

2 A short introduction to the TM129 virtual computing environment
-----------------------------------------------------------------

As you will be making use of a range of third-party software tools, applications and programming libraries as part of the robotics block of TM129, we have decided to distribute the software pre-installed into a virtual computing environment (VCE).

The VCE can be run on your own computer as a ‘local VCE’ and may also be available as an OU hosted environment (which we might refer to as a ‘hosted VCE’; check the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum for availability). It is also possible for you to run your own remotely hosted VCE (a ‘remote VCE’).

The local VCE runs under the Docker application as a _guest_ Linux (Ubuntu) operating system on your own computer (the _host_ operating system). The virtual machine running inside the local VCE operates in a ‘headless’ mode (that is, without a graphical desktop interface) and runs a variety of application services. The applications are exposed as interactive, graphical web applications via an HTTP interface that you can access through a web browser running on your own host computer.

The local VCE shares a folder, TM129VCE, with the host computer. We refer to this as the ‘TM129 shared folder’. The contents of this folder are visible to both the host computer and the local VCE (that is, the guest machine); they also remain visible on the host even if the guest machine is not running. The shared folder thus provides a way of passing files from your host machine into the local VCE, as well as getting files (such as backup files) out of the local VCE and onto your host computer. Figure 1 broadly describes the architecture of the TM129 local VCE and its relationship with your host operating system.

![Described image](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/c634556c/tm351_sg_f001.eps.png)

Figure 1 Overview of the architecture of the TM129 virtual computing environment

[Long description](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&extra=longdesc_idm45625717896576&clicked=1)

The TM129 VCE provides access from the host computer to Jupyter notebooks on the local VCE via a web browser. A Jupyter notebook is an interactive environment for writing, executing and capturing the output of Python code.

The notebooks can be accessed from a web browser using the URL [http://127.0.0.1:8129](http://127.0.0.1:8129) (or on some systems [http://localhost:8129](http://localhost:8129)).

### Browser favourites or bookmarks

To make it easier to access the Jupyter notebooks, we suggest that you add a browser bookmark for the Jupyter service.

3 Installing the TM129 virtual computing environment
----------------------------------------------------

These instructions describe how to:

*   download and install the Docker application and the TM129 virtual computing environment Docker container image, which contains all the software applications needed for the robotics block
*   create the _TM129 shared folder_, which contains a range of resources such as the notebook files used for the practical programming exercises, which are visible to both the host operating system and guest virtual environment.

To familiarise yourself with the installation sequence, we recommend that you read through the installation process for your host operating system and the description of testing your installation at least once before carrying out the process on your own computer.

### 3.1 Microsoft Windows 10

For Windows 10 Pro, Enterprise and Education users, follow the instructions on the Docker website for how to [Install Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/). This will require you to:

*   download the Docker installation package
    
*   double-click the installation package to run it
    
*   check your virtualisation settings:
    
    *   [enable Hyper-V settings](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v#enable-the-hyper-v-role-through-settings) if they are not already enabled
        
*   start the Docker application:
    
    *   search for Docker, and select Docker Desktop in the search results.
        

For Windows 10 Home users, follow the instructions on the Docker website for how to [Install Docker Desktop on Windows Home](https://docs.docker.com/docker-for-windows/install-windows-home/). This will require you to:

*   [check your version of Windows 10](https://support.microsoft.com/en-gb/help/4027391/windows-10-see-which-version-you-have) (version 2004 or higher is required)
    
*   check that hardware assisted virtualisation is supported and enabled ([hardware assisted virtualisation diagnostics tool](https://www.microsoft.com/en-us/download/details.aspx?id=592)).
    
    *   If virtualisation is available and not enabled, you will need to enable it. The actual approach may depend on your computer, but general guidance can be found here: [How can I enable virtualisation (VT) on my PC?](https://support.bluestacks.com/hc/en-us/articles/115003174386-How-can-I-enable-virtualization-VT-on-my-PC-)
        
*   download and install the [WSL2 Linux Kernel update](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)
    
*   download the Docker installation package, double-click it and follow the installation prompts, making sure you select the Enable WSL 2 Features option on the Configuration page
    
*   start the Docker application:
    
    *   search for Docker, and select Docker Desktop in the search results.

If you are running an earlier version of Windows than Windows 10 Pro / Enterprise / Education / Home (2004+), then you may still be able to run Docker using the [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/). This application is due to be retired in late 2020, but it may hang around for a little while after that.

If your computer cannot run Docker, or you have problems getting Docker working, then please contact your tutor for details of how to access an online version of the TM129 VCE.

All Windows users should now be able to download the VCE container image from the Docker Hub.

#### Accessing a terminal command-line interface

To run Docker commands on the command line, you will need access to PowerShell.

In Windows 10, click on Start and start typing PowerShell into the search bar. Open the PowerShell application that should be listed as a result.

#### Downloading the VCE Docker image

Using PowerShell, run the command:

docker pull ousefulcoursecontainers/ou-tm129:current

This will download a Docker container image from which individual Docker containers can be instantiated. The download may take some time (up to 20 minutes depending on your network connection). You should only need to download the original image once.

To share files between your host computer and the VCE, we recommend you create a folder at the following standard location:

C:\\Users\\your-username\\TM129VCE

Jupyter notebook files, data files and other project files downloaded from the module website or created otherwise can be placed inside the TM129VCE folder and will be available inside the VCE. Files saved to the shared folder from the VCE are saved to the host desktop and will persist even if the container is stopped or destroyed.

When you have completed installing the TM129 virtual computing environment, move to [Section 3.4 Creating the VCE container](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=3.4).

### 3.2 Apple macOS

Apple Mac users should follow instructions on the Docker website for how to [Get started with Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/).

This will require you to:

*   download the Docker installation package
*   double-click the installation package to run it
*   start the Docker application.

You should now be able to download the VCE container image from the Docker Hub.

#### Accessing a terminal command-line interface

To run Docker commands on the command line, you will need access to a terminal.

Open the Applications folder and find the Utilities folder inside it. The Terminal application should be in that (Applications/Utilities) folder. Drag the Terminal onto the Dock so you can access it more easily in future.

#### Downloading the VCE Docker image

From a terminal, run the command:

docker pull ousefulcoursecontainers/ou-tm129:current

This will download a Docker container image from which individual Docker containers can be instantiated. The download may take some time (up to 20 minutes depending on your network connection). You should only need to download the original image once.

To share files between your host computer and the VCE, we recommend you create a new folder on your computer called TM129VCE (for example, in your Documents folder).

Jupyter notebook files, data files and other project files downloaded from the module website or created otherwise can be placed inside the TM129VCE folder and will be available inside the VCE. Files saved to the shared folder from the VCE are saved to the host desktop and will persist even if the container is stopped or destroyed.

When you have completed installing the TM129 virtual computing environment, move to [Section 3.4 Creating the VCE container](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=3.4).

### 3.3 Linux

Linux users may find that Docker is already installed as part of their Linux distribution. If it is not already installed, then find the appropriate package distribution for your particular flavour of Linux from the [Install Docker Engine](https://docs.docker.com/engine/install/) page on the Docker website.

You should now be able to download the VCE container image from the Docker Hub.

#### Accessing a terminal command-line interface

To run Docker commands on the command line, you will need access to a terminal.

In the Applications Menu, the Terminal can usually be found in the System or Accessories menu area.

#### Downloading the VCE Docker image

From a terminal, run the command:

docker pull ousefulcoursecontainers/ou-tm129:current

This will download a Docker container image from which individual Docker containers can be instantiated. The download may take some time (up to 20 minutes depending on your network connection). You should only need to download the original image once.

To share files between your host computer and the VCE, we recommend you create a new directory on your computer called TM129VCE.

Jupyter notebook files, data files and other project files downloaded from the module website or created otherwise can be placed inside the TM129VCE directory and will be available inside the VCE. Files saved to the shared directory from the VCE are saved to the host desktop and will persist even if the container is stopped or destroyed.

When you have completed installing the TM129 virtual computing environment, move to [Section 3.4 Creating the VCE container](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=3.4).

### 3.4 Creating the VCE container

The VCE is started and stopped using the Docker command-line interface. This interface also supports downloading Docker container images, running and managing Docker containers instantiated from those images, managing port forwarding between containers and host machines, and establishing shared folders that are visible inside guest containers as well as on the host operating system.

Although we can download a Docker image and then launch a corresponding Docker container from it in a single step, it is often convenient to _pull_ the Docker image prior to running a container based on it:

docker pull ousefulcoursecontainers/ou-tm129:current

If you haven’t already pulled the image, then the docker run command will automatically download it for you.

A VCE container can then be launched from the command line using the following commands depending on your platform.

**You should only run the docker run command once.**

**If you see an error message when running the command, check [Section 8 Troubleshooting](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=8).**

#### Windows users (PowerShell)

Change directory to the directory containing your TM129VCE directory. For example, if you created C:\\Users\\your-username\\TM129VCE

run the command:

CD \\Users\\your-username\\TM129VCE

Then run the following command:

docker run --name tm129vce -d -p 8129:8888 -v $pwd\\:/home/jovyan/shared -e JUPYTER\_TOKEN="letmein" ousefulcoursecontainers/ou-tm129:current

#### macOS and Linux users

Change directory to the directory containing your TM129VCE directory. For example, if you created /Users/your-username/Documents/TM129VCE

run the command:

cd /Users/your-username/Documents/TM129VCE

or

cd ~/Documents/TM129VCE

Then run the following command:

docker run --name tm129vce -d -p 8129:8888 -v "$PWD/TM129VCE:/home/jovyan/shared" -e JUPYTER\_TOKEN="letmein" ousefulcoursecontainers/ou-tm129:current

In general, the commands will be the same across platforms. The differences come from the way in which the paths to folders/directories for volumes mounted from the host desktop into the launched container are specified.

The VCE container can be controlled more generally by issuing commands from a terminal / command prompt on the host computer. The core commands are as follows, although they may be modified using various flags:

Action

Terminal command

Pull container image

docker pull IMAGENAME

Create a container from an image using a specified container name

docker run --name CONTAINER\_NAME IMAGENAME

Stop container

docker stop CONTAINER\_NAME

Start a previously stopped container

docker start CONTAINER\_NAME

Restart a container

docker restart CONTAINER\_NAME

Delete a container

docker rm CONTAINER\_NAME

Show running containers

docker ps

Show specific running container

docker ps --filter "name=CONTAINER\_NAME"

Show ports exposed by a container

docker port CONTAINER\_NAME

Run a command inside a container

docker exec -it CONTAINER\_NAME COMMAND

Access the command line inside a container

docker exec -it CONTAINER\_NAME /bin/bash

List all containers

docker container –ls --all

The following flags may also be used with the docker run command:

Action

Flags

Create container name

\--name CONTAINER\_NAME

Specify volume mount points

\-v/--volume PATH/ON/HOST:/PATH/IN/CONTAINER

Port mapping

\-p/--publish HOST\_PORT:CONTAINER\_PORT

Automatically remove container when it exits

\--rm

Run container in background

\-d/--detach

Set environment variable inside container

\-e/--env ENV\_VARIABLE="ENV VALUE"

Just like a typical computer, the VCE is first ‘booted’ or ‘powered up’ and various services are started inside it. It may take a few seconds for them all to start up.

Once running, your VCE can be stopped and restarted.

Once you have created the Docker container, you can start and stop it either from the command line (Windows/macOS/Linux) or via the Docker Dashboard (Windows/macOS) as explained in the following section.

The docker stop tm129vce command is the equivalent of a shutdown command, so the VCE will go through a controlled shutdown. A previously stopped container can be restarted using the command docker start tm129vce.

If the VCE enters an error state (the equivalent of a crash), then the docker restart tm129vce command will attempt to stop and restart the VCE).

In extreme circumstances, the internal state of your container may get damaged beyond repair, with the result that the container cannot successfully be restarted. You can force its deletion using the command docker rm --force tm129vce. After removing the container, enter the original docker run command again to generate a new instance of the container.

This approach can also be used to recreate a new environment if you uninstall or otherwise damage any of the services that run inside the container.

Deleting the container will not delete the files in the shared folder. They will persist in the shared folder on the host and can be shared back into a newly created replacement container.

The docker pull command pulls a reference image from an online repository onto your computer. You can create a running Docker container from this image using the command line or the Docker Dashboard (Windows/macOS only).

#### Using the Docker Dashboard (Windows/macOS)

##### Opening the Docker Dashboad

###### Windows users

Open the Docker Desktop menu by clicking the Docker icon in the Notifications area (or System Tray): ![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/466ef3ee/docker_whale.png).

###### macOS users

From the Docker menu (opened via the Docker whale icon ![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/466ef3ee/docker_whale.png) in the menu bar at the top of the screen), select Dashboard.

##### Managing an existing container from the pulled image

You can start, stop and restart a container from the Containers / Apps tab in the Docker Dashboard application. Select the tm129vce container from the container list and use the icons to manage the container:

start/stop the container

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/7ccf2a9b/docker_start32.png) ![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/d2efdf56/docker_stop32.png)

restart the container

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/5c49dcca/docker_restart32.png)

open in browser to open the notebook server in your web browser

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/e0c1e774/docker_open_in_browser32.png)

Other options include:

CLI to access the command line inside the container

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/5c79a44e/docker_cli32.png)

Delete to delete the container (a replacement container can then be created by re-running the original docker run command)

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/668224b1/docker_delete32.png)

### 3.5 Testing your installation

After you have installed the TM129 VCE and shared resources, start the VCE using the provided docker run command.

Once the VCE has started, test that the Jupyter notebooks are running correctly by trying to access them from your web browser.

By default, the notebooks should be viewable via [http://127.0.0.1:8129](http://127.0.0.1:8129/) (or [http://localhost:8129](http://localhost:8129/)). On the first run, you should see a start page asking for a password or token. Use the token you provided as the JUPYTER\_TOKEN value in the docker run command (by default, letmein). When accessing the notebooks thereafter, you should not need to enter the password/token again.

Having successfully negotiated the token challenge, you should be presented with the notebooks folder home page.

![Described image](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/df33f73c/tm129_robotics_software_guide_fig02.png)

Figure 2 An example of the notebooks folder home page. The actual directory file path and file listing is indicative only.

[Long description](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&extra=longdesc_idm45625717705008&clicked=1)

If the Jupyter notebook server application is not available at its default address, there are three possibilities:

1.  the application is _not_ running
2.  the application _is_ running, _but_ on an incorrectly configured port inside the VCE
3.  the application _is_ running, and on the correct port, _but_ the port or the proxy used to expose it is being blocked in some way.

See [Section 8 Troubleshooting](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=8) for more information.

#### Accessing the practical activities

Once you have visited localhost:8129 through your browser, you should see a listing of different folders. Tick the checkbox to select the one named ‘content’. In the toolbar, select Move, and enter /shared in the pathname box as shown in Figure 3. This will set up a shared directory that allows files to be shared between your local machine and the container, and vice versa.

![Described image](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/7630df78/tm129_robotics_software_guide_fig02a.png)

Figure 3

[Long description](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&extra=longdesc_idm45625717690816&clicked=1)

You can access each week’s practical activities through the notebook home page. Click on the ‘shared’ folder, and then click on the ‘content’ folder. You should now see a list of notebook folders starting with ‘01. Introducing notebooks and the RobotLab environment’. Within each folder are a number of notebooks for you to work through during each week of the block. Follow the guidance on the study planner for a reminder as to which notebooks you should be studying each week.

If you encounter permissions-based problems when trying to move files into the shared folder or creating files or folders from the notebook server homepage, then check the file permissions. From a command code cell, list the directories set in your home directory, along with their permissions, by running the command:

ls -l ~

If you notice that any of the files have the user:group field set to root root rather than jovyan jovyan, reset the permissions by running the following command from PowerShell (Windows) or a terminal (Mac/Linux) on your host computer:

`docker container exec -itu 0 tm129vce chown -R 1234:1234 /home/jovyan/shared`

If you still see an error, restart your computer. You will also need to (re)start the container, either directly from the Docker Dashboard, or in PowerShell/your terminal by running the command:

`docker restart tm129vce`

On Windows, if you create a TM129VCE folder then run the docker run command in the same directory, you may see the error message:

`docker: Error response from daemon: mkdir C:\\WINDOWS\\system32\\TM129VCE: Access is denied.`

If you see this error message, delete the TM129VCE folder and execute the docker run command again. This will automatically recreate the folder.

4 Backing-up your work
----------------------

It is generally regarded as good practice to make backup copies of any files that you would not like to lose. This applies to the contents of the TM129VCE folder.

Any files you save in the Jupyter notebook environment not rooted on the `/home/jovyan/`shared directory (or any other directories you have mounted into from the docker run command) _will not be saved on your desktop_ although they will persist inside the container until the container is destroyed.

### Backing-up the TM129VCE folder

The TM129 VCE has been configured so that the TM129VCE folder you will be working in is shared with your own computer. That is, the files you will be working on in the VCE (guest operating system) can also be seen on your own (host) operating system, even when the VCE has been switched off.

Every so often, and quite frequently when working on your TMAs and EMA, you should make an archival copy of the TM129VCE folder on your own computer and store it in a safe place.

The contents of the TM129VCE shared folder should persist on your host computer in the face of most VCE issues, including restarting the container, or destroying it and creating a replacement. (That is not to say that you shouldn’t also back up the contents of that folder every so often though, including to other media or locations!)

5 Using other software with the shared folder contents
------------------------------------------------------

The TM129VCE shared folder contents are accessible from the host computer, which means you can access them directly from applications on your host machine. That is, you are not restricted to accessing them solely from the VCE. For example, in certain circumstances, you may want to download files from the internet onto your host computer and then pass them into the VCE, or edit data files using tools on your own host computer. (A simple text editor is also available via the Jupyter server: from the notebooks folder home page select Text File from the New drop-down menu on the right-hand side to create a new file.)

If you are familiar with other packages that manipulate specific file formats, and have them on your host computer, then you may find them useful for some data capture and data preparation tasks.

6 Getting started with the VCE command-line interface
-----------------------------------------------------

For the purposes of the TM129 robotics block, you should not need to access the VCE command line. However, if you find you do want to issue a command-line command or gain access to a command-line interface or terminal within the virtual machine, there are five main ways of doing this:

*   Within a notebook code cell, in the first line of the cell enter the command:

    `%%bash`
    
    Any additional code lines you enter into the cell will be interpreted as shell commands and executed as such when you run the cell.
    
*   Within a notebook code cell, prefix the command-line command you want to run with an exclamation mark (!). For example, to list the contents of the current directory, run the Linux/Unix ls command:
    
    `! ls`
    
*   Use the Jupyter interactive shell. From the notebooks folder home page, create a new terminal by selecting Terminal from the New drop-down menu on the right-hand side as shown in Figure 4.
    
    ![Described image](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/87e597db/tm351_sg_f004.eps.jpg)
    
    Figure 4
    
    [Long description](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&extra=longdesc_idm45625710349184&clicked=1)
    
*   Via a command line / terminal / command prompt on your host computer, change directory to the TM129 shared folder and then run:
    
    `docker exec -it tm129vce /bin/bash`
    

The Docker container that houses the VCE is running a version of Linux. The TM129 operating systems block introduces the Linux command line more formally.

The table below provides a quick summary of Linux/Unix commands you might find useful. Don’t worry if these commands are new to you: we will introduce them in slightly more detail as and when they are required in the block. However, if you have the opportunity to do so, you will find that gaining some proficiency in working with the Linux/Unix command line will stand you in good stead for a wide variety of data handling and system administration tasks.

Command

Description

`pwd`

Show the path to the current working directory (folder).

`cd PATH`

Change directory to the specified path (where .. signifies ‘parent of’ and a single . represents the current directory).

`ls`

List files and folders.

`ls /home/jovyan`

List contents of the specified directory. Inside the VCE, the /home/jovyan path is the path to the shared folder.

`head PATH/FILENAME`

Preview the first 10 lines of the specified file.

`tail -n 20 PATH/FILENAME`

Preview the last 20 lines of the specified file.

`man COMMAND`

Display manual pages for _command_, e.g. man pwd.

`wget URL`

Download the file from the specified URL to the current directory.

`tar -xvf FILENAME`

Uncompress and unarchive files from a _.tar.gz_ or _.tgz_ file.

7 How the Jupyter notebook server works
---------------------------------------

When you open a new notebook, the notebook server starts a new Jupyter kernel running an IPython process associated with the path and filename used to locate that notebook. The code cells in the notebook then talk to that process.

If you open the same notebook in more than one browser tab (which is not necessarily a sensible thing to do!), all copies of the notebook will access the same Jupyter kernel process. You can see this if you set a variable value in a notebook in one tab: you will be able to display the value in the notebook in the other tab. (Run a cell containing a=5 in one tab, and run a cell containing print(a) in a second tab – the same Jupyter kernel process is visible in both instances of the notebook.)

If one of the tabbed copies of the notebook is saved, then the other may pop up an alert noticing the difference and ask what you want to do about it. Generally, it’s a good idea to avoid this problem by only opening a given notebook in a single tab.

The Jupyter kernel process that started when you opened the first notebook will continue to run after you have closed all the tabs containing the notebook. You can see this when you look at the notebooks folder home page. If you want the process to stop, then you need to explicitly shut down that process. If you don’t shut it down, then any state associated with the process will be as it was, so if you reopen the notebook and enter a it should still be set to 5.

If you hibernate your computer and then wake it up again, any running Jupyter kernel processes should just hibernate and still retain their previous state. If you stop a notebook, either from the notebooks folder home page or by stopping and restarting the VCE, then the Jupyter kernel process will be stopped and all states (as far as the process is concerned) will be lost.

So how does this all work? A running notebook comprises two things:

*   a JSON file, rendered as an HTML page in your browser
*   a kernel process that is accessed via the code cells (in the case of TM129, the default IPython Jupyter kernel is used, although kernels for other languages are also available).

The Jupyter kernel process contains the program state and handles the computation; the notebook is just a device that is used to write to and from the process.

The important thing to remember is that the notebook displayed in the browser provides a view onto the state of a Jupyter kernel process via the code cells. If the output of a code cell displays a particular value for a variable, for example, but the underlying kernel process has been stopped and then started again since that value was originally displayed, then the variable will not actually be set in the Jupyter kernel process.

A final important note: any changes to the cells visible in the browser, and therefore the running process, need to be saved if you want them to persist (i.e. for the notebook to remember the changes between processes). It is possible that you may attempt to close the browser tab for a notebook without the content changes having been saved. The browser will usually display a warning and offer you the option of staying on the page, or leaving the page – this warning will differ depending on your host browser, but will say something like ‘Are you sure you want to leave this page?’. This is a sign that the most recent changes to the page haven’t been saved – usually you want to stay on the page, click the save icon, then close the tab.

8 Troubleshooting
-----------------

While we have tried to ensure that the software installation process and all the software-related activities run smoothly, there is always a chance that you may encounter a problem or issue with the software. [Section 1.3 Where to go for additional support](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=1.3) describes a general strategy for working through problems or raising technical issues. This section describes more specific guidance for working through issues with particular software elements.

You shouldn’t need to work though the following unless there are specific problems that have occurred with the software for the robotics block. However, you may want to skim through this section after installing your software and treat it as reference material in case problems arise later.

### 8.1 Problems installing and/or running a local VCE

You will be using the TM129 VCE throughout the robotics block, so we suggest you run through the simple setup activities described in [Section 3.6 Testing your installation](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=3.5) as soon as you can. If you have problems installing Docker or the TM129 Docker container / VCE, please be sure to include details of your operating system when posting to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum.

You can check whether the TM129 VCE container is currently running by entering the command docker ps in a terminal / command prompt and looking for the container named tm129vce.

If the container is not running (you cannot see it reported as ‘Up’ for a certain period of time in the docker ps listing) or the services appear not to be running (your browser doesn’t connect to the service after you have entered the appropriate address, e.g. [http://127.0.0.1:8129](http://127.0.0.1:35180)) then _reload_ the VCE by issuing the terminal command docker restart tm129vce.

#### Issuing Docker commands on the command line

##### Microsoft Windows

To change directory to the desired location, open the command prompt and use the CD command, followed by the path to the directory (i.e. folder) you want to move to. To display the name of the current directory, enter CD without any parameters. To list the contents of the current directory, use the DIR command.

##### Mac and Linux

To change directory to the desired location, open a terminal and use the cd command, followed by the path to the directory (i.e. folder) you want to move to. To display the name of the current directory, enter pwd without any parameters. To list the contents of the current directory, use the ls command.

##### Error messages

When running the docker run command, if you see the error message:

`docker: Error response from daemon: Conflict. The container name "/tm129vce" is already in use by container "…". You have to remove (or rename) that container to be able to reuse that name.`

you have already created the container. You should be able to restart it using the command `docker restart tm129vce` or from the Docker Dashboard (Windows/macOS).

If you need to create a new instance of the container, delete the current instance by running the command `docker rm -f tm129vce` or using the Docker Dashboard (Windows/macOS), and then try running the docker run command again.

#### Recovering a Docker container after sleep

If your computer goes to sleep, the container will also be hibernated. When you wake your computer, the container and the services it is running should also wake up, although you may have to restart any Jupyter notebook kernels you left running. In rare cases, you may find that the container has got stuck somehow. In such a case, check whether the TM129 VCE container is currently running by entering the command docker ps in a terminal / command prompt and looking for the container named `tm129vce`.

If the container is not running (you cannot see it reported as ‘Up’ for a certain period of time in the docker ps listing) or the services appear not to be running (your browser doesn’t connect to the service after you have entered the appropriate address, e.g. [http://127.0.0.1:8129](http://127.0.0.1:35180)) then _reload_ the VCE by issuing the terminal command `docker restart tm129vce`.

#### Taking drastic action

You might want to take a backup of the TM129VCE folder and any database content (described below) before attempting the following.

If for any reason you need to delete a VCE container instance and create a replacement container from the original image, or update the Docker image and create a newly updated container instance, run the following command to stop and delete the container:

docker rm --force tm129vce

and then run the original docker run command again.

Running docker rm --force tm129vce will _not_ delete any of the contents of the TM129 shared folder.

### 8.2 Problems running the browser-accessed applications or database services

If you cannot see the notebooks folder home page (127.0.0.1:8129) in your browser, the first thing to check is that the VCE is running: on the command line, run the command docker ps --filter "name=tm129vce" or the more general docker ps to see whether the container is running. If the container is _not_ running, then restart it by issuing the command docker restart tm129vce.

You can then check the services have been started and where the services are running as described below.

#### Identifying what services are running

You can list the services that are running under the default user by running the following shell command in the VCE:

pgrep -fa -u jovyan

#### Identifying what host ports services should be running on

Within the VCE, applications publish services on port numbers associated with the ‘localhost’ network _inside_ the virtual environment. Docker then _forwards_ the traffic on published ports to another set of port numbers that are visible on the localhost network relative to the host. The localhost network within the VCE is _not_ the same network as the localhost network on the host. This is shown in Figure 5.

![Described image](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/c514f008/tm129_robotics_software_guide_fig04.png)

Figure 5

[Long description](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&extra=longdesc_idm45625710259872&clicked=1)

You can find out what port(s) are published by the container by running the following command via a command-line terminal on your host computer:

docker port tm129vce

The published ports for the VCE container will then be listed in the form GUESTPORT -> HOSTPORT. So, for example, the line 8888 -> 8129 declares that guest port 8888 (the Jupyter notebook server port) maps on to port 8129 on the host.

If the browser-accessed services do not appear to display properly in your browser, please include the browser type and version number in any related messages you post to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum.

You can inspect the ports associated with a particular process inside the VCE by running a shell command with the following form inside the VCE:

lsof -P -sTCP:LISTEN -i TCP -a -p PROCESS\_ID

You can list processes running inside the VCE, filtered using a particular search term, using commands of the form:

pgrep -fa -f SEARCH\_TERM

You can limit processes to processes run by a specific user (for example, the jovyan user) with commands of the form:

pgrep -a -u jovyan -f SEARCH\_TERM

If you can’t get a connection, try to restart the VCE (see [Section 3.4 Creating the VCE container](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=3.4)).

If your problem persists, post a relevant message, including any error messages, to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum.

### 8.3 Problems arising from working with large notebooks

If you have tried to display a large amount of data in a notebook cell then you may find that your browser struggles to display the notebook. You should first attempt to clear all the output cells using the notebook menu Cell > All Output > Clear. If you are entirely unable to run the notebook to access the menu, first try closing any other notebooks you have open then try opening the problem notebook. If that doesn’t allow the notebook to open, then using a command-line command you can run the problem notebook through a separate process that will clear all the cell outputs.

Open a terminal in the VCE; use the second, third or fourth methods listed in [Section 6 Getting started with the VCE terminal](https://learn2.open.ac.uk/mod/oucontent/view.php?id=1725861&amp;printable=1&section=6). Then cd to the TM129VCE folder, and issue the following command (all on one line):

jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True YOURNOTEBOOK.ipynb

By default, the clean notebook will be named YOURNOTEBOOK.nbconvert.ipynb. To clean the notebook and retain the same filename, add the flag \--inplace to the command line:

jupyter nbconvert --inplace --to notebook --ClearOutputPreprocessor.enabled=True YOURNOTEBOOK.ipynb

The notebook server may also run into memory problems if you have a large number of notebooks open containing large _pandas_ DataFrames. (_pandas_ DataFrames are held in memory.) Try stopping all the notebooks and then restarting the notebook you are currently working on. (You will need to rerun the code cells to restore the state of the variables.)

### 8.4 Problems running the Python code

If you have problems running Python code in the TM129 notebooks, or running your own code, read any error messages carefully to see if they point to the cause of the problem. You may also find it useful to check the relevant documentation, such as the _pandas_ documentation, or run a web search using key elements of any error messages that occur.

Technical Q&A sites such as [Stack Overflow](http://stackoverflow.com/) contain answers to a wide variety of ‘_How do I …?_’ style questions and are often well worth exploring. Results from searches on Stack Overflow can also be limited to relevant questions by adding appropriate tags to your query, such as _pandas_ or _python_.

If you continue to have problems, check the module forums to see if anyone else has encountered – and resolved – the same issue. You may also ask for support in the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum or from your tutor.

The OU Computing Helpdesk will not be able to help with detailed technical queries arising from the module practical activities, so please limit any module-content related enquiries to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum or your tutor. The OU Computing Helpdesk can help with more general computing matters, including some support for installation problems that might occur.

### 8.5 Finding version numbers for software in your VCE

There may be occasions, such as when troubleshooting or debugging problems, when you are asked to confirm which versions of software and Python packages you have in your VCE. The following notebook commands will show you how to find most of the key versions:

*   **VCE version:** run the following in a notebook code cell:
    
    ! cat ${CONDA\_DIR/version.txt
    
*   **Python version:** run the following in a notebook code cell:
    
    from platform import python\_version python\_version()
    
*   **_pandas_ Python package:** run the following in a notebook code cell:
    
    import pandas as pd pd.show\_versions()
    

### 8.6 Notebook initialisation

During troubleshooting or debugging you might be asked to report what is in the initialisation script that is loaded by default into every notebook when it is started.

To inspect the initialisation script, run the following shell command in a notebook code cell:

! head -n 50 $(ipython locate)/profile\_default/startup/tm129\_start.ipy

### 8.7 Notebook accessibility

The notebooks are rendered within a browser as HTML. Instructional text in notebook Markdown cells are directly readable by screen readers. Code cells are contained within HTML group elements and need to be internally navigated to.

Most of the Jupyter notebook features are keyboard accessible. Several optional extensions provide further support in terms of visual styling and limited audio feedback support.

If you struggle to use the simulator for any reason, including but not limited to incompatibility with any tools you may use to improve software access or usability, please raise an issue in the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum or contact your tutor.

The module team are exploring the use of audible indicators to provide alerts regarding the current execution state of a Jupyter notebook, as well as tools for generating automated textual descriptions of user-created data visualisation charts. Please email [tony.hirst@open.ac.uk](mailto:tony.hirst@open.ac.uk) if you are interested in helping us investigate these approaches further.

#### Keyboard interface

The Jupyter notebook interface supports a wide range of pre-defined keyboard shortcuts to menu and toolbar options. The shortcuts can be displayed using the Keyboard Shortcuts item from the notebook Help menu or via the Esc-H keyboard shortcut.

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/08fc2e0b/00_01_jupyter_nb_shortcuts.png)

Figure 6 The Jupyter notebook ‘Keyboard shortcuts’ dialogue box

You can also add additional shortcuts and/or edit exist shortcuts via the Edit Keyboard Shortcuts menu item as shown in Figure 7.

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/e64cd214/00_01_jupyter_nb_edit_shortcuts.png)

Figure 7 The Jupyter notebook dialogue box for editing keyboard shortcuts

The RoboLab simulator provides a range of keyboard shortcuts to customise the environment display and control certain simulator behaviours. (More details can be found in the actual activity notebooks.)

#### Visual appearance

If required, you can use the [jupyter-themes](https://github.com/dunovank/jupyter-themes) extension to modify the visual appearance of the notebooks. The extension has been pre-installed in the virtual environment. See the [jupyter-themes documentation](https://github.com/dunovank/jupyter-themes) for more information. If you encounter any issues trying to run the extension, post a question to the [Technical help](olink.php?id=1725861&targetdoc=Technical+help) forum.

##### Magnification

The apparent size of the notebook contents in general can be zoomed using standard browser magnification tools.

Alternatively, use operating systems tools such as Windows Magnify or the macOS Zoom Window, or other assistive software.

#### Audio support features

Some RoboLab programs ‘speak’. Where the speech is generated as a part of a program flow, a visual display of the spoken phrase will also typically be displayed at the time the phrase is spoken.

An experimental extension to provide screen reading support to the notebooks is available. If you would be interested in helping us further develop and test this extension, or raise accessibility issues or concerns either in general or with particular reference to specific extensions, please email [tony.hirst@open.ac.uk](mailto:tony.hirst@open.ac.uk).

#### Accessibility Toolbar (experimental)

The Jupyter environment includes an [accessibility toolbar extension](https://github.com/uclixnjupyternbaccessibility/accessibility_toolbar) that allows you to control the presentation style of the Jupyter notebook; for example, you can change the font style, size and spacing, the notebook background colour, and so on.

##### Enabling the Accessibility Toolbar

The accessibility toolbar extension is **disabled** in the RoboLab environment by default. To use the accessibility extension, you need to enable it first. You can do this from the Nbextensions tab on the notebook home page: tick the Accessibility Toolbar extension to enable the toolbar (Figure 8). When you open a new notebook, the toolbar should be displayed.

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/ee01c654/00_01_nb_extensions_accessibility.png)

Figure 8 The Jupyter Nbextensions tab showing the Accessibility Toolbar extension

Check the [accessibility toolbar documentation](https://github.com/uclixnjupyternbaccessibility/accessibility_toolbar#toolbar-summary) for more information.

All of the styles are saved into local storage when refreshing the page. This means that if you use notebooks on different servers with the same browser, the same accessibility settings will be applied to notebooks on all servers within which you have enabled the accessibility extension.

##### Controlling colours and fonts using the Accessibility Toolbar

If you wish to change the font and interface colours used in RoboLab to improve readability, the accessibility toolbar allows you to select the font style, size and colour. You can also modify the line spacing and spacing between individual characters as shown in Figure 9.

![](https://learn2.open.ac.uk/pluginfile.php/3204127/mod_oucontent/oucontent/1268731/7f55b304/dbd4a6c2/00_01_accessibility_display.png)

Figure 9

The font style applies to _all_ text elements within the notebook itself. This includes the contents of Markdown (text) cells, code cells and code cell outputs.

The toolbar can also be used to control the notebook’s background colour and the cell background colour.

You can also save a style you have defined from the Add new style… option in the Predefined styles menu. Once saved, it will be added to the menu list so you can apply it as required.

#### Other assistive software

Please contact your tutor if you discover that the material does not work with a particular screen reader or dictation system that you would typically expect to be able to use.

### 8.8 Notebook spell checking

When creating your own notebooks you can check the spelling of words within individual Markdown cells by double-clicking in the Markdown cell to set it to Edit mode, and then pressing the ‘tick’ button on the notebook toolbar. Any words in the cell not recognised by the spell-checker will be highlighted with a jagged red underline.

### 8.9 Windows performance issues

You may find that performance of your Windows computer degrades when running Docker under WSL2.

This is caused by WSL2 appropriating too much computational resource from your computer. The solution is to create a file called `.wslconfig` in `C:\\Users\\your-username\\` containing the lines:

`\[wsl2\] memory=4GB # Limits VM memory in WSL 2 to 4 GB processors=2 # Makes the WSL 2 VM use two virtual processors`

Using an account with admin rights, from a PowerShell command line, restart WSL2 by entering:

`Restart-Service LxssManager`

You should find that setting memory=2GB is enough to run the container although you may find things, particularly in the second half of the course, run more smoothly by setting memory=4GB.

### 8.10 Linux permission errors

If you are running Docker on a Linux computer, you may find that the Jupyter notebook server raises a _Permission Denied_ error if you try to create or save a notebook to one of the shared directories. Run the following command from the host command line to see if it repairs the permissions enough to allow you to save the files as required:

`docker rm -f tm129vce docker run --name tm129vce -d -p 8129:8888 -v "$PWD/TM129VCE:/home/jovyan/shared" -e JUPYTER\_TOKEN="letmein" --user 1234 ousefulcoursecontainers/ou-tm129:current docker exec -u 0 tm129vce chown -R jovyan /home/jovyan`

If you continue to see the Permission Denied error, check the [Technical help](olink.php?id=1725861&targetdoc=Technical+help)  forum for possible alternative solutions.

Copyright © 2020 The Open University