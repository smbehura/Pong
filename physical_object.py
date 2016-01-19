'''
Physical Object class specifically to handle collisions and such things
'''

import pygame

class PhysObj(Sprite):
  def __init__(self, location):
    self.location = location
  
  def isCollis(self, obj):
    # checks if input obj is touching self
    pass
