'''
Ball Class
'''
from paddle_class import Paddle
from physical_object import PhysObj

import pygame, random, math

from wall_class import Wall


class Ball(PhysObj): # Ball inherits from the Physical Object class
    def __init__(self, color, vel, x, y):
        super(Ball, self).__init__(x, y)
        self.image = pygame.image.load("ball.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        # Set the attributes for the Ball object
        self.color = color 
        self.velocity = vel
        self.pos_x = x
        self.pos_y = y
        self.angle = random.random() * 2 * math.pi
        self.update_rect()
        pass

    # Set the velocity of the ball
    # input: integer value representing velocity
    # output: none but self.velocity is updated to new value
    def set_vel(self, velocity):
        self.velocity = velocity

    # Set the angle that the ball will bounce
    # input: integer value in radians representing angle
    # output: none but self.angle is updated to new input value
    def set_angle(self,angle):
        self.angle = angle
    
    # Set the color to the color chosen
    # input: color
    # output: none but self.color is updated to new input color
    def set_color(self, color):
        self.color = color

    # Returns angle
    # input: none
    # output: integer value representing current angle
    def get_angle(self):
        return self.angle

    # Returns color
    # input: none
    # output: color representing current color of Ball
    def get_color(self):
        return self.color

    # Returns velocity
    # input: none
    # output: integer value representing current velocity of Ball
    def get_velocity(self):
        return self.velocity

    # Changes x and y coordinates of the ball position and updates the location
    # input: none
    # output: none but x and y positions of Ball and rectangle of ball are updated
    def move(self):
        self.pos_x += (1 * self.velocity * math.cos(self.angle))
        self.pos_y += (1 * self.velocity * math.sin(self.angle))
        self.update_rect()

    # Collision function that changes direction of Ball when it collides with another physical object
    # input: physical object
    # output: none but changes self.angle depending on what type of physical object and orientation of object it hits
    def changeDir(self, obj):
        if self.isCollis(obj):
            # Collision function for if ball hits a paddle or a wall
            if type(obj) is Paddle or type(obj) is Wall:
                if obj.orientation % 2 == 0: # even number: top or bottom
                    # bottom: 5*pi/4 --> 3*pi/4; 7*pi/4 --> pi/4
                    # top: 3*pi/4 --> 5*pi/4; pi/4 --> 7*pi/4
                    self.angle = 2 * math.pi - self.angle
                elif obj.orientation % 2 == 1: # odd number: left or right
                    # right: 7*pi/4 --> 5*pi/4; pi/4 --> 3*pi/4
                    # left: 5*pi/4 --> 7*pi/4; 3*pi/4 --> pi/4
                    if self.angle <= math.pi:
                        self.angle = math.pi - self.angle
                    elif self.angle > math.pi:
                        self.angle = 3 * math.pi - self.angle
            # Collision function for if ball hits another ball
            elif type(obj) is Ball:
                # pi/4 --> 3*pi/4; 3*pi/4 --> pi/4; 5*pi/4 --> 7*pi/4; 7*pi/4 --> 5*pi/4
                if self.angle <= math.pi:
                    self.angle = math.pi - self.angle
                elif self.angle > math.pi:
                    self.angle = 3 * math.pi - self.angle
        return self.get_angle()
        #returns new angle of ball
        #if position of ball is equal to pos range of paddles then return true
        #loop through each paddle and add/subtract length of paddle
        
    # checks if ball is off screen (used later in function below)
    # input: none
    # output: boolean based on whether or not ball is on screen or off screen
    def isOffScreen(self):
        if 0 < self.pos_x and self.pos_x > 500 and 0 < self.pos_y and self.pos_y > 500:
            return False
        return True
        
    # returns orientation of player who lost ball and 0 if ball is still on board
    # input: none
    # output: returns integer representing orientation of wall that ball is off screen on (so losing player can be identified)
    def offScreenOrientation(self):
        if self.isOffScreen():
            if self.pos_x > 500 and self.pos_y < 500:
                return 1
            elif self.pos_x > 0 and self.pos_y > 500:
                return 2
            elif self.pos_x < 0 and self.pos_y > 0:
                return 3
            elif self.pos_x < 500 and self.pos_y < 0:
                return 4
        else:
            return 0
