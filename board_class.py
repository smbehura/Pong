'''
Board Class
'''

import pygame
from paddle_class import Paddle
from ball_class import Ball
from player_class import Player
from wall_class import Wall
import random

class Board(object):
    white = (0, 0, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, num_players, num_balls, ball_speed):
        self.num_players = num_players
        self.num_balls = num_balls
        self.ball_speed = ball_speed

        self.ball = [] # list of balls in game which depends on self.numBalls
        self.player = [] # list of players in game which depends on self.numPlayers
        self.paddle = [] #list of paddles in game which depends on self.numPlayers
        self.wall = [] #list of the walls that will be used for bouncing

        for num in range(num_balls):
            self.ball.append(Ball(self.white, ball_speed, random.randint(200,300), random.randint(200,300))) #determine x, y

        for num in range(num_players):
            if num == 0:
                new_paddle = Paddle(self.red, 480, 200, num + 1)
                self.paddle.append(new_paddle)
            elif num == 1:
                new_paddle = Paddle(self.blue, 200, 480, num + 1)
                self.paddle.append(new_paddle)
            elif num == 2:
                new_paddle = Paddle(self.yellow, 5, 200, num + 1)
                self.paddle.append(new_paddle)
            elif num == 3:
                new_paddle = Paddle(self.green, 200, 5, num + 1)
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
        self.num_players = num

    def changeToLoss(self, player_num):
        player = None
        for person in self.player:
            if player_num == person.orient:
                player = person
                break;

        if player is not None:
            player.lose()
            self.paddle.remove(player.paddle)
            self.paddles.remove(player.paddle)

            num = player.orient
            if num == 1:
                new_wall = Wall(num, 480, 0)
            elif num == 2:
                new_wall = Wall(num, 0, 480)
            elif num == 3:
                new_wall = Wall(num, 0, 0)
            elif num == 4:
                new_wall = Wall(num, 0, 0)
            self.wall.append(new_wall)
            self.walls.add(new_wall)

            self.ball = []
            for num in range(self.num_balls):
                self.ball.append(Ball(self.white, self.ball_speed, random.randint(200,300), random.randint(200,300))) #determine x, y
            self.balls = pygame.sprite.RenderPlain()
            for obj in self.ball:
                self.balls.add(obj)
            self.objects = self.ball + self.paddle + self.wall
        

    def checkForWin(self):
        if (len(self.wall) == 3 and len(self.player) != 1) or (len(self.wall) == 4 and len(self.player) == 1):
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
