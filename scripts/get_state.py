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
        'name': 'Shane\'s  Monitor',
        'type': 'switch'
    },
    {
        'pin': 3,
        'name': 'Shane\'s  Monitor',
        'type': 'switch'
    },
    {
        'pin': 20,
        'name': 'Shane\'s  Monitor',
        'type': 'switch'
    },
    {
        'pin': 21,
        'name': 'Shane\'s  Monitor',
        'type': 'switch'
    }
]

# Functions
def gpioToString(output):
    if output == 1: return 'off'
    return 'on'

# Init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pins mode
for i in CONST_DATA:
    GPIO.setup(i['pin'], GPIO.OUT)

# Main
for i in CONST_DATA:
    i['state'] = gpioToString(GPIO.input(i['pin']))
print (json.dumps(CONST_DATA))
