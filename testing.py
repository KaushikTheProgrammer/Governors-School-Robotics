#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

colorSensor = ColorSensor()
colorSensor.mode = 'COL-REFLECT'

while True:
    val = colorSensor.reflected_light_intensity
    print(val)