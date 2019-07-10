#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

rightLight = LightSensor('in2')
rightLight.mode = 'REFLECT'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

base_speed = 200
setpoint = 35
kP = 2.0

while True:
    lightOutput = rightLight.reflected_light_intensity
    
    error = lightOutput - setpoint

    rightMotor.run_forever(speed_sp=base_speed + error * kP)
    leftMotor.run_forever(speed_sp=base_speed + error * kP)
    







    #     # Black
    # if right < 40:
    #     # Turn Left
    #     rightMotor.run_forever(speed_sp=-150)
    #     leftMotor.run_forever(speed_sp=150)

    # elif right > 50:
    #     # Turn Right
    #     rightMotor.run_forever(speed_sp=0)
    #     leftMotor.run_forever(speed_sp=-160)
    # else:
    #     # Go Forward with left bias
    #     rightMotor.run_forever(speed_sp=-175)
    #     leftMotor.run_forever(speed_sp=80)
    
    # # Black
    # if right < 40:
    #     # Turn Left
    #     rightMotor.run_forever(speed_sp=350)
    #     leftMotor.run_forever(speed_sp=-40)

    # elif right > 50:
    #     # Turn Right
    #     rightMotor.run_forever(speed_sp=0)
    #     leftMotor.run_forever(speed_sp=160)
    # else:
    #     # Go Forward with left bias
    #     rightMotor.run_forever(speed_sp=175)
    #     leftMotor.run_forever(speed_sp=-80)
