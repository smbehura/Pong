'''
Board Class
'''

import pygame
from paddle_class import Paddle
from ball_class import Ball
from player_class import Player
from wall_class import Wall

class Board(object):
    def __init__(self, num_players, num_balls, ball_speed):
        self.num_players = num_players
        self.num_balls = num_balls
        self.ball_speed = ball_speed

        self.ball = [] # list of balls in game which depends on self.numBalls
        self.player = [] # list of players in game which depends on self.numPlayers
        self.paddle = [] #list of paddles in game which depends on self.numPlayers
        self.wall = [] #list of the walls that will be used for bouncing

        white = (0, 0, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)

        for num in range(num_balls):
            self.ball.append(Ball(white, ball_speed, 250, 250)) #determine x, y

        for num in range(num_players):
            if num == 0:
                new_paddle = Paddle(red, 480, 200, num + 1)
                self.paddle.append(new_paddle)
            elif num == 1:
                new_paddle = Paddle(blue, 200, 480, num + 1)
                self.paddle.append(new_paddle)
            elif num == 2:
                new_paddle = Paddle(yellow, 5, 200, num + 1)
                self.paddle.append(new_paddle)
            elif num == 3:
                new_paddle = Paddle(green, 200, 5, num + 1)
                self.paddle.append(new_paddle)
            new_player = Player(new_paddle, num + 1)
            self.player.append(new_player)

        for num in range(4, num_players, -1):
            if num == 1:
                new_wall = Wall(num, 480, 0)
            elif num == 2:
                new_wall = Wall(num, 0, 480)
            elif num == 3:
                new_wall = Wall(num, 0, 0)
            elif num == 4:
                new_wall = Wall(num, 0, 0)
            self.wall.append(new_wall)

        self.balls = pygame.sprite.RenderPlain()
        self.paddles = pygame.sprite.RenderPlain()
        self.walls = pygame.sprite.RenderPlain()

        #adds objects to sprite lists for drawing purposes
        for obj in self.ball:
            self.balls.add(obj)
        for obj in self.paddle:
            self.paddles.add(obj)
        for obj in self.wall:
            self.walls.add(obj)

        self.objects = self.ball + self.paddle + self.wall

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
        for person in self.player:
            if person.state == 1:
                return True
        return False

    def checkCollandDir(self):
        for obj in self.objects:
            for obj2 in self.objects:
                if obj.isCollis(obj2):
                    if type(obj) == Ball:
                        obj.changeDir()

    def idk(self):
        pass
