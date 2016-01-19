'''
Paddle Class
'''

from physical_object import PhysObj

import pygame

class Paddle(PhysObj):
	def __init__(self, color, location, x, y):
		self.color = color
		self.location = location #based on orientation
		#need funciton in player class to turn player orientation into paddle location
		self.pos_x = x
		self.pos_y = y

	def get_color(self):
		return self.color

	def get_loc(self):
		return self.location

	def move(self):
		pass

	def isPaddleofPlayer(self, player):
		# this function will probably need to moved to the player class
		pass

	"""
	def draw(self):
		# draw paddle using location and stuff
		pass
	"""
	
	def get_x(self):
		return self.pos_x
		
	def get_y(self):
		return self.pos_y
