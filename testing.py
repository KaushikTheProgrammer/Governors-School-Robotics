#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
import time

centerLight = LightSensor('in4')
#centerLight.mode = 'COL-REFLECT'

detector = ColorSensor()
detector.mode = 'RGB-RAW'

ballfinder = Sensor(address='in2:i2c8', driver_name='ht-nxt-ir-seek-v2')
ballfinder.mode = 'AC'

ultrasonicSensor = UltrasonicSensor('in3')
ultrasonicSensor.mode = 'US-DIST-CM'

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')

startButton = Button()

base_speed = 120
setpoint = 40

kP = 23

prevGreen = 120
prevRed = 160
numGreen = 0
numRed = 0
detectedTime = 0
threshold = 10

line = True

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


print('waiting for start')
while not startButton.any():
    continue

while line:
    lightOutput = centerLight.reflected_light_intensity
    redVal = detector.value(0)
    greenVal = detector.value(1)
    currentTime = time.time()

    error = lightOutput - setpoint
    rightMotorVal = base_speed + (error * kP)
    leftMotorVal = base_speed - (error * kP)

    # if (prevGreen == (greenVal + 1) or prevGreen == (greenVal - 1)) and (greenVal >= 17 and greenVal <= 19) and currentTime > detectedTime + threshold:
    #     numGreen += 1
    # else:
    #     numGreen = 0

    # if numGreen == 10:
    #     Sound.beep()
    #     detectedTime = currentTime

    if (prevRed <= redVal + 20 and prevRed >= redVal - 20) and (redVal >= 100 and redVal <= 140):
        numRed += 1
    else:
        numRed = 0

    if numRed == 15:
        line = False

    prevGreen = greenVal
    prevRed = redVal

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
    Sound.beep()
    while ultrasonicSensor.distance_centimeters > 3:
        rightMotor.run_forever(speed_sp=-200)
        leftMotor.run_forever(speed_sp=-200)
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')
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

    while not(ballfinder.value() >= 3 and ballfinder.value() <= 6):
        leftMotor.run_to_rel_pos(position_sp=-15, speed_sp=200, stop_action='hold')
        rightMotor.run_to_rel_pos(position_sp=0, speed_sp=200, stop_action='hold')
        # rightMotor.wait_until_not_moving()
        # leftMotor.wait_until_not_moving()

    # A ball exists in this hallway
    if ballfinder.value() >= 3 and ballfinder.value() <= 6:
        Sound.beep()
        while ultrasonicSensor.distance_centimeters > 3:
            rightMotor.run_forever(speed_sp=-200)
            leftMotor.run_forever(speed_sp=-200)
        rightMotor.stop(stop_action='brake')
        leftMotor.stop(stop_action='brake')
    # else:
    #     rotateRight()
    #     leftMotor.run_to_rel_pos(
    #         position_sp=-540, speed_sp=200, stop_action='hold')
    #     rightMotor.run_to_rel_pos(
    #         position_sp=-540, speed_sp=200, stop_action='hold')
        
    #     rightMotor.wait_until_not_moving()
    #     leftMotor.wait_until_not_moving()
       
    #     rotateLeft()

    #     # Go to end of the inside box
    #     while ultrasonicSensor.distance_centimeters > 3:
    #         rightMotor.run_forever(speed_sp=-200)
    #         leftMotor.run_forever(speed_sp=-200)

    #     rotateRight()
    #     if ballfinder.value() != 0:
    #         Sound.beep()
