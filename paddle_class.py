'''
Paddle Class
'''

from physical_object import PhysObj

import pygame

class Paddle(PhysObj):
	def __init__(self, color, x, y, orientation):
		determine_image(orientation)
  		self.rect = self.image.get_rect()
		self.color = color
		self.pos_x = x
		self.pos_y = y
		self.orientation = orientation
		self.update_rect()
		#need funciton in player class to turn player orientation into paddle location

	def determine_image(self, num):
		if num == 1:
			self.image = pygame.image.load("paddle_R.png").convert_alpha()
		elif num == 2: 
			self.image = pygame.image.load("paddle_B.png").convert_alpha()
		elif num == 3: 
			self.image = pygame.image.load("paddle_L.png").convert_alpha()
		elif num == 4: 
			self.image = pygame.image.load("paddle_T.png").convert_alpha()

	def get_color(self):
		return self.color

	def move(self, posOrNeg):
		if posOrNeg = True:
			if self.orientation % 2 = 0:
				self.pos_x += 5 # moves paddle right
				self.update_rect()
			elif self.orientation % 2 = 1:
				self.pos_y += 5 # moves paddle down
				self.update_rect()
	
		elif posOrNeg = False:
			if self.orientation % 2 = 0:
				self.pos_x -= 5 # moves paddle left
				self.update_rect()
			elif self.orientation % 2 = 1:
				self.pos_y -= 5 # moves paddle up
				self.update_rect()

	def isPaddleofPlayer(self, player):
		# this function will probably need to moved to the player class
		pass

	def draw():
		# draw paddle using location and stuff
		pass
