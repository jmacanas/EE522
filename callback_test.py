#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 3/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Tests threading of callbacks available in the RPi.GPIO library"""
# ---------------------------------------------------------------------------
import time

import RPi.GPIO as GPIO

import Motor_Driver


GPIO.setmode(GPIO.BOARD)

# Board pins used as inputs to read encoder.
CHAN_A = 11
CHAN_B = 13

# Board pins used as inputs to go up and down.
PIN_UP = 16
PIN_DOWN = 18

GPIO.setup([CHAN_A, CHAN_B, PIN_UP, PIN_DOWN], GPIO.IN)

# encoder_states[A][B] should go from 1 -> 2 -> 3 -> 4 -> 1 as motor goes forward with the states of channels A and B defined to A and B respectively
encoder_states = [[1,2],[4,3]]

motor_pos = 0
Motor = Motor_Driver.MotorDriver()

def continue_reading_encoder():
    motor_moving = True
    repeat_pos = 0
    global motor_pos
    pos = 0
    while motor_moving:
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
            motor_pos+= 1
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 4 and pos == 1):
            motor_pos-= 1
        if pos == encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]:
            repeat_pos += 1
            if repeat_pos > 300:
                motor_moving = False
        else:
            repeat_pos = 0

        pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]

def motor_forward(channel):
    Motor.MotorRun(0, 'forward', 100)
    starting_pos= encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    global motor_pos
    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    while True:
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
            motor_pos += 1
        pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
        if GPIO.input(PIN_UP) == GPIO.LOW:
            Motor.MotorStop(0)
            continue_reading_encoder()
            print(motor_pos)
            break

def motor_backward(channel):
    Motor.MotorRun(0, 'backward', 100)
    starting_pos= encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    global motor_pos
    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    while True:
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 4 and pos == 1):
            motor_pos -= 1
        pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
        if GPIO.input(PIN_DOWN) == GPIO.LOW:
            Motor.MotorStop(0)
            continue_reading_encoder()
            print(motor_pos)
            break

GPIO.add_event_detect(PIN_UP, GPIO.RISING, callback=motor_forward)
GPIO.add_event_detect(PIN_DOWN, GPIO.RISING, callback=motor_backward)

print('waiting for input...')
time.sleep(10)
print('closing program...')
Motor.MotorStop(0)
