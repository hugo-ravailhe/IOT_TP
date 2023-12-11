### Question 8 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 8 Launch")

LED_GREEN = 22
LED_YELLOW = 27
LED_RED = 17
BUZZER = 18

FRESH = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.output(LED_YELLOW, GPIO.LOW)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.HIGH)

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

try:
    while True:
       GPIO.output(LED_RED, GPIO.LOW)
       GPIO.output(LED_GREEN, GPIO.HIGH)
       print("Green")
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(5)

       GPIO.output(LED_GREEN, GPIO.LOW)
       GPIO.output(LED_YELLOW, GPIO.HIGH)
       print("Yellow")
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(2)

       GPIO.output(LED_YELLOW, GPIO.LOW)
       GPIO.output(LED_RED, GPIO.HIGH)
       print("Red")
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.HIGH)
       time.sleep(0.5)
       GPIO.output(BUZZER, GPIO.LOW)
       time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()