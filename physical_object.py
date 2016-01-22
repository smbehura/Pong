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
    
  # isCollis checks if self has collided or has overlap with input object
  # input: object which self is being checked against (for overlap)
  # output: boolean depending on whether or not there is overlap/collision
  def isCollis(self, obj):
    x = obj.get_x
    y = obj.get_y
    rect = obj.get_rect()
    rect2 = self.get_rect()
    # print rect2.colliderect(rect)
    # print rect, rect2
    # return False
    return rect2.colliderect(rect)
  
  # get_x returns the x position of self
  # input: none
  # output: integer value representing x position
  def get_x(self):
    return self.pos_x

  # get_y returns the y position of self
  # input: none
  # output: integer value representing y position
  def get_y(self):
    return self.pos_y

  # get_rect returns the rectangle representing self
  # input: none
  # output: rectangle object that represents self
  def get_rect(self):
    return self.rect

  # update_rect updates rectangle object with current selfs' positions x and y
  # input: none
  # output: none but self.rect is updated to most recent changes in x and y positions
  def update_rect(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
  # move allows subclasses to override this function and provide their own method
  # input: none
  # output: none
  def move(self):
    pass
  
  # changeDir allows subclasses to override this function and provide their own method
  # input: none
  # output: none
  def changeDir(self):
    pass
