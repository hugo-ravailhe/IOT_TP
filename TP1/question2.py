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

try:
    while True:

        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(FRESH)

        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(FRESH)

except KeyboardInterrupt:
    GPIO.cleanup()