### Question 4 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO

print("Question 4 Launch")

LED_GREEN = 22
LED_YELLOW = 27
LED_RED = 17

BUTTON_GREEN = 24
BUTTON_YELLOW = 23
BUTTON_RED = 18

FRESH = 1

GPIO.setmode(GPIO.BCM)

# Set up the LED pins as output and initialize them to LOW (off)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.output(LED_YELLOW, GPIO.LOW)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

# Set up the button pins as input with pull-up resistors
GPIO.setup(BUTTON_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BUTTON_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BUTTON_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read and print the state of the buttons
        button_state_green = GPIO.input(BUTTON_GREEN)
        button_state_yellow = GPIO.input(BUTTON_YELLOW)
        button_state_red = GPIO.input(BUTTON_RED)
        print(f"Red: {button_state_green}")
        print(f"Yellow: {button_state_yellow}")
        print(f"Red: {button_state_red}")

        # set on or off the LEDs based on the button states
        if button_state_green == True:
            GPIO.output(LED_GREEN, GPIO.LOW)
        else:
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if button_state_yellow == True:
            GPIO.output(LED_YELLOW, GPIO.LOW)
        else:
            GPIO.output(LED_YELLOW, GPIO.HIGH)

        if button_state_red == True:
            GPIO.output(LED_RED, GPIO.LOW)
        else:
            GPIO.output(LED_RED, GPIO.HIGH)

        print()
except KeyboardInterrupt:
    GPIO.cleanup()
