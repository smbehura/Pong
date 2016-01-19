'''
Used to run and test Pong
'''

import pygame

from board_class import Board

pygame.init()
screen = pygame.display.set_mode((600,250)) #subject to change
pygame.display.set_caption('Pong')

game = Board() #something in here

game.play()



# initialize screen, do stuff idk
