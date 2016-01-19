'''
Board Class
'''

import pygame

class Board(object):
	def __init__(numPlayers, numBalls):
		self.numPlayers = numPlayers
		self.state = 0
		self.numBalls = numBalls
		self.balls = [] # list of balls in game which depends on self.numBalls
		self.players = [] # list of players in game which depends on self.numPlayers

	def setNumPlay(num):
		self.numPlayers = num

	def changeToLoss(player):
		# sets specified player's state variable to loss
		pass

	def checkForWin():
		# loops through all the players and checks for win
		pass
