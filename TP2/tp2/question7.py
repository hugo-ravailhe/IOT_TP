### Question 7 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

print("Question 7 Launch")

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

print("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# set the TRIG pin to low initially
GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

# function to get the distance


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


try:
    while True:
        # the user choose the unit
        choice = input("Choose unit (meters/feet): ").lower()
        if choice not in ['meters', 'feet']:
            print("Invalid choice. Please enter 'meters' or 'feet'.")
            continue

        # get distance
        distance = get_distance()
        distance_meters = distance / 100

        # Convert the distance to the chosen unit of measurement and print the result
        if choice == 'meters':
            print(f"Distance: {distance_meters:.2f} meters")
        elif choice == 'feet':
            distance_feet = distance_meters * 3.281  # 1 meter = 3.281 feet
            print(f"Distance: {distance_feet:.2f} feet")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
