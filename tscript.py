# For testing python functions
from shapeGen import*
import random

# Run test
sampleRhythmicIntensities = [0]*100;
blue = (0,255,0);	#sample color for shape
for i in range(0, 100):
	sampleRhythmicIntensities[i] = random.random()
print makeDisplay(sampleRhythmicIntensities, blue)
