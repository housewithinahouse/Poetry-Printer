#!/usr/bin/env python
     
import os
from time import sleep
     
import RPi.GPIO as GPIO
     
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

os.system('sudo chown pi:pi /dev/usb/lp0')
     
while True:
        if (GPIO.input(23) == False):
		os.system('sh /home/pi/Desktop/PocketPoems/startup');
		sleep(1);
	if (GPIO.input(24) == False):
                os.system('sh /home/pi/Desktop/PocketPoems/startup-patron_poems');
                sleep(1);