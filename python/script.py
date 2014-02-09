
import RPi.GPIO as gpio
from time import sleep

def uklop():
	gpio.setup(8, gpio.OUT)
	gpio.output(8,True)
	sleep(1)
	gpio.output(8,False)
	sleep(1)
	
for num in range(1,10):
	uklop()
	