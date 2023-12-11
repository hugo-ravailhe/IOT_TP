### Question 6 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time, sys
import Adafruit_DHT
from datetime import datetime

print("Question 6 Launch")

SENSOR  = 22
PIN     = 5

try:
    file = open("data.txt", "a")

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if humidity is not None and temperature is not None:
            output = 'Temp={0:0.1f}°  Humidity={1:0.1f}%\n'.format(temperature, humidity)
            output = f"Current Time: {current_time} - {output}"
            print(output)
            file.write(output)
            time.sleep(3)

        else:
            print('Failed to get reading. Exit')
            break

except KeyboardInterrupt:
    print('Exit')
    file.close()
    sys.exit(0)