### Question 2 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 2 Launch")

PIR_MOTION  = 25
# We use RGB Led
LED_BLUE    = 22
LED_RED     = 17
LED_GREEN   = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

# Turn on the red LED and turn off the green LED initially
GPIO.output(LED_RED, True)
GPIO.output(LED_GREEN, False)

try:
    while True:
         # Check if motion is detected by the PIR sensor
        if GPIO.input(PIR_MOTION):
            print("Motion Detected")
            GPIO.output(LED_RED, False)
            GPIO.output(LED_GREEN, True)
            print()
        else:
            GPIO.output(LED_GREEN, False)
            GPIO.output(LED_RED, True)

except KeyboardInterrupt:
    GPIO.cleanup()