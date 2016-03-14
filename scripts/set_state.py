#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

# Init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Get input
pin = int(sys.argv[1])
desiredState = sys.argv[2]

# Set pin mode
GPIO.setup(pin, GPIO.OUT)

# Main
if desiredState == "false":
    GPIO.output(pin, GPIO.HIGH)
    print ("Device is now off.")
else:
    GPIO.output(pin, GPIO.LOW)
    print ("Device is now on.")
