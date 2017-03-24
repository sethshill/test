# File: interpretMood.py
# Author: Seth Shill
# Date Created: 2/23/2017
# Description: Contains functions for interpreting mood from data, and generating output based on mood.

from LEDfuncs import*
import collections	# For using millisecond function
from time import sleep

class Mood(object):
	def __init__(self,valence,arousal):
		self.valence = valence
		self.arousal = arousal
		
# Set Global Variables
mood = Mood(60,60)		# Set default values

def displayMood(mood):
	"""This function takes in mood, a class valence and arousel levels (1-100) and returns nothing. It does however generate a unique color 
	and displays this color on an 8x8 matrix."""
	#~ print(mood.valence, mood.arousal)
	if mood.valence < 50 and mood.arousal > 50:
		# Describes Exuberance
		solid(250,50,0)		# Red (mostly)
		print('Exuberance, Red (not working yet)')
	if mood.valence > 50 and mood.arousal > 50:
		# Describes Anxious/Frantic
		solid(220,125,0)	# Orange
		print('Anxious, Orange')
	if mood.valence > 50 and mood.arousal < 50:
		# Describes Depression
		solid(0,0,250)		# Blue
		print('Depression, Blue')
	if mood.valence < 50 and mood.arousal < 50:
		# Describes Contentment
		solid(250,200,0)	# Yellow
		print('Contentment, Yellow')

def genMood(mood = Mood(50,50), key = None,rhythm = None,dynamic = None,tempo= None):
	"""Takes in a string (key) and 3 integers (rythIntensity, dynamic, tempo). Returns a tuple of arousal and valence levels."""
	
	# Set dummy variables for each component's respective contribution to valence (stress, x) and arousal (energy, y)
	keyValence = 0
	keyArousal = 0
	rythmArousal = 0
	# Analyze musical keys (based on Charpentier's Regles de Composition ca. 1682, biteyourownelbow.com/keychar.htm)
	if any([key == 'Cma', key == 'Dma', key == 'Emi', key == 'Gma', key == 'Gmi']):	# Exuberance: gay, warlike, joyous, effeminate, amorous, plaintiff, serious and magnificent 
		keyValence = 25
		keyArousal = 75
	if any([key == 'Ama', key == 'Bmi', key == 'Bbma']):	# Contentment: joyful and pastoral, solitary and melecholny, magnificant & joyful
		keyValence = 25
		keyArousal = 25
	if any([key == 'Dmi', key == 'Ebma', key == 'Ema', key == 'Fma', key == 'Bma']):	# Anxious/Frantic: serious and pious, quarrelsome and boisterous, furious and quick-tempered subjecteds, harsh and plaintiff
		keyValence = 75
		keyArousal = 75
	if any([key == 'Fmi', key == 'B', key == 'Ami', key == 'Bbmi']):	# Depression: obscure and plaintiff, tender and plaintiff, obscure and terrible
		keyValence = 75
		keyArousal = 25	
	
	# Analyze rythmic intensity
	if rhythm > 50:
		rythmArousal = 80	# to return arousal average >50
	if rhythm < 50:
		rythmArousal = 20 # to return arousal average < 50
	
	# Calculate valence and arousal as averages
	mood.valence = keyValence
	mood.arousal = (keyArousal + rythmArousal)/2
	return mood
