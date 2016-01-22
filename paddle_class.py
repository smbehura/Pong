'''
Paddle Class
'''

from physical_object import PhysObj

import pygame

class Paddle(PhysObj):
    def __init__(self, color, x, y, orientation, ball_speed):
        super(Paddle, self).__init__(x, y)
        self.determine_image(orientation)
        self.rect = self.image.get_rect()
        # Assign the attributes to the paddle
        self.color = color
        self.pos_x = x
        self.pos_y = y
        self.ball_speed = ball_speed
        self.orientation = orientation
        self.update_rect()
        #need function in player class to turn player orientation into paddle location

    # Function determines which image to load for the paddle depending on which player number they are
    # Takes in a number and sets the image of the paddle accordingly
    # Returns None
    def determine_image(self, num):
        if num == 1:
            self.image = pygame.image.load("paddle_R.png").convert_alpha()
        elif num == 2:
            self.image = pygame.image.load("paddle_B.png").convert_alpha()
        elif num == 3:
            self.image = pygame.image.load("paddle_L.png").convert_alpha()
        elif num == 4:
            self.image = pygame.image.load("paddle_T.png").convert_alpha()

    # Returns the color of the paddle
    def get_color(self):
        return self.color

    # Takes in boolean posOrNeg and determines which direction to move the paddle
    # If posOrNeg is True, then the paddle will move either right or down depending on if they player's number (orientation) is even or odd
    def move(self, posOrNeg):
        if posOrNeg == True:
            if self.orientation % 2 == 0 and self.pos_x + 5 <= 500:
                self.pos_x += self.ball_speed + 5 # moves paddle right
                self.update_rect()
            elif self.orientation % 2 == 1 and self.pos_y + 5 <= 500:
                self.pos_y += self.ball_speed + 5 # moves paddle down
                self.update_rect()
    
    # If posOrNeg is False, then the paddle will either move left or right depending on if they player's number (orientation) is even or odd
        elif posOrNeg == False:
            if self.orientation % 2 == 0 and self.pos_x - 5 >= 0:
                self.pos_x -= self.ball_speed + 5 # moves paddle left 
                self.update_rect()
            elif self.orientation % 2 == 1 and self.pos_y - 5 >= 0:
                self.pos_y -= self.ball_speed + 5 # moves paddle up
                self.update_rect()

    # Update the position of the paddle
    # Returns None
    def update_rect(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
