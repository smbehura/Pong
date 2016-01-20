'''
Physical Object class specifically to handle collisions and such things
'''

import pygame

class PhysObj(object):
  def __init__(location, x, y):
    self.location = location
    self.pos_x = x
    self.pos_y = y
    
  def isCollis(obj):
    # checks if input obj is touching self
    pass
  
  def get_x(self):
		return self.pos_x
		
	def get_y(self):
		return self.pos_y
		
	def update_rect():
	  self.rect.x = pos_x
	  self.rect.y = pos_y
