#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 3/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Operates an automated blinds operator by fetching weather data every hour and setting the position
according to weather. Also allows for manual inputs with buttons wired to Raspberry Pi to move blinds
up and down as needed.
"""
# ---------------------------------------------------------------------------
import time
import urllib.request
import json
import sched
import math
import tracemalloc
import psutil

import RPi.GPIO as GPIO

import Motor_Driver


GPIO.setmode(GPIO.BOARD)

debug = False

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
motor_moving = False
Motor = Motor_Driver.MotorDriver()

previous_weather = {}
weather_change_detected = False



def continue_reading_encoder():
    repeat_pos = 0
    global motor_pos
    global motor_moving
    pos = 0
    if debug:
        print('entering c_r_e loop')
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
    if debug:
        print('cre loop exitted')

def motor_forward(channel):
    global motor_moving 
    motor_moving = True
    Motor.MotorRun(0, 'forward', 100)
    global motor_pos
    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    if debug:
        print('entering forward loop')
    while True:
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
            motor_pos += 1
        pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
        if GPIO.input(PIN_UP) == GPIO.LOW:
            Motor.MotorStop(0)
            continue_reading_encoder()
            print(motor_pos)
            break
    if debug:
        print('forward loop exitted')

def motor_backward(channel):
    global motor_moving 
    motor_moving = True
    Motor.MotorRun(0, 'backward', 100)
    global motor_pos
    pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
    if debug:
        print('entering backwards loop')
    while True:
        if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 4 and pos == 1):
            motor_pos -= 1
        pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
        if GPIO.input(PIN_DOWN) == GPIO.LOW:
            Motor.MotorStop(0)
            continue_reading_encoder()
            print(motor_pos)
            break
    if debug:
        print('exitting backwrds loop')

def fetch_weather():
    weather_api_format = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

    #coordiates for Seattle Area
    lat = '47.6062'
    lon = '-122.3321'

    #unique api key for openweathermap.org
    API_key = '831c3248984f934c37d5377f495f30c1'

    formatted_url = weather_api_format.format(lat = lat, lon = lon, API_key = API_key)

    with urllib.request.urlopen(formatted_url) as response:
        weather_data = json.loads(response.read().decode('utf-8'))
    
    daytime = False
    if (time.time() > weather_data['sys']['sunrise'] and time.time() < weather_data['sys']['sunset']):
        daytime = True
    
    weather_data['Daytime'] = daytime

    return weather_data

def weather_to_position(weather_data):
    try:
        daytime = False
        if (time.time() > weather_data['sys']['sunrise'] and time.time() < weather_data['sys']['sunset']):
            daytime = True
        
        main_weather = weather_data['weather'][0]['main']
        if main_weather == 'Clear' and daytime:
            return 1000
        elif main_weather == 'Snow':
            return 1000
        else:
            return 0
    except:
        print('weather data not recognized')

def move_to_position(position):
    global motor_pos
    global motor_moving
    if debug:
        print('entering mtp loop')
    if not motor_moving:
        if motor_pos < position:
            Motor.MotorRun(0, 'forward', 100)
            pos= encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
            while motor_pos < position:
                if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 1 and pos == 4):
                    motor_pos += 1
                pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
            Motor.MotorStop(0)
            continue_reading_encoder()
        
        elif motor_pos > position:
            Motor.MotorRun(0, 'backward', 100)
            pos= encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
            while motor_pos > position:
                if (encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)] == 4 and pos == 1):
                    motor_pos -= 1
                pos = encoder_states[GPIO.input(CHAN_A)][GPIO.input(CHAN_B)]
            Motor.MotorStop(0)
            continue_reading_encoder()
    
    if debug:
        print('exitting mtp loop')
    
def calc_next_time(time_interval):
    current_time = time.time()
    next_interval_start = math.ceil(current_time/time_interval) * time_interval
    print('next sched time:', next_interval_start)
    return next_interval_start

def detect_weather_change(cur_weather, prev_weather):
    if cur_weather['weather'][0]['main'] != prev_weather['weather'][0]['main']:
        return True
    elif cur_weather['Daytime'] != prev_weather['Daytime']:
        return True
    else:
        False

def routine_action():
    global weather_data, previous_weather
    weather_data = fetch_weather()
    if detect_weather_change(weather_data, previous_weather):
        pos = weather_to_position(weather_data)
        move_to_position(pos)
        previous_weather = weather_data.copy()
    else:
        pass

def alter_weather_data(weather_cond, daytime):
    global weather_data, previous_weather
    weather_data['weather'][0]['main'] = weather_cond
    weather_data['Daytime'] = daytime
    previous_weather = weather_data.copy()

tracemalloc.start()

GPIO.add_event_detect(PIN_UP, GPIO.RISING, callback=motor_forward)
GPIO.add_event_detect(PIN_DOWN, GPIO.RISING, callback=motor_backward)

weather_data = fetch_weather()
previous_weather = weather_data.copy()
target_pos = weather_to_position(weather_data)
move_to_position(target_pos)

s = sched.scheduler(time.time, time.sleep)

while True:
    s.enterabs(calc_next_time(10), 0, routine_action)
    s.enterabs(calc_next_time(5), 1, alter_weather_data, ("Force Change", True))
    s.run()
    print(tracemalloc.get_traced_memory())
    print('The CPU usage is: ', psutil.cpu_percent(10))
