### Question 1 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 1 Launch")
LED = 17
FRESH = int(input("Enter a interval value:\n"))
# Enter a interval value
GPIO.setmode(GPIO.BCM)
GPIO.output(LED, GPIO.LOW)  # set the LED off

try:
    while True:

        GPIO.output(LED, GPIO.HIGH)  # set the LED on
        time.sleep(FRESH)

        GPIO.output(LED, GPIO.LOW)  # set the LED off
        time.sleep(FRESH)

except KeyboardInterrupt:
    GPIO.cleanup()
