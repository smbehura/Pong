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
		
	        self.balls = pygame.sprite.RenderPlain()
	        self.paddles = pygame.sprite.RenderPlain()
	        self.walls = pygame.sprite.RenderPlain()
	
	        self.wall.append(<blank>) #add wall to list
	        self.walls.add(<blank>) #add wall to sprite list
	        ### do for all lists

	def setNumPlay(self, num):
		self.numPlayers = num

	def changeToLoss(self, player):
		# sets specified player's state variable to loss
		pass

	def checkForWin(self):
		# loops through all the players and checks for win
		pass
