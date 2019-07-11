#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

centerLight = ColorSensor('in4')
centerLight.mode = 'COL-REFLECT'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

base_speed = 150
setpoint = 13
kP = 4

while True:
    lightOutput = centerLight.reflected_light_intensity
    
    error = lightOutput - setpoint
    rightMotorVal = base_speed + (error * kP)
    leftMotorVal = base_speed - (error * kP)

    print("light", lightOutput, "error", error, "rightMotor", rightMotorVal, "leftMotor", leftMotorVal)

    # rightMotor.run_forever(speed_sp=motorVal)
    # leftMotor.run_forever(speed_sp=motorVal)
    







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
