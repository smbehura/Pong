'''
Wall Class
'''

import pygame
from physical_object import PhysObj

class Wall(PhysObj): # Inherits functions from superclass PhysObj
  def __init__(self, orientation, x, y):
    super(Wall, self).__init__(x, y)
    # Sets the attributes of wall
    self.orientation = orientation
    self.pos_x = x
    self.pos_y = y
    # Determines if the wall is horizontal or vertical by seeing if the orientation number is even or odd
    # Uploads the appropriate image according to the parity of the number
    if orientation % 2 == 0:
      self.image = pygame.image.load('wall_H.png').convert_alpha()
    elif orientation % 2 == 1:
      self.image = pygame.image.load('wall_V.png').convert_alpha()
    else:
      print 'Error: orientation is not defined or is not a number'
    # Update the image of the wall
    self.rect = self.image.get_rect()
    self.update_rect()
