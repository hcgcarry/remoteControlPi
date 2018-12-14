import time
import pigpio # abyz.co.uk/rpi/pigpio/python.html

LED=17

pi = pigpio.pi() # Connect to local Pi.

pi.set_mode(LED, pigpio.OUTPUT)

for i in range(10):
   pi.write(LED, 1)
   time.sleep(0.2)
   pi.write(LED, 0)
   time.sleep(0.2)

pi.stop() # Disconnect from local Pi.
