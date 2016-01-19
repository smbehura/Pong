'''
Paddle Class
'''
import pygame

class Paddle(PhysObj):
	def __init__(color, location):
		self.color = color
		self.location = location #based on orientation
		#need funciton in player class to turn player orientation into paddle location

	def get_color():
		return self.color

	def get_loc():
		return self.location

	def move():
		pass

	def isPaddleofPlayer(player):
		# this function will probably need to moved to the player class
		pass

	def draw():
		# draw paddle using location and stuff
		pass
