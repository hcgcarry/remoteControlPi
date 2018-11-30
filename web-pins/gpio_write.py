import sys
import pigpio
import time
help = sys.argv

pin = int(help[2])
mode = int(help[1])
pi=pigpio.pi()
if int(mode) == 1:
	pi.set_mode(pin,pigpio.OUTPUT)
	pi.write(pin,1)
	print(1)

if int(mode) == 0:
	pi.set_mode(pin,pigpio.OUTPUT)
	pi.write(pin,0)
	print(0)

pi.stop()

