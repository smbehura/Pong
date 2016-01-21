'''
Used to run and test Pong
'''

import pygame
from example_menu import main as menu
from example_menu import alt_main as instructions

from board_class import Board

pygame.init()
window_size = [500, 500] # width, height
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pong')

class Game(object):
    def __init__(self, screen, board, clock):
        self.screen = screen
        self.board = board
        self.clock = clock
        self.pause = False

    def pause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True
        
    def main_loop(self, num_players, num_balls, ball_speed):
        quit = False
        while not self.board.checkForWin() or not quit:
            self.screen.fill((0, 0, 0))
            self.board.paddles.draw(screen)
            self.board.balls.draw(screen)
            self.board.walls.draw(screen)
            pygame.display.flip()

            ###USER INPUT
            if not self.pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit = True
                        break
                    if event.type == pygame.KEYDOWN:
                        try:
                            if event.key == pygame.K_COMMA:
                                board.paddle[3].move(False)
                            elif event.key == pygame.K_PERIOD:
                                board.paddle[3].move(True)
                            elif event.key == pygame.K_c:
                                board.paddle[1].move(False)
                            elif event.key == pygame.K_v:
                                board.paddle[1].move(True)
                            elif event.key == pygame.K_q:
                                board.paddle[2].move(False)
                            elif event.key == pygame.K_a:
                                board.paddle[2].move(True)
                            elif event.key == pygame.K_UP:
                                board.paddle[0].move(False)
                            elif event.key == pygame.K_DOWN:
                                board.paddle[0].move(True)
                            elif event.key == pygame.K_p:
                                self.pause()
                        except Exception:
                            print "Invalid move."
    
                for ball in self.board.ball:
                    ball.move()
                    for object in self.board.objects:
                        ball.changeDir(object)
                    
                    orientation = ball.offScreenOrientation()
                    if orientation != 0:
                        self.board.changeToLoss(orientation)
                
                self.screen.fill((0, 0, 0))
                self.board.paddles.draw(screen)
                self.board.balls.draw(screen)
                self.board.walls.draw(screen)
    
                pygame.display.flip() # update screen
            self.clock.tick(1)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause()
        pygame.quit()

result = -1
while result == -1:
    screen.fill((0, 0, 0))
    pygame.display.flip()
    result = menu(screen)
    if result == 1: #start game
        print "***START GAME***"
        num_players = int(raw_input("Number of Players (1 to 4): "))
        num_balls = int(raw_input("Number of Balls (1 to 3): "))
        ball_speed = int(raw_input("Ball Speed (1 to 10): "))
        board = Board(num_players, num_balls, ball_speed)
        clock = pygame.time.Clock()
        game = Game(screen, board, clock)
        game.main_loop(num_players, num_balls, ball_speed)
    if result == 2: #instructions
        screen.fill((0, 0, 0))
        pygame.display.flip()
        result = instructions(screen)
        

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



# if stop == True:


        #     again = raw_input("Would you like to run the simulation again? If yes, type 'yes'\n")
        #     if again == 'yes':
        #         new_game()
        # while stop == False:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT: #user clicks close
        #             stop = True
        #             pygame.quit()
        #         elif event.type==pygame.KEYDOWN:
        #             if event.key==pygame.K_p:
        #                 if pause:
        #                     pause = False
        #                     print "GAME RESUMED"
        #                 else:
        #                     pause = True
        #                     print "GAME PAUSED"
