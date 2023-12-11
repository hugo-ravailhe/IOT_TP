### Question 8 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

print("Question 8 Launch")

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
LED = 17

print("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, False)
GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)


def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# function to make the red LED blink with a period


def blink_led(period):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(period - 0.05)

# function to control the LED blinking based on the distance


def led_blinking(distance):
    if distance < 5:
        blink_led(0.05)
    elif 5 <= distance <= 100:
        period = 0.05 + 0.95 * ((distance - 5) / 95)
        blink_led(period)
    else:
        GPIO.output(LED, GPIO.LOW)


try:
    while True:
        distance = get_distance()
        led_blinking(distance)

        distance_meters = distance / 100
        print(f"Distance: {distance_meters:.2f} meters")

except KeyboardInterrupt:
    GPIO.cleanup()
