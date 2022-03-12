#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Jared Macanas
# Created Date: 2/24/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Used to test urllib capabilities by retrieving weather data for Seattle area"""
# ---------------------------------------------------------------------------

import urllib.request
import json


weather_api_format = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'


#coordiates for Seattle Area
lat = '47.6062'
lon = '-122.3321'

#unique api key for openweathermap.org
API_key = '831c3248984f934c37d5377f495f30c1'

formatted_url = weather_api_format.format(lat = lat, lon = lon, API_key = API_key)

with urllib.request.urlopen(formatted_url) as response:
   weather_data = json.loads(response.read().decode('utf-8'))

print(type(weather_data), weather_data)
