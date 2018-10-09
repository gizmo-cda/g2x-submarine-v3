#!/usr/bin/env python3

import os
import time
import atexit
import signal
import RPi.GPIO as GPIO

SECOND = 1
MINUTE = 60 * SECOND

LIGHT_PIN = 11


def light_on():
    GPIO.output(LIGHT_PIN, GPIO.HIGH)


def light_off():
    GPIO.output(LIGHT_PIN, GPIO.LOW)


def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_PIN, GPIO.OUT);


def shutdown(signum=0, frame=None):
    light_off()
    GPIO.cleanup([LIGHT_PIN])


if __name__ == "__main__":
    if os.geteuid() != 0:
        print("You must run this script with root privileges")
        exit(1)

    # cleanup on exit or sigterm
    atexit.register(shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # initialize GPIO
    init_gpio()

    # go through light cycle forever
    while True:
        light_on()
        time.sleep(45 * MINUTE)

        light_off()
        time.sleep(15 * MINUTE)
