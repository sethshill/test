# File: LEDfuncs
# Author: Seth Shill
# Date Created: 2/23/2017
# Description: Contains all the main functions to light the LEDs

import spidev
from time import sleep
from array import array


# Set global variables
numLEDs = 64

# Include predefined list of values
data_stream = array('B')
data_stream = [0] * (4*numLEDs + 8)
led,data = numLEDs, 4;
led_info = array('B')
led_info = [[0 for x in range(data)] for y in range(led)]


# Setup SPI
spi = spidev.SpiDev()
spi.open(0,0)	# Open bus 0, CE0 (bus 1 is at open(0,1))
# Settings
spi.max_speed_hz = 1000000
spi.mode = 0b01

def solid(r, g, b):
	"""Sets the entire 64-LED matrix one color based on r, g, b value and brightness. The first 3 values are ints ranging 0-255, where 255 is full brightness. brightness is a variable 0 to 1.0"""
		
	index = 0;	# Set start index
	# Set led_info array brightness and colors
	for i in range(numLEDs):
		led_info[i][0] = 0xFF
		led_info[i][1] = b
		led_info[i][2] = g
		led_info[i][3] = r
	# Set START bytes
	for start in range(4):
		data_stream[index] = 0x00 
		index += 1
	# Set DATA bytes
	for i in range(numLEDs):
		for j in range(4):
			data_stream[index] = led_info[i][j]
			index += 1
	# Set END bytes
	for i in range(4):
		data_stream[index] = 0xFF
		index += 1
	# Send data
	spi.xfer(data_stream)
def off():
	"""Turns off all LEDs."""
	
	index = 0;	# Set start index
	# Set led_info array brightness and colors
	for i in range(numLEDs):
		led_info[i][0] = 0xE0
		led_info[i][1] = 0x00
		led_info[i][2] = 0
		led_info[i][3] = 0
	# Set START bytes
	for start in range(4):
		data_stream[index] = 0x00 
		index += 1
	# Set DATA bytes
	for i in range(numLEDs):
		for j in range(4):
			data_stream[index] = led_info[i][j]
			index += 1
	# Set END bytes
	for i in range(4):
		data_stream[index] = 0xFF
		index += 1
	# Send data
	spi.xfer(data_stream)

def mkSqr(r,g,b,time=None):
	"""Takes in r,g,b colors and then makes a square that grows according to time speed."""
	if time is None:
		time = 0.1	# Set default value to 100 ms
	
	for k in range(4):	# Execute square 4x, from inner to outer
		
		index = 0;	# Set start index
		# Set led_info array colors for smallest square
		for i in range(numLEDs):
			if k == 0:
				if i == 27 or i == 28 or i == 35 or i == 36:
					led_info[i][0] = 0xFF
					led_info[i][1] = b
					led_info[i][2] = g
					led_info[i][3] = r
				else:
					led_info[i][0] = 0xE0
					led_info[i][1] = 0x00
					led_info[i][2] = 0
					led_info[i][3] = 0
			if k == 1:
				if i == 27 or i == 28 or i == 35 or i == 36:
					led_info[i][0] = 0xFF
					led_info[i][1] = b
					led_info[i][2] = g
					led_info[i][3] = r
				else:
					led_info[i][0] = 0xE0
					led_info[i][1] = 0x00
					led_info[i][2] = 0
					led_info[i][3] = 0
			if k == 2:
				if i == 27 or i == 28 or i == 35 or i == 36:
					led_info[i][0] = 0xFF
					led_info[i][1] = b
					led_info[i][2] = g
					led_info[i][3] = r
				else:
					led_info[i][0] = 0xE0
					led_info[i][1] = 0x00
					led_info[i][2] = 0
					led_info[i][3] = 0
			if k == 3:
				if i == 27 or i == 28 or i == 35 or i == 36:
					led_info[i][0] = 0xFF
					led_info[i][1] = b
					led_info[i][2] = g
					led_info[i][3] = r
				else:
					led_info[i][0] = 0xE0
					led_info[i][1] = 0x00
					led_info[i][2] = 0
					led_info[i][3] = 0
					 
		# Set START bytes
		for start in range(4):
			data_stream[index] = 0x00 
			index += 1
		# Set DATA bytes
		for i in range(numLEDs):
			for j in range(4):
				data_stream[index] = led_info[i][j]
				index += 1
		# Set END bytes
		for i in range(4):
			data_stream[index] = 0xFF
			index += 1
		# Send data
		spi.xfer(data_stream)
		time.sleep(time)
		
#~ def modulate(inFunc,freq = None):
	#~ while True:
		#~ inFunc
		#~ sleep(1)
		#~ off()
		#~ sleep(1)
		#~ sleep(1)
