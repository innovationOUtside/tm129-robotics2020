#!/usr/bin/env bash

if [ ! -f /opt/firstrun.done ]; then
	touch /opt/firstrun.done
    echo "Please restart after first/build run..."
    echo ""
    echo ""
    echo "**************************************************************"
    echo "************* TO CHECK O/S UPDATES ARE INSTALLED *************"
    echo "*************       RUN: vagrant reload          *************"
    echo "**************************************************************"
    echo ""
    echo ""
    echo "**************************************************************"
    echo "*************          TO PACKAGE THE BOX           **********"
    echo "*************   RUN: vagrant package --output NAME  **********"
    echo "**************************************************************"
    echo ""
    echo ""
    echo "**************************************************************"
    echo "*************               UPLOAD TO:              **********"
    echo "*************       https://app.vagrantup.com/      **********"
    echo "**************************************************************"
    echo ""
    echo ""

    
    #shutdown -r now
fi