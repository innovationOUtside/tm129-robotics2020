#!/usr/bin/env bash

#Path to shared notebook directory
NBDIRECTORY=/vagrant/notebooks

if  [ -d "$NBDIRECTORY" ]; then

    # Trust notebooks in notebook directory
    files=(`find $NBDIRECTORY/* -maxdepth 2 -name "*.ipynb"`)
    if [ ${#files[@]} -gt 0 ]; then
        jupyter trust $NBDIRECTORY/*.ipynb;
        jupyter trust $NBDIRECTORY/*/*.ipynb;
    fi

fi