#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

rightLight = LightSensor('in1')
rightLight.mode = 'REFLECT'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

while True:
    right = rightLight.reflected_light_intensity
    print("right", right) 
    # Black
    if right < 30:
        # Turn Left
        rightMotor.run_forever(speed_sp=-230)
        leftMotor.run_forever(speed_sp=40)

    elif right > 50:
        # Turn Right
        rightMotor.run_forever(speed_sp=0)
        leftMotor.run_forever(speed_sp=-160)
    else:
        # Go Forward with left bias
        rightMotor.run_forever(speed_sp=-200)
        leftMotor.run_forever(speed_sp=100)
