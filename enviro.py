#!/usr/bin/env python3

from envirophat import light, motion, weather, leds
import csv
import time

timestamp = int(time.time())
filename = "g2x-submarine-{}.csv".format(timestamp)

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow([
        "r", "g", "b",
        "x", "y", "z", "heading",
        "celsius", "hPa"
    ])

    # NOTE: the device needs to be face up and pointing north before this
    # reading is taken
    # north = motion.heading

    leds.on()

    while True:
        r, g, b = light.rgb()
        x, y, z = motion.accelerometer()
        # heading = (motion.heading() - north) % 360
        temp_in_celsius = weather.temperature()
        pressure_in_hpa = weather.pressure(unit='hPa')

        writer.writerow([
            r, g, b,
            x, y, z, # heading,
            temp_in_celsius, pressure_in_hpa
        ])

        time.sleep(1)
