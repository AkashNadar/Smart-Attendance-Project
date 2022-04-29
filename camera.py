#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.vflip = True
camera.start_preview()
sleep(2)
camera.capture('picture.jpg')
camera.stop_preview()
