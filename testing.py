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
    leftMotor.run_to_rel_pos(position_sp=0, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=-754, speed_sp=200, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()

def turnRight():
    leftMotor.run_to_rel_pos(position_sp=-754, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=0, speed_sp=200, stop_action='hold')
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

turnLeft()

# # At the start of the house
# while ultrasonicSensor.distance_centimeters > 3.5:
#     print(ultrasonicSensor.distance_centimeters)
#     rightMotor.run_forever(speed_sp=-200)
#     leftMotor.run_forever(speed_sp=-200)

# # Stop in front of the first wall
# rightMotor.stop(stop_action='brake')
# leftMotor.stop(stop_action='brake')

# turnRight()
# print("first right")


# # Get the left end of the wall
# while ultrasonicSensor.distance_centimeters > 3.5:
#     rightMotor.run_forever(speed_sp=-200)
#     leftMotor.run_forever(speed_sp=-200)

# print("got to left end of the wall")

# # Stop in front of the first wall
# rightMotor.stop(stop_action='brake')
# leftMotor.stop(stop_action='brake')
# print("stop in front of the first wall")

# turnLeft()

# # A ball exists in this hallway
# if ballfinder.value() != 0:
#     leftMotor.run_to_rel_pos(position_sp=360, speed_sp=200, stop_action='hold')
#     rightMotor.run_to_rel_pos(
#         position_sp=360, speed_sp=200, stop_action='hold')
#     Sound.beep()
# # A ball doesn't exist in this hallway
# else:
#     turnLeft()
#     # Go to left end of the track
#     while ultrasonicSensor.distance_centimeters > 3.5:
#         rightMotor.run_forever(speed_sp=-200)
#         leftMotor.run_forever(speed_sp=-200)
#     # Stop in front of the left wall
#     rightMotor.stop(stop_action='brake')
#     leftMotor.stop(stop_action='brake')

#     turnRight()

#     # A ball exists in this hallway
#     if ballfinder.value() != 0:
#         leftMotor.run_to_rel_pos(
#             position_sp=360, speed_sp=200, stop_action='hold')
#         rightMotor.run_to_rel_pos(
#             position_sp=360, speed_sp=200, stop_action='hold')
#         Sound.beep()
#     else:
#         turnRight()
#         leftMotor.run_to_rel_pos(
#             position_sp=360, speed_sp=200, stop_action='hold')
#         rightMotor.run_to_rel_pos(
#             position_sp=360, speed_sp=200, stop_action='hold')
#         turnLeft()

#         # Go to end of the inside box
#         while ultrasonicSensor.distance_centimeters > 3.5:
#             rightMotor.run_forever(speed_sp=-200)
#             leftMotor.run_forever(speed_sp=-200)

#         turnRight()
#         if ballfinder.value() != 0:
#             Sound.beep()
