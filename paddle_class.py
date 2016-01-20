'''
Paddle Class
'''

from physical_object import PhysObj

import pygame

class Paddle(PhysObj):
	def __init__(self, color, location, x, y):
		self.image = pygame.image.load("blank.png").convert_alpha()
  		self.rect = self.image.get_rect()
		self.color = color
		self.pos_x = x
		self.pos_y = y
		self.location = location #based on orientation
		self.update_rect()
		#need funciton in player class to turn player orientation into paddle location

	def get_color(self):
		return self.color

	def get_loc(self):
		return self.location

	def move(self):
		self.update_rect()
		pass

	def isPaddleofPlayer(self, player):
		# this function will probably need to moved to the player class
		pass

	def draw():
		# draw paddle using location and stuff
		pass
