#! /usr/bin/env python
import RPi.GPIO as GPIO

import time

print("Lancement tutoriel")
LED = 17
FRESH = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
    while True:
        print()
        print("Entrée")
        print("Allumée")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(FRESH)
        print("Eteinte")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(FRESH)
        print("Sortie")
        print()

except KeyboardInterrupt:
    GPIO.cleanup()