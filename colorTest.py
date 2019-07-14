#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

detector = ColorSensor()
detector.mode = 'RGB-RAW'

while True:
    print(detector.value(0), detector.value(1), detector.value(2))