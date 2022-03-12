#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 3/5/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Tests the functionality of Hall effect motor encoder"""
# ---------------------------------------------------------------------------

from PCA9685 import PCA9685
import RPi.GPIO as GPIO

import Motor_Driver

GPIO.setmode(GPIO.BOARD)

# Board pins used as inputs to go up and down.
CHAN_A = 11
CHAN_B = 13

GPIO.setup([CHAN_A, CHAN_B], GPIO.IN)

# encoder_states[A][B] should go from 1 -> 2 -> 3 -> 4 -> 1 as motor goes forward with the states of channels A and B defined to A and B respectively
encoder_states = [[1,2],[4,3]]

Motor = Motor_Driver.MotorDriver()
Motor.MotorRun(0, 'forward', 100)
starting_pos= encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
per_count = 0
pos = 0
# for i in range(10000):
#     print(encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)])

while per_count < 200:
    if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
        per_count+= 1
    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    print(pos, per_count)


Motor.MotorStop(0)

motor_moving = True
repeat_pos = 0
while motor_moving:
    if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
        per_count+= 1

    if pos == encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]:
        repeat_pos += 1
        if repeat_pos > 300:
            motor_moving = False
    else:
        repeat_pos = 0

    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    print(pos, per_count)
Motor.MotorStop(1)
print('counted periods:', per_count)
# 120 periods corresponds to approximately 1 revolution of the motor
# upon retesting, 190 periods now seem to equal 1 rev.
