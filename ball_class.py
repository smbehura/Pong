'''
Ball Class
'''

from physical_object import PhysObj

import pygame

class Ball(PhysObj):
	def __init__(color, vel):
		self.color = color
		self.velocity = vel
		pass

	def set_vel(velocity):
		self.velocity = velocity

	def get_color():
		return self.color

	def get_velocity():
		return self.velocity
