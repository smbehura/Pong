'''
Player Class
'''

class Player(object):
	def __init__(paddle, orientation):
		self.paddle = paddle
		self.orient = orientation #orientation means top, bottom, left, or right of window
		self.state = 0

	def get_paddle():
		return self.paddle

	def get_orient():
		return self.orient

	def get_state():
		return self.state

	def neutral():
		self.state = 0

	def win():
		self.state = 1

	def lose():
		self.state = -1
