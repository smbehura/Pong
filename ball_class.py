'''
Ball Class
'''

from physical_object import PhysObj

import pygame

class Ball(PhysObj):
	def __init__(self, color, vel):
		self.color = color
		self.velocity = vel
		pass

	def set_vel(self, velocity):
		self.velocity = velocity
		
	def set_color(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def get_velocity(self):
		return self.velocity
