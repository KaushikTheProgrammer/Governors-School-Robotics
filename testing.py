#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

rightLight = LightSensor()
rightLight.mode = 'REFLECT'

leftLight = LightSensor()
leftLight.mode = 'REFLECT'

while True:
    right = rightLight.reflected_light_intensity
    left = leftLight.reflected_light_intensity
    print("right", right, "left", left)