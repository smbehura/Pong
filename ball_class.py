'''
Ball Class
'''

from physical_object import PhysObj

import pygame, random, math

class Ball(PhysObj):
<<<<<<< HEAD
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

    def is_collided(self):
        #should return if it collides with a paddle, wall, or ball
        #if position of ball is equal to pos range of paddles then return true
        #loop through each paddle and add/subtract length of paddle
        pass

    def changeColor(self):
        #changes color based on paddle hit
        pass

    def move(self):
        self.pos_x += (0.5 * self.velocity * math.cos(self.angle))
        self.pos_y += (0.5 * self.velocity * math.sin(self.angle))
        self.update_rect()

    def changeDir(self, obj):
        pass
=======
	def __init__(self, color, vel, x, y):
		self.image = pygame.image.load("blank.png").convert_alpha()
  		self.rect = self.image.get_rect()
		self.color = color
		self.velocity = vel
		self.pos_x = x
		self.pos_y = y
		angle = random.random() * 2 * math.pi
		self.angle = angle
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

	def is_collided(self):
		#should return if it collides with a paddle, wall, or ball
		#if position of ball is equal to pos range of paddles then return true
		#loop through each paddle and add/subtract length of paddle
		pass

	def changeColor(self):
		#changes color based on paddle hit
		pass

	def move(self, velocity):
		self.pos_x += (0.5 * velocity * math.cos(self.angle))
		self.pos_y += (0.5 * velocity * math.sin(self.angle))
		self.update_rect()
		
	def changeDir(self, obj):
		pass
>>>>>>> origin/master
