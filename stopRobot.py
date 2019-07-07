#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

rightMotor.run_forever(speed_sp=0)
leftMotor.run_forever(speed_sp=-0)