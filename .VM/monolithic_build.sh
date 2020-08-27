#!/usr/bin/env bash

# This script is responsible for constructing the OU VM
# Child scripts are loaded using `source`
# This has the effect of making exported env vars available to them

#Set the base build directory to the one containing this script
BUILDDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

BINDERBUILDDIR=/vagrant/.binder

#Python / pip installer
# (should really precede this with python package installation?)
#https://stackoverflow.com/questions/49836676/python-pip3-cannot-import-name-main
PIP="python3 -m pip"
export PIP

PIPNC="python3 -m pip install --upgrade --no-cache-dir"
export PIPNC

#Keep track of build datetime
chmod u+x $BUILDDIR/version.sh
$BUILDDIR/version.sh

#Create users
OU_USER=oustudent
OU_UID=1129
OU_GID=100
export OU_USER OU_UID OU_GID

echo "Adding service user: $OU_USER"
useradd -m -s /bin/bash -N -u $OU_UID $OU_USER
#Add oustudent user to sudo group
usermod -a -G sudo oustudent

OU_USER_HOME="$(getent passwd $OU_USER | cut -d: -f6)"

#Note: the user is used to run Jupyter notebook and OpenRefine services
echo "..user added"

#Make Jupyter user same as the OU user
NB_USER=$OU_USER
NB_GID=$OU_GID
export NB_USER NB_GID

#...done users

echo "Create env vars..."
#PRESERVE ENVT VARS
ENV_VARS=/etc/profile.d/course_env.sh

#Note - for env vars to be available to py kernel in Jupyter notebook
# they need to be defined in the Jupyter service definition file
# Use: `Environment=MYENVVAR=/my/value` as part of `[Service]` definition.

echo "" >> $ENV_VARS
echo "# Environemnt variables for OU course user" >> $ENV_VARS
echo "OU_USER=$OU_USER" >> $ENV_VARS
echo "OU_UID=$OU_UID" >> $ENV_VARS
echo "OU_USER=$OU_USER" >> $ENV_VARS
echo "OU_GID=$OU_GID" >> $ENV_VARS
echo "NB_USER=$NB_USER" >> $ENV_VARS
echo "NB_GID=$NB_GID" >> $ENV_VARS
echo "" >> $ENV_VARS

echo "...env vars created"
#END ENVT VARS


#Just in case
cp $BUILDDIR/files/fix-permissions /usr/local/bin/fix-permissions
chmod g+w /etc/passwd /etc/group
#End user definitions

# Install packages
echo "Essential core Linux packages..."
apt-get update && apt-get upgrade -y && apt-get install -y python3-pip
echo "...essential core Linux packages installed"

echo "Required Linux packages..."
cat $BINDERBUILDDIR/apt.txt | xargs apt-get -y install
echo "...required Linux packages installed"

echo "Required py packages..."
$PIPNC certifi
$PIPNC git+https://github.com/innovationOUtside/ou-tm129-py.git
echo "...required py packages installed"

echo "postBuild..."
source $BINDERBUILDDIR/postBuild
echo "...postBuild executed"

######## Jupyter space #########
echo "Jupyter setup..."


#Define a custom config dir
JUPYTERCONFIGDIR=$(runuser -l $NB_USER -c '/usr/local/bin/jupyter --config-dir')

echo "Locating Jupyter directories..."
echo "   - JUPYTERCONFIGDIR: $JUPYTERCONFIGDIR"
mkdir -p $JUPYTERCONFIGDIR
chown $NB_USER:$NB_GID $JUPYTERCONFIGDIR

#Copy styling files
cp -r $BUILDDIR/../.jupyter/* $JUPYTERCONFIGDIR/
chown -R $NB_USER:$NB_GID $JUPYTERCONFIGDIR/
cp $BUILDDIR/config/jupyter_notebook_config.py $JUPYTERCONFIGDIR/jupyter_notebook_config.py

# Service setup
cp $BUILDDIR/services/jupyter.service /lib/systemd/system/jupyter.service

# Enable autostart
systemctl enable jupyter.service

# Refresh service config
systemctl daemon-reload

#(Re)start service
systemctl restart jupyter.service

#OU custom packages and extensions
#source $BUILDDIR/jupyter-custom/jupyter_ou_tutor.sh

#source $BUILDDIR/jupyter-custom/jupyter_ou_test_nb.sh
source $BUILDDIR/jupyter-custom/jupyter_ou_trust.sh
echo "...jupyter setup done"

# Tidy up package lists
echo "Tidy up..."
apt-get autoremove -y
apt-get clean -y
apt-get autoclean -y
rm -rf /var/lib/apt/lists/*
echo "...tidy up done"