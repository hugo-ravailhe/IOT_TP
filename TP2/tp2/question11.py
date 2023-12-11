### Question 11 - Senhua Liu & Hugo Ravailhe ###
#! /usr/bin/env python
import RPi.GPIO as GPIO
import time, sys, threading
import Adafruit_DHT

print("Question 11 Launch")

PIR_MOTION  = 4
BUZZER      = 12
LED_GREEN   = 6
LED_RED     = 5
LED_YELLOW  = 13
SENSOR      = 22
PIN         = 25

GPIO.setmode(GPIO.BCM)

# Buzzer
GPIO.setup(BUZZER, GPIO.OUT)

# Pir Motion
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Led
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
# Led
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_YELLOW, GPIO.LOW)


# Initialize variables for the smart home system
alarm_enabled = False
# lights_status = {'Living Room': False, 'Bedroom': False, 'Kitchen': False}
temperature_trigger = None
temperature_value = 0.0

# Functions for services
def enable_alarm():
    global alarm_enabled
    alarm_enabled = True
    print("Alarm system enabled.")

def disable_alarm():
    global alarm_enabled
    alarm_enabled = False
    print("Alarm system disabled.")

def enable_lights(room):
    if room == '1':
        GPIO.output(LED_RED, GPIO.HIGH)
        print(f"Lights in Living Room enabled.")
    elif room == '2':
        GPIO.output(LED_GREEN, GPIO.HIGH)
        print(f"Lights in 'Bedroom enabled.")
    else:
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        print(f"Lights in Kitchen enabled.")

def disable_lights(room):
    if room == '1':
        GPIO.output(LED_RED, GPIO.LOW)
        print(f"Lights in Living Room disabled.")
    elif room == '2':
        GPIO.output(LED_GREEN, GPIO.LOW)
        print(f"Lights in 'Bedroom disabled.")
    else:
        GPIO.output(LED_YELLOW, GPIO.LOW)
        print(f"Lights in Kitchen disabled.")

def turn_on_all_lights():
    GPIO.output(LED_GREEN, GPIO.HIGH)
    GPIO.output(LED_RED, GPIO.HIGH)
    GPIO.output(LED_YELLOW, GPIO.HIGH)
    print("All lights turned on.")

def turn_off_all_lights():
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_YELLOW, GPIO.LOW)
    print("All lights turned off.")

def set_temperature_trigger(value):
    global temperature_trigger
    temperature_trigger = value
    print(f"Temperature trigger set to {value} degrees.")

def view_temperature():
    global temperature_value
    print('Temp={0:0.1f}°  '.format(temperature_value))

# Thread for simulating temperature changes
def temperature_simulation():
    print("Temperature simulation launched")
    global temperature_value
    while True:
        # Simulate temperature changes
        humidity, temperature_value = Adafruit_DHT.read_retry(SENSOR, PIN)
        # print('Temp={0:0.1f}°  '.format(temperature_value))
        if temperature_trigger is not None and temperature_value > temperature_trigger:
            GPIO.output(BUZZER, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(BUZZER, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(BUZZER, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(BUZZER, GPIO.LOW)
            time.sleep(1.4)
        else:
            time.sleep(2)

def alarm_system():
    print("Alarm System launched")
    while True:
        if GPIO.input(PIR_MOTION):
            if alarm_enabled:
                GPIO.output(BUZZER, GPIO.HIGH)
        else:
            GPIO.output(BUZZER, GPIO.LOW)
        
        time.sleep(0.2)

try:
    thread_temperature = threading.Thread(target=temperature_simulation)
    thread_temperature.start()
    thread_alarm = threading.Thread(target=alarm_system)
    thread_alarm.start()

    while True:
        print("\n===== Smart Home Menu =====")
        print("1. Alarm System")
        print("2. Lights")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            action = input("1. Enable Alarm\n2. Disable Alarm\nEnter action (1-2): ")
            if action == '1':
                enable_alarm()
            elif action == '2':
                disable_alarm()
        elif choice == '2':
            action = input("1. Enable Lights\n2. Disable Lights\n3. Turn On All Lights\n4. Turn Off All Lights\nEnter action (1-4): ")
            if action == '1':
                room = input("Enter room (1: Living Room/ 2: Bedroom/ 3: Kitchen): ")
                enable_lights(room)
            elif action == '2':
                room = input("Enter room (1: Living Room/ 2: Bedroom/ 3: Kitchen): ")
                disable_lights(room)
            elif action == '3':
                turn_on_all_lights()
            elif action == '4':
                turn_off_all_lights()
        elif choice == '3':
            action = input("1. Set Temperature Trigger\n2. View Temperature\nEnter action (1-2): ")
            if action == '1':
                value = float(input("Enter temperature trigger value: "))
                set_temperature_trigger(value)
            elif action == '2':
                view_temperature()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
finally:
    GPIO.cleanup()
    thread_temperature.join()  # Stop the temperature simulation thread
    thread_alarm.join()
    print("Program stopped")
