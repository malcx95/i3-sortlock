#!/bin/bash

scrot /tmp/screen.png
python3 $HOME/Programming/sortlock/sortlock.py
i3lock -i /tmp/screen.png
rm /tmp/screen.png

