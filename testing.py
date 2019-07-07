#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from simple_pid import PID

pid = PID(1, 0.1, 0.05, setpoint=45)

pid.output_limits = (-400, 0)

rightLight = LightSensor('in2')
rightLight.mode = 'REFLECT'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

base_speed = 200

while True:
    lightOutput = rightLight.reflected_light_intensity
    pidOutput = pid(lightOutput)

    rightMotor.run_forever(speed_sp=pidOutput + base_speed)
    







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
