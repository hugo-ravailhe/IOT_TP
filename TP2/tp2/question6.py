### Question 6 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT
from datetime import datetime

print("Question 6 Launch")

SENSOR = 22
PIN = 5

try:
    # Open the file in append mode
    file = open("data.txt", "a")

    while True:
        # read temperature
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        # get the time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if humidity is not None and temperature is not None:
            # format the temperature and humidity
            output = 'Temp={0:0.1f}°  Humidity={1:0.1f}%\n'.format(
                temperature, humidity)
            # add all the information on the output
            output = f"Current Time: {current_time} - {output}"
            print(output)
            # put the output into the file
            file.write(output)
            time.sleep(3)

        else:
            print('Failed to get reading. Exit')
            break

except KeyboardInterrupt:
    print('Exit')
    file.close()
    sys.exit(0)
