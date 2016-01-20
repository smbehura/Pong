'''
Board Class
'''

import pygame

class Board(object):
	def __init__(self, num_players, num_balls, ball_speed):
		self.num_players = num_players
		self.num_balls = num_balls
		self.ball_speed = ball_speed
		
		self.ball = [] # list of balls in game which depends on self.numBalls
		self.player = [] # list of players in game which depends on self.numPlayers
		self.paddle = [] #list of paddles in game which depends on self.numPlayers
		self.wall = [] #list of the positions of the walls that will be used for bouncing
		
		white = (0, 0, 0)
		red = (255, 0, 0)
		yellow = (255, 255, 0)
		green = (0, 255, 0)
		blue = (0, 0, 255)
		
		for num in range(num_balls):
			balls.append(Ball(white, ball_speed, x, y)) #determine x, y
			
		for num in range(num_players):
			if num == 0:
				paddle.append(Paddle(red, 480, 150, num + 1)
			if num == 1:
				paddle.append(Paddle(blue, 150, 480, num + 1)
			if num == 2:
				paddle.append(Paddle(yellow, 5, 150, num + 1)
			if num == 3:
				paddle.append(Paddle(green, 150, 5, num + 1)
			player.append(Player(paddle, num + 1))
			
		for num in range(4, num_players, -1):
			wall.append(Wall(num))
		
	        self.balls = pygame.sprite.RenderPlain()
	        self.paddles = pygame.sprite.RenderPlain()
	        self.walls = pygame.sprite.RenderPlain()
	
		#adds objects to sprite lists for drawing purposes
		for obj in ball:
			self.balls.add(obj)
		for obj in paddle:
			self.paddles.add(obj)
		for obj in wall:
			self.walls.add(obj)
	
	def setNumPlay(self, num):
		self.numPlayers = num

	def changeToLoss(self, player):
		player.lose()
		self.paddle.remove(player.paddle)
		self.paddles.remove(player.paddle)
		
		new_wall = Wall(player.orientation)
		self.wall.append(new_wall)
		self.walls.add(new_wall)

	def checkForWin(self):
		for person in player:
			if person.state == 1:
				return true
		return false
