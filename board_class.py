'''
Board Class
'''

import pygame

class Board(object):
	def __init__(self, numPlayers, numBalls):
		self.numPlayers = numPlayers
		self.state = 0
		self.numBalls = numBalls
		self.balls = [] # list of balls in game which depends on self.numBalls
		self.players = [] # list of players in game which depends on self.numPlayers
		self.paddles = [] #list of paddles in game which depends on self.numPlayers
		self.walls = [] #list of the positions of the walls that will be used for bouncing

	def setNumPlay(self, num):
		self.numPlayers = num

	def changeToLoss(self, player):
		# sets specified player's state variable to loss
		pass

	def checkForWin(self):
		# loops through all the players and checks for win
		pass
	
	def play(self):
		# runs through entire game and plays Pong, must include ball starting etc.
