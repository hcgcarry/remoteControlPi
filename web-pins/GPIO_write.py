import sys
import RPi.GPIO as GPIO

help = sys.argv


pinIn = help[2]
mode = help[1]

if int(mode) == 1:
	GPIO.setup(pinIn , GPIO.OUT)
	GPIO.output(pinIn , True)
	
if int(mode) == 0:
	GPIO.setup(pinIn , GPIO.OUT)
	GPIO.output(pinIn , False)
	