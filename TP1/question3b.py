### Question 3b - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 3b Launch")

LED = 17
LED_STATE = GPIO.LOW
BUTTON = 27
FRESH = 0.1

# We add this variable to know the previous state of the button
previous_button_state = True

GPIO.setmode(GPIO.BCM)
# GPIO 17 - LED
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, LED_STATE)
# GPIO 27 - Button
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(BUTTON)
        print(button_state)
        if button_state == True:
            previous_button_state = button_state
            print("Button not pressed")
        else:
            print("Button pressed")
            # This If statement use to verify that the previous state of the button is "not pressed",
            # so in the case we keep pushing the button, we didn't execute the code more than once
            if previous_button_state != button_state:
                if LED_STATE == GPIO.LOW:
                    LED_STATE = GPIO.HIGH
                    GPIO.output(LED, LED_STATE)
                else:
                    LED_STATE = GPIO.LOW
                    GPIO.output(LED, LED_STATE)
            # we set the "previous_button_state" to high
            previous_button_state = button_state

except KeyboardInterrupt:
    GPIO.cleanup()