
import RPi.GPIO as gpio
from time import sleep

def uklop():
	gpio.setup(8, gpio.OUT)
	puts "Turning on 8"
	gpio.output(8,True)
	sleep(1)
	puts "Turning off 8"
	gpio.output(8,False)
	sleep(1)
	
	
print "Script is starting..."
for num in range(1,10):
	uklop()

print "Done."
