'''
Ball Class
'''

from physical_object import PhysObj

import pygame, random, math

class Ball(PhysObj):
    def __init__(self, color, vel, x, y):
        super(Ball, self).__init__(x, y)
        self.image = pygame.image.load("ball.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.color = color
        self.velocity = vel
        self.pos_x = x
        self.pos_y = y
        self.angle = random.random() * 2 * math.pi
        self.update_rect()
        pass

    def set_vel(self, velocity):
        self.velocity = velocity

    def set_angle(self,angle):
        self.angle = angle

    def set_color(self, color):
        self.color = color

    def get_angle(self):
        return self.angle

    def get_color(self):
        return self.color

    def get_velocity(self):
        return self.velocity

    def changeColor(self):
        #changes color based on paddle hit
        pass

    def move(self):
        self.pos_x += (0.5 * self.velocity * math.cos(self.angle))
        self.pos_y += (0.5 * self.velocity * math.sin(self.angle))
        self.update_rect()

    def changeDir(self, obj):
        if self.isCollis(obj):
        	if type(obj) is Paddle:
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
