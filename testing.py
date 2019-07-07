#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

lightSensor = LightSensor()
lightSensor.mode = 'REFLECT'

while True:
    val = lightSensor.reflected_light_intensity
    print(val)