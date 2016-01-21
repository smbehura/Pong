'''
Physical Object class specifically to handle collisions and such things
'''

import pygame

class PhysObj(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super(PhysObj, self).__init__()
    self.image = pygame.Surface([15, 15])
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
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
  def move(self):
    pass
  
  def changeDir(self):
    pass
        
  def move():
  	pass
  
  def changeDir():
  	pass
        
