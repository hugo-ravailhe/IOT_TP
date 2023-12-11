### Question 4 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

print("Question 5 Launch")

SENSOR = 22
PIN = 5
# We use RGB Led
LED_BLUE = 22
LED_RED = 17
LED_GREEN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)

GPIO.output(LED_RED, False)

try:
    # get the user input
    temperature_input = float(input("Enter the temperature : "))
    while True:
        # Read the temperature and humidity
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}°  Humidity={1:0.1f}%'.format(
                temperature, humidity))
            # compare the input temperature and the actual temperature
            if temperature_input < temperature:
                GPIO.output(LED_RED, True)
            else:
                GPIO.output(LED_RED, False)

            time.sleep(3)

        else:
            print('Failed to get reading. Exit')
            break

except KeyboardInterrupt:
    print('Exit')
    GPIO.cleanup()
    sys.exit(0)
