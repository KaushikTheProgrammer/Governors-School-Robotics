#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
import time

centerLight = LightSensor('in4')
#centerLight.mode = 'COL-REFLECT'

detector = ColorSensor()
detector.mode = 'COL-COLOR'

ballfinder = Sensor(address='in2:i2c8', driver_name='ht-nxt-ir-seek-v2')
ballfinder.mode = 'AC'

ultrasonicSensor = UltrasonicSensor('in3')
ultrasonicSensor.mode = 'US-DIST-CM'

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
ballFound = False


def rotateLeft():
    leftMotor.run_to_rel_pos(position_sp=377, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=-377, speed_sp=200, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()


def rotateRight():
    leftMotor.run_to_rel_pos(position_sp=-377, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=377, speed_sp=200, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()

def turnLeft():
    leftMotor.run_to_rel_pos(position_sp=0, speed_sp=150, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=-760, speed_sp=150, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()

def turnRight():
    leftMotor.run_to_rel_pos(position_sp=-760, speed_sp=150, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=0, speed_sp=150, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()


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

    rightMotor.run_forever(speed_sp=-rightMotorVal)
    leftMotor.run_forever(speed_sp=-leftMotorVal)

# At the start of the house
while ultrasonicSensor.distance_centimeters > 3:
    print(ultrasonicSensor.distance_centimeters)
    rightMotor.run_forever(speed_sp=-200)
    leftMotor.run_forever(speed_sp=-200)

# Stop in front of the first wall
rightMotor.stop(stop_action='brake')
leftMotor.stop(stop_action='brake')

rotateRight()
print("first right")


# Get the right end of the wall
while ultrasonicSensor.distance_centimeters > 3:
    rightMotor.run_forever(speed_sp=-200)
    leftMotor.run_forever(speed_sp=-200)

print("got to right end of the wall")

rightMotor.stop(stop_action='brake')
leftMotor.stop(stop_action='brake')

rotateLeft()

# A ball exists in this hallway
if ballfinder.value() >= 3 and ballfinder.value() <= 6:
    leftMotor.run_to_rel_pos(position_sp=-360, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(
        position_sp=-360, speed_sp=200, stop_action='hold')
    Sound.beep()
# A ball doesn't exist in this hallway
else:
    rotateLeft()
    #rightMotor.run_to_rel_pos(position_sp=5, speed_sp=200, stop_action='hold')
    #leftMotor.run_to_rel_pos(position_sp=-5, speed_sp=200, stop_action='hold')
    #rightMotor.wait_until_not_moving()
    #leftMotor.wait_until_not_moving()
    
    print("going to left end")
    # Go to left end of the track
    while ultrasonicSensor.distance_centimeters > 3:
        rightMotor.run_forever(speed_sp=-200)
        leftMotor.run_forever(speed_sp=-200)
    # Stop in front of the left wall
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')

    rotateRight()

    # A ball exists in this hallway
    if ballfinder.value() >= 3 and ballfinder.value() <= 6:
        leftMotor.run_to_rel_pos(position_sp=7, speed_sp=200, stop_action='hold')
        rightMotor.run_to_rel_pos(position_sp=-7, speed_sp=200, stop_action='hold')
        leftMotor.wait_until_not_moving()
        rightMotor.wait_until_not_moving()
        leftMotor.run_to_rel_pos(
            position_sp=-1400, speed_sp=200, stop_action='hold')
        rightMotor.run_to_rel_pos(
            position_sp=-1400, speed_sp=200, stop_action='hold')
        Sound.beep()
    else:
        rotateRight()
        print("at the annoying turn")
        leftMotor.run_to_rel_pos(
            position_sp=-540, speed_sp=200, stop_action='hold')
        rightMotor.run_to_rel_pos(
            position_sp=-540, speed_sp=200, stop_action='hold')
        
        rightMotor.wait_until_not_moving()
        leftMotor.wait_until_not_moving()
       
        rotateLeft()

        # Go to end of the inside box
        while ultrasonicSensor.distance_centimeters > 3:
            rightMotor.run_forever(speed_sp=-200)
            leftMotor.run_forever(speed_sp=-200)

        rotateRight()
        if ballfinder.value() != 0:
            Sound.beep()