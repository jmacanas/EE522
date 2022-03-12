#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 2/24/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" test the accuracy of time.sleep() method. Code blocks need to be un-commented to run test code."""
# ---------------------------------------------------------------------------
import time

# ---------------------------------------------------------------------------
time_intervals = [1, 5, 10, 30]

for sleep_time in time_intervals:
    sleep_start = time.time()
    time.sleep(sleep_time)
    sleep_end = time.time()

    real_sleep_time = sleep_end - sleep_start
    error = real_sleep_time - sleep_time
    percent_error = error/sleep_time * 100.0
    print('target sleep time:', sleep_time,'\nreal sleep time:', real_sleep_time,'\nerror:', error, 'percent error:', percent_error)

# --------------------------------------------------------------------------
one_second_results = []

for i in range(100):
    sleep_start = time.time()
    time.sleep(1)
    sleep_end = time.time()
    one_second_results.append(sleep_end - sleep_start)

print(one_second_results)

five_second_results = []

for i in range(100):
    sleep_start = time.time()
    time.sleep(5)
    sleep_end = time.time()
    five_second_results.append(sleep_end - sleep_start)

print(five_second_results)
