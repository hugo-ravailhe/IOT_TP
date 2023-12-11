### Question 10 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

print("Question 10 Launch")

# Computes duty cycle with giving angle and does the servo rotation


def set_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    print(f"Duty cycle: {duty_cycle}")
    print()

    p.ChangeDutyCycle(duty_cycle)
    time.sleep(1)


PIR_MOTION = 4
MOTOR = 26
LED_GREEN = 6
LED_RED = 5

current_position = 0

GPIO.setmode(GPIO.BCM)

# Motor
GPIO.setup(MOTOR, GPIO.OUT)
p = GPIO.PWM(MOTOR, 50)
p.start(2.5)

# Pir Motion
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Led
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
# Led
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_RED, GPIO.LOW)

# function for movement detected


def movement_detected():
    set_angle(90)

# function for no movement detected


def movement_not_detected():
    set_angle(0)

# Computes duty cycle with giving angle and does the servo rotation


def set_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    print(f"Duty cycle: {duty_cycle}")
    print()

    p.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)


try:
    choice = input("Choose 'enabled' or 'disabled' door's mode: ").lower()
    if choice not in ['enabled', 'disabled']:
        print("Invalid choice. Please enter 'enabled' or 'disabled'.")
    else:
        if choice == 'enabled':
            # green led on : door is can be open
            GPIO.output(LED_GREEN, GPIO.HIGH)
        else:
            # door cannot be open
            GPIO.output(LED_RED, GPIO.HIGH)

        while True:
            if GPIO.input(PIR_MOTION):
                print("Motion Detected")
                if choice == 'enabled':
                    # door open at 90°
                    movement_detected()
            else:
                print("No Motion Detected")
                if choice == 'enabled':
                    # close the door (at 0°)
                    movement_not_detected()

            time.sleep(0.1)

finally:
    p.stop()
    GPIO.cleanup()
    print("Program stopped")
