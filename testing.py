#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
import time

centerLight = LightSensor('in4')
#centerLight.mode = 'COL-REFLECT'

detector = ColorSensor()
detector.mode = 'COL-COLOR'

ballfinder = Sensor(address='in2:i2c8', driver_name='ht-nxt-ir-seek-v2')
ballfinder.mode = 'AC'

# ultrasonicSensor = UltrasonicSensor('in3')
# ultrasonicSensor.mode = 'US-DIST-CM'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

base_speed = 120
setpoint = 40

kP = 23

prevColor = 6
numGreen = 0
numRed = 0
detectedTime = 0
threshold = 10

line = False


def turnLeft():
    


while line:
    lightOutput = centerLight.reflected_light_intensity
    colorVal = detector.color
    currentTime = time.time() 
    
    error = lightOutput - setpoint
    rightMotorVal = base_speed + (error * kP)
    leftMotorVal = base_speed - (error * kP)

    if prevColor == colorVal and (colorVal == 3 or colorVal == 4) and currentTime > detectedTime + threshold:
        numGreen += 1
    else:
        numGreen = 0
    
    if numGreen == 10:
        Sound.beep()
        detectedTime = currentTime
    
    if prevColor == colorVal and colorVal == 5:
        numRed += 1
    else:
        numRed = 0

    if numRed == 5:
        line = False

    prevColor = colorVal

    # rightMotor.run_forever(speed_sp=-rightMotorVal)
    # leftMotor.run_forever(speed_sp=-leftMotorVal)

leftMotor.run_to_rel_pos(position_sp=770, speed_sp=200, stop_action='hold')

rightMotor.run_to_rel_pos(position_sp=-770, speed_sp=200, stop_action='hold')
# ballfinder.value()
