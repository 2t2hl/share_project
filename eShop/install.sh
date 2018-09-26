#!/bin/bash
# Set default python to version 3
update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Install pip for python 3
apt install python3-pip -y
# Uncomment following line to upgrade pip
#pip install --upgrade pip

# Create a symbolic link for pip3 to pip
ln -s /usr/bin/pip3 /usr/bin/pip

# Install a stable version of Django, can update later
pip install Django==2.0.5
pip install Django-oscar
pip install Django-compressor
pip install Django-paypal
pip install Django-oscar-paypal

# Start application server
./manage.py runserver
