#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 2/24/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Prints the state of pins 16 and 18 on a Raspberry pi as code is ran. """
# ---------------------------------------------------------------------------
import RPi.GPIO as GPIO

debug = True

GPIO.setmode(GPIO.BOARD)

# Board pins used as inputs to go up and down.
PIN_UP = 16
PIN_DOWN = 18

GPIO.setup([PIN_UP, PIN_DOWN], GPIO.IN)
if(debug):
    print('up pin state:', GPIO.input(PIN_UP))
    print('down pin state:', GPIO.input(PIN_DOWN))
