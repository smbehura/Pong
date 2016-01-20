'''
Wall Class
'''

import pygame

class Wall(PhysOjb):
  def __init__(orientation):
    self.orientation = orientation
    if orientation % 2 == 0:
      self.image = pygame.image.load('wall_H.png').convert_alpha()
    elif orientation % 2 == 1:
      self.image = pygame.image.load('wall_V.png').convert_alpha()
    else:
      print 'Error: orientation is not defined or is not a number'
