'''
Used to run and test Pong
'''

import pygame
from example_menu import main as menu

from board_class import Board

pygame.init()
window_size = [500, 500] # width, height
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pong')

result = 2
while result == 2:
    result = menu(screen)
    if result == 1: #start game
        print "***START GAME***"
        num_players = int(raw_input("Number of Players (1 to 4): "))
        num_balls = int(raw_input("Number of Balls (1 to 3): "))
        ball_speed = int(raw_input("Ball Speed (1 to 10): "))
        board = Board(num_players, num_balls, ball_speed)
        clock = pygame.time.Clock()
        main_loop(screen, board, num_players, num_balls, ball_speed, clock, False, False)
    if result == 2: #instructions
        print "***INSTRUCTIONS***"
        print 
        print "USER INPUT"
        print "•Player 1 (right): up/down keys"
        print "•Player 2 (bottom): C/V keys"
        print "•Player 3 (left): Q/A keys"
        print "•Player 4 (top): </> keys"
        print 
        print "HOW TO WIN"
        print "1-Player Mode:"
        print "•Try to keep the ball in play for as long as possible in order to beat the previous 1-player score."
        print "Multipllayer Mode"
        print "•Try to keep the ball from running of the screen."
        print "•Each time a player misses the ball, he/she is eliminated from the game and replaced with a bouncing wall."
        print "•The game keeps running until one player (the winner) is left."
        print 
        print "Press P at anytime to pause the game."
        

def main_loop(screen, board, num_players, num_balls, ball_speed, clock, stop, pause):
    board.paddles.draw(screen)
    board.balls.draw(screen)
    board.walls.draw(screen)
    pygame.display.flip() 

    if stop == True:
        again = raw_input("Would you like to run the simulation again? If yes, type 'yes'\n")
        if again == 'yes':
            new_game()
    while stop == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks close
                stop = True
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    if pause:
                        pause = False
                        print "GAME RESUMED"
                    else:
                        pause = True
                        print "GAME PAUSED"

        if stop == False and pause == False:
            ###USER INPUT
            ###UPDATE VALUES FOR MOVABLE OBJECTS
            board.paddles.draw(screen)
            board.balls.draw(screen)
            board.walls.draw(screen)

            #text
            #change the color of the ball
            pygame.display.flip() # update screen
            clock.tick(.5)
    pygame.quit() # closes things, keeps idle from freezing


# parsed = False
#   while not parsed:
#       try:
#           size_y = int(raw_input("NUMBER OF ROWS: "))
#           parsed = True
#       except ValueError:
#           print "INVALID INPUT"

# parsed = False
#   while not parsed:
#       try:
#           size_x = int(raw_input("NUMBER OF COLUMNS: "))
#           parsed = True
#       except ValueError:
#           print "INVALID INPUT"

