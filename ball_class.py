'''
Ball Class
'''

from physical_object import PhysObj

import pygame

class Ball(PhysObj):
	def __init__(self, color, vel, x, y):
		self.color = color
		self.velocity = vel
		self.pos_x = x
		self.pos_y = y
		pass

	def set_vel(self, velocity):
		self.velocity = velocity
		
	def set_color(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def get_velocity(self):
		return self.velocity
	
	def get_x(self):
		return self.pos_x
		
	def get_y(self):
		return self.pos_y
