'''
Physical Object class specifically to handle collisions and such things
'''

import pygame

class PhysObj(Sprite):
  def __init__(x, y):
  	self.image = pygame.image.load("blank.png").convert_alpha()
  	self.rect = self.image.get_rect()
	self.pos_x = x
	self.pos_y = y
	self.update_rect()
    
  def isCollis(self, obj):
    x = obj.get_x
    y = obj.get_y
    rect = obj.get_rect
    return self.rect.pygame.Rect.colliderect(rect)
  
  def get_x(self):
  	return self.pos_x

  def get_y(self):
	return self.pos_y
	
  def get_rect(self):
  	return self.rect
	
  def update_rect(self):
        self.rect.x = pos_x
        self.rect.y = pos_y
        
  def move():
  	pass
  
  def changeDir():
  	pass
        
