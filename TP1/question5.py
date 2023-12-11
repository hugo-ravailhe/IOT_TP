### Question 5 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 5 Launch")

LED_GREEN = 22
LED_YELLOW = 27
LED_RED = 17

FRESH = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.output(LED_YELLOW, GPIO.LOW)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.HIGH)

try:
    while True:
       
       GPIO.output(LED_RED, GPIO.LOW)
       GPIO.output(LED_GREEN, GPIO.HIGH)
       print("Green")
       time.sleep(5)
       GPIO.output(LED_GREEN, GPIO.LOW)
       GPIO.output(LED_YELLOW, GPIO.HIGH)
       print("Yellow")
       time.sleep(2)
       GPIO.output(LED_YELLOW, GPIO.LOW)
       GPIO.output(LED_RED, GPIO.HIGH)
       print("Red")
       time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()