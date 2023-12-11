### Question 1 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 1 Launch")

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(2.5)

# Computes duty cycle with giving angle and does the servo rotation
def set_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    print(f"Duty cycle: {duty_cycle}")
    print()

    p.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    

try:
    while True:
        # Get user input for the angle
        angle = float(input("Enter the angle (0 to 180 degrees): "))
        
        # Check if the angle is within the valid range
        if 0 <= angle <= 180:
            set_angle(angle)
            print(f"Servo rotated to {angle} degrees.")
        else:
            print("Invalid angle. Please enter an angle between 0 and 180 degrees.")


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()