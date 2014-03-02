
import RPi.GPIO as gpio
from time import sleep

def init(pin):
	gpio.setup(pin, gpio.OUT)

def turnOn(pin):
	gpio.output(pin,False)

def turnOff(pin):
	gpio.output(pin,True)

def getStatus():
	f = open('../script/input.txt', 'r')
	return f.read(1)


### Main Program

up = 7
down = 8
left = 11
right = 15

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
		# turnOn(up)
		turnOn(left)

	elif status == '4':
		print "Going Right"
		# turnOn(up)
		turnOn(right)

	else:
		turnOff(up)
		turnOff(down)
		turnOff(left)
		turnOff(right)

	sleep(0.1)
