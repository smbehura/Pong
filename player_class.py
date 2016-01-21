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
		return self.paddle

	def get_orient(self):
		return self.orient

	def get_state(self):
		return self.state

	def neutral(self):
		self.state = 0

	def win(self):
		self.state = 1

	def lose(self):
		self.state = -1
