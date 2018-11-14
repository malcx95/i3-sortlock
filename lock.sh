#!/bin/bash

scrot /tmp/screen.png
python3 /home/malcolm/Programming/sortlock/sortlock.py
i3lock -i /tmp/screen.png
rm /tmp/screen.png

