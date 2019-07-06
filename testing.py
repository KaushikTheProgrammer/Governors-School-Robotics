#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

colorSensor = ColorSensor()
colorSensor.mode = 'COL-REFLECT'
val = colorSensor.value()
print(val)