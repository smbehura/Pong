'''
Player Class
'''

from ball_class import Ball
from paddle_class import Paddle

import pygame

class Player(object):
	def __init__(self, paddle, orientation):
		self.paddle = paddle
		self.orient = orientation #orientation means top, bottom, left, or right of window
		self.state = 0

	def get_paddle(self):
		'''
		returns paddle variable
		'''
		return self.paddle

	def get_orient(self):
		'''
		returns orient variable
		'''
		
		return self.orient

	def get_state(self):
		'''
		returns state variable
		'''
		
		return self.state

	def neutral(self):
		'''
		sets state variable to 0
		returns None
		'''
		
		self.state = 0

	def win(self):
		'''
		sets state variable to 1
		returns None
		'''
		
		self.state = 1

	def lose(self):
		'''
		sets state variable to -1
		returns None
		'''
		self.state = -1
