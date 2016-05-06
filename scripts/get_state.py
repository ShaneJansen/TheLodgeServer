#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import json

CONST_DATA = [
    {
        'pin': 4,
        'name': 'Shane\'s  Lamp',
        'type': 'switch'
    },
    {
        'pin': 17,
        'name': 'Shane\'s  Monitor',
        'type': 'switch'
    },
    {
        'pin': 2,
        'name': 'Ceiling Fan',
        'type': 'switch'
    },
    {
        'pin': 3,
        'name': 'Air Conditioner',
        'type': 'switch'
    },
    {
        'pin': 20,
        'name': 'Refrigerator',
        'type': 'switch'
    },
    {
        'pin': 21,
        'name': 'Alarm',
        'type': 'switch'
    }
]

# Functions
def gpioToBool(output):
    if output == 1: return False
    return True

# Init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pins mode
for i in CONST_DATA:
    GPIO.setup(i['pin'], GPIO.OUT)

# Main
for i in CONST_DATA:
    i['isOn'] = gpioToBool(GPIO.input(i['pin']))
print (json.dumps(CONST_DATA))
