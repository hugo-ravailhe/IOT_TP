### Question 9 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time, sys

print("Question 9 Launch")

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
BUZZER = 12
LED_GREEN = 6
LED_RED  = 5

# Buzzer
GPIO.setup(BUZZER,GPIO.OUT)
# Led
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
# Sonar
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# Buzzer
GPIO.output(BUZZER, GPIO.LOW)
# Led
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_RED, GPIO.LOW)
# Sonar
GPIO.output(TRIG, False)

time.sleep(1)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def not_secure():
    print("Not secure")
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_RED, GPIO.HIGH)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(BUZZER, GPIO.LOW)

def is_secure():
    print("Is secure")
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.HIGH)

def check_security(distance, security_distance):
    if distance < security_distance:
        not_secure()
    else:
        is_secure()

try:
    choice = float(input("Choose a security distance in cm: ").lower())
    while True:
        distance = get_distance()
        check_security(distance, choice)

        distance_meters = distance
        print(f"Distance: {distance_meters:.2f} centimeters")
        time.sleep(0.2)

finally:
    GPIO.cleanup()