'''
Used to run and test Pong
'''

import pygame
from example_menu import main as menu

from board_class import Board

pygame.init()
window_size = [size_x * WIDTH + 175, size_y * HEIGHT + 20] # width, height
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pong')

result = menu(screen)
if result is None: #start game
    #determine variables
    board = Board(num_players, num_balls, ball_speed)
    clock = pygame.time.Clock()
    main_loop(screen, board, num_players, num_balls, ball_speed, clock, False, False)
# if result == 2: #load game
#     with open("saved_state.txt", "r") as f:
#         save_state = f.readline()
#     my_game = Game(screen, save_state)
#     my_game.play()

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
                    else:
                        pause = True

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

