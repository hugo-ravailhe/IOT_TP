### Question 3a - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO

print("Question 3a Launch")

LED = 17
BUTTON = 27
FRESH = 1

GPIO.setmode(GPIO.BCM)
# # GPIO 17 - LED
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
# GPIO 27 - Button
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(BUTTON)
        print(button_state)
        if button_state == True:
            GPIO.output(LED, GPIO.LOW)
            print("Button not pressed")
        else:
            GPIO.output(LED, GPIO.HIGH)
            print("Button pressed")

except KeyboardInterrupt:
    GPIO.cleanup()