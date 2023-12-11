### Question 1 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 1 Launch")
LED = 17
FRESH = int(input("Enter a interval value:\n"))
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
    while True:

        GPIO.output(LED, GPIO.HIGH)
        time.sleep(FRESH)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(FRESH)

except KeyboardInterrupt:
    GPIO.cleanup()