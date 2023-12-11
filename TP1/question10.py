### Question 10 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import random

print("Question 10 Launch")

LED_BLUE    = 22
LED_RED     = 17
LED_GREEN   = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

def input_one():
    GPIO.output(LED_RED, GPIO.HIGH)

def input_two():
    GPIO.output(LED_RED, GPIO.LOW)

def input_three():
    GPIO.output(LED_BLUE, GPIO.HIGH)

def input_four():
    GPIO.output(LED_BLUE, GPIO.LOW)

def input_five():
    GPIO.output(LED_GREEN, GPIO.HIGH)

def input_six():
    GPIO.output(LED_GREEN, GPIO.LOW)

def input_seven():
    GPIO.output(LED_GREEN, GPIO.HIGH)
    GPIO.output(LED_BLUE, GPIO.HIGH)
    GPIO.output(LED_RED, GPIO.HIGH)

def input_eight():
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)

def input_nine():
    input_eight()
    random_list = [LED_GREEN, LED_BLUE, LED_RED]
    choice = random.choice(random_list)
    GPIO.output(choice, GPIO.HIGH)

def print_menu():
    print()
    print("MENU")
    print("1. Red ON  2. Red OFF  3. Blue ON  4. Blue OFF")
    print("5. Green ON  6. Green OFF   7. Turn ON ALL  8. Turn OFF ALL")
    print("9. Random color  0. Exit")
    print()


try:
    while True:
        print_menu()
        user_choice = input("Make your choice: ")

        if user_choice == '1':
            input_one()
        elif user_choice == '2':
            input_two()
        elif user_choice == '3':
            input_three()
        elif user_choice == '4':
            input_four()
        elif user_choice == '5':
            input_five()
        elif user_choice == '6':
            input_six()
        elif user_choice == '7':
            input_seven()
        elif user_choice == '8':
            input_eight()
        elif user_choice == '9':
            input_nine()
        elif user_choice == '0':
            print("Exit")
            break
        else:
            print("Wrong input, try again")
            
except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()