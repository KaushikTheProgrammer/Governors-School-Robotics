#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

right = LargeMotor('outA')
left = LargeMotor('outD')

for x in range(100, 900):
    right.run_forever(speed_sp=x)
    left.run_forever(speed_sp=-x)
    sleep(0.05)
sleep(1)

right.stop(stop_action="hold")
left.stop(stop_action="hold")
