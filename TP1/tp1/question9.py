### Question 9 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

print("Question 9 Launch")

GPIO.setmode(GPIO.BCM)
turn_off_GPIO_time = 0.1
value = 0

LED = 17
BUZZER = 18
LDR = 4

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

# We add this variable to know the previous state of the button
previous_button_state = True

def rc_time(pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

try:
    while True:
        value = rc_time(LDR)
        if ( value <= 100000 ): 
            print("Lights are ON")
            GPIO.output(LED, GPIO.LOW)
            previous_button_state = True
        else:
            print("Lights are OFF")
            if previous_button_state == True:
                GPIO.output(LED, GPIO.HIGH)
                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(BUZZER, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(BUZZER, GPIO.LOW)
            previous_button_state = False

except KeyboardInterrupt: 
    GPIO.cleanup()