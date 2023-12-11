### Question 3 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

print("Question 3 Launch")

SENSOR = 22
PIN = 5

try:
    while True:
        # Read the temperature and humidity from the DHT sensor
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if humidity is not None and temperature is not None:  # if success
            print(
                'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Exit')
            sys.exit(1)
        time.sleep(3)  # Wait 3 seconds before read again
except KeyboardInterrupt:
    print('Exit')
    sys.exit(0)
