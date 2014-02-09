
import RPi.GPIO as gpio
from time import sleep

def init(pin):
	gpio.setup(8, gpio.OUT)
	
def turnOn(pin):
	gpio.output(8,True)
	
def turnOff(pin):
	gpio.output(8,False)
	
def getStatus():
	f = open('../script/input.txt', 'r')
	return f.read(1)

	
### Main Program

print "Script is starting..."

print "Initializing pin 8..."
init(8)
print "Done."

while True:
	status = getStatus()
	
	if status == '1':
		print "Going UP"
		turnOn(8)
		
	else:
		print "Idle"
		turnOff(8)

	sleep(1)
