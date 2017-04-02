# Python file for generator shapes

from interpretMood import *
# class MakeShape:
# 	def __init__(self, array, arrayo):
# 		self.array = [];
# 		self.arrayOfRectangles = [];

# 	def makeInputs(self):

square = 0

def makeDisplay(rhythmicIntensities, color, shape=None):
	""" 
	- Takes in a string, shape to be generated (e.g. square, circle, etc.) - default is square
	- Takes in an array of ints, time series data of the rhythmic intensity or volume level
	- Takes in a tuple, the color corresponding to mood from color module
	- Returns an array of tuples, each corresponding to an appropriate input to the appropriate function
	"""
	if shape is None:
		shape = square

	animationInputs = [0]*len(rhythmicIntensities);		
	for i in range(0, len(rhythmicIntensities)):
		print '0'
		# assume shape is square
		if rhythmicIntensities[i] < 0.5:
			animationInputs[i] = (3, 3, 2, 2, color)
		elif rhythmicIntensities[i] >= 0.5 and rhythmicIntensities < 0.7:
			animationInputs[i] = (2, 2, 4, 5, color)
		elif rhythmicIntensities[i] >= 0.7 and rhythmicIntensities < 0.9:
			animationInputs[i] = (1, 1, 6, 6, color)
		elif rhythmicIntensities[i] >= 0.9:
			animationInputs[i] = (0, 0, 8, 8, color)
	
	return animationInputs;

#def determineMood(rhythmicIntensities=None, key):
	
# def display(shape=None, deltaT, animationInputs):
# 	if shape is None:
# 		shape = square
# 	for (i = 0; i < len(animationInputs); i++):
# 		if shape is square:
# 			fill