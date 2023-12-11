### Question 2 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 2 Launch")

LED1 = 17
LED2 = 10
FRESH = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.output(LED1, GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED2, GPIO.LOW)
# set all LED off

try:
    while True:

        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        # set the Red LED on and green LED off
        time.sleep(FRESH)

        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        # set the Red LED off and green LED on
        time.sleep(FRESH)

except KeyboardInterrupt:
    GPIO.cleanup()
