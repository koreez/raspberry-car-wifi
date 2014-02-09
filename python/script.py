
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

up = 8
down = 8
left = 8
right = 8

print "Script is starting..."

print "Initializing pins..."
init(up)
init(down)
init(left)
init(right)

print "Done."

while True:
	status = getStatus()
	
	if status == '1':
		print "Going UP"
		turnOn(up)
		
	elif status == '2':
		print "Going Back"
		turnOn(down)
		
	elif status == '3':
		print "Going Left"
		turnOn(left)
		
	elif status == '4':
		print "Going Right"
		turnOn(right)
		
	else:
		print "Idle"
		turnOff(up)
		turnOff(down)
		turnOff(left)
		turnOff(right)

	sleep(1)
