### Question 7 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import random
import time

print("Question 7 Launch")

LED_GREEN = 22
LED_BLUE = 27
LED_RED = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

def blink_red():
    for _ in range(5):
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_RED, GPIO.LOW)
        time.sleep(0.2)

def blink_blue():
    for _ in range(5):
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_BLUE, GPIO.LOW)
        time.sleep(0.2)

secret_number = int(random.random() * 20) + 1

attempts = 4

try:
    for _ in range(attempts):
        user_guess = int(input("Guess the secret number (between 1 and 20): "))

        if user_guess == secret_number:
            GPIO.output(LED_GREEN, GPIO.HIGH)
            print("Congratulation")
            time.sleep(3)
            break

        elif user_guess < secret_number:
            blink_red()
            print("Try a higher number.")

        else:
            blink_blue()
            print("Try a lower number.")
    # If the loop completes without a break, user ran out of attempts
    else:
        print(f"LOOOOOOOOOSER, you ran out of attempts. The secret number was {secret_number}.")

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()