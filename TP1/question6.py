### Question 6 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 6 Launch")

LED_GREEN = 22
LED_YELLOW = 27
LED_RED = 17

green_state = GPIO.LOW
yellow_state = GPIO.LOW
red_state = GPIO.HIGH

BUTTON = 24

FRESH = 1

# We add this variable to know the previous state of the button
previous_button_state = True

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, green_state)

GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.output(LED_YELLOW, yellow_state)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, red_state)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        

        button_state = GPIO.input(BUTTON)
        if button_state == True:
            previous_button_state = button_state
            print("Button not pressed")

        else:
            print("Button press")
            if previous_button_state != button_state:
                if green_state == GPIO.HIGH:
                    green_state = GPIO.LOW
                    yellow_state = GPIO.HIGH

                elif yellow_state == GPIO.HIGH:
                    yellow_state = GPIO.LOW
                    red_state = GPIO.HIGH

                elif red_state == GPIO.HIGH:
                    green_state = GPIO.HIGH
                    red_state = GPIO.LOW
                
                
                GPIO.output(LED_GREEN, green_state)
                GPIO.output(LED_YELLOW, yellow_state)
                GPIO.output(LED_RED, red_state)
            # we set the "previous_button_state" to high
            previous_button_state = button_state

except KeyboardInterrupt:
    GPIO.cleanup()