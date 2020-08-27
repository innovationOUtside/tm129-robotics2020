#!/usr/bin/env bash

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


if [ ! -f /opt/jupyter_test_nb.done ]; then

   #Bake test notebooks into the VM
    cp -r $THISDIR/notebooks/ /opt/notebooks/

    NB_DIR=/vagrant/notebooks
    export NB_DIR

    mkdir -p $NB_DIR
    cp -r /opt/notebooks/. $NB_DIR/
    chown $NB_USER:$NB_GID $NB_DIR


    touch /opt/jupyter_test_nb.done
fi