
import RPi.GPIO as gpio
from time import sleep

def init(pin):
	gpio.setup(8, gpio.OUT)
	
def turnOn(pin):
	gpio.output(8,True)
	
def turnOff(pin):
	gpio.output(8,False)

	
### Main Program

print "Script is starting..."

print "Initializing pin 8..."
init(8)
print "Done."

while True:
	print "Turning on 8"
	turnOn(8)
	sleep(1)
	
	print "Turning off 8"
	turnOff(8)
	sleep(1)
	