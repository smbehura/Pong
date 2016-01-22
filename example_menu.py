#! /usr/bin/python

## \file  example_simple.py
#  \brief A (very simple) example of using the menu system
#  \author Scott Barlow
#  \date 2009
#  \version 1.0.0
#
#  An example script to create a window and explore some of the features of the
#  menu class I've created.  This script just creates a very simple menu for
#  users that just want to see a plain and simply menu.  This could be made even
#  more simple, but I keep some features I deem "essential" (such as
#  non-blocking code and only updating the portion of the screen that changed).
#
#
#       Copyright 2009 Scott Barlow
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA or see <http://www.gnu.org/licenses/>.
#
#
#  Changelog
#     V1.0.0 - Initial Release
#     V1.0.1 - No change to this file
#     V1.0.2 - No change to this file
#     V1.0.3 - No change to this file
#


#-------------------------------------------------------------------------------
#---[ Imports ]-----------------------------------------------------------------
#-------------------------------------------------------------------------------
import sys, pygame
from menu import *


## ---[ main ]------------------------------------------------------------------
#  This function runs the entire screen and contains the main while loop
#

def main(screen):
   '''
   main menu when game is opened
   '''

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu = cMenu(0, 0, 0, 0, 'vertical', 100, screen,
               [("Title",         0, pygame.image.load('pong.png').convert_alpha()),
                ('Start Game',    1, pygame.image.load('start.png').convert_alpha()),
                ('Instructions',  2, pygame.image.load('instructions.png').convert_alpha()),
                ('Quit',          3, pygame.image.load('quit.png').convert_alpha())])

   # Center the menu on the draw_surface (the entire screen here)
   menu.set_center(True, True)

   # Center the menu on the draw_surface (the entire screen here)
   menu.set_alignment('center', 'center')

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.MOUSEBUTTONDOWN or e.type == EVENT_CHANGE_STATE:
         if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = tuple(e.pos)
            if x >= 130 and x <= 305 and y >= 180 and y <= 220:
               state = 1
            elif x >= 120 and x <= 320 and y >= 260 and y <= 300:
               state = 2
            elif x >= 170 and x <= 260 and y >= 340 and y <= 380:
               state = 3
            else:
               state = 0
         if state == 0:
            rect_list, state = menu.update(e, state)
         elif state == 1:
            print 'Start Game!'
            state = 0
            return 1
         elif state == 2:
            print 'Instructions!'
            state = 0
            return 2
         else:
            print 'Quit!'
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      # Update the screen
      pygame.display.update(rect_list)

def alt_main(screen):
   '''
   instructions menu when instruction button is clicked
   '''

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu = cMenu(0, 0, 0, 0, 'vertical', 100, screen,
               [("Back to Menu", 1, pygame.image.load('back.png').convert_alpha())])

   myfont = pygame.font.SysFont("monospace", 40)
   inst = myfont.render("INSTRUCTIONS", 1, (255,255,255))

   myfont = pygame.font.SysFont("monospace", 25)
   input = myfont.render("USER INPUT", 1, (0,120,161))
   win = myfont.render("HOW TO WIN", 1, (0,120,161))
   pause = myfont.render("Press 'P' at anytime to pause", 1, (0,120,161))
   pause1 = myfont.render("the game.", 1, (0,120,161))

   myfont = pygame.font.SysFont("monospace", 17)
   onep = myfont.render("1-Player Mode:", 1, (93,190,222))
   multip = myfont.render("Multiplayer Mode:", 1, (93,190,222))

   myfont = pygame.font.SysFont("monospace", 13)
   p1 = myfont.render("Player 1 (right): up/down keys", 1, (255,0,0))
   p2 = myfont.render("Player 2 (bottom): C/V keys", 1, (0,15,255))
   p3 = myfont.render("Player 3 (left): Q/A keys", 1, (255,255,0))
   p4 = myfont.render("Player 4 (top): </> keys", 1, (0,255,0))
   onep1 = myfont.render("-Try to keep the ball in play for as long as possible", 1, (255,255,255))
   onep2 = myfont.render(" in order to beat the previous 1-player score.", 1, (255,255,255))
   multip1 = myfont.render("-Take note of the amount of players and which keys should be", 1, (255,255,255))
   multip11 = myfont.render(" used.", 1, (255,255,255))
   multip2 = myfont.render("-Try to keep the ball from running of the screen by using your", 1, (255,255,255))
   multip21 = myfont.render(" paddle.", 1, (255,255,255))
   multip3 = myfont.render("-Each time a player misses the ball, he/she is eliminated from", 1, (255,255,255))
   multip31 = myfont.render(" the game and replaced with a bouncing wall.", 1, (255,255,255))
   multip4 = myfont.render("-The game keeps running until one player (the winner) is left.", 1, (255,255,255))

   screen.blit(inst, (210, 0))

   screen.blit(input, (3, 50))
   screen.blit(p1, (3, 75))
   screen.blit(p2, (3, 90))
   screen.blit(p3, (3, 105))
   screen.blit(p4, (3, 120))

   screen.blit(win, (3, 145))
   screen.blit(onep, (3, 170))
   screen.blit(onep1, (3, 190))
   screen.blit(onep2, (3, 205))
   screen.blit(multip, (3, 230))
   screen.blit(multip1, (3, 250))
   screen.blit(multip11, (3, 265))
   screen.blit(multip2, (3, 280))
   screen.blit(multip21, (3, 295))
   screen.blit(multip3, (3, 310))
   screen.blit(multip31, (3, 325))
   screen.blit(multip4, (3, 340))

   screen.blit(pause, (3, 365))
   screen.blit(pause1, (3, 390))

   pygame.display.flip()

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.MOUSEBUTTONDOWN or e.type == EVENT_CHANGE_STATE:
         if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = tuple(e.pos)
            if x >= 0 and x <= 205 and y >= 0 and y <= 40:
               state = -1
            else:
               state = 0
         if state == 0:
            rect_list, state = menu.update(e, state)
         elif state == -1:
            print 'Menu!'
            state = 0
            return -1
         else:
            print 'Quit!'
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      # Update the screen
      pygame.display.update(rect_list)

def nalt_main(screen):
   '''
   options screen where user inputs game values
   '''
   
   input_list = [1, 1, 5]

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu = cMenu(0, 0, 0, 0, 'vertical', 100, screen,
               [("Start Game", 1, pygame.image.load('start.png').convert_alpha())])

   p1 = pygame.image.load('p1.png').convert_alpha()
   p2 = pygame.image.load('p2.png').convert_alpha()
   p3 = pygame.image.load('p3.png').convert_alpha()
   p4 = pygame.image.load('p4.png').convert_alpha()

   b1 = pygame.image.load('b1.png').convert_alpha()
   b2 = pygame.image.load('b2.png').convert_alpha()
   b3 = pygame.image.load('b3.png').convert_alpha()
   b4 = pygame.image.load('b4.png').convert_alpha()

   s1 = pygame.image.load('s1.png').convert_alpha()
   s2 = pygame.image.load('s2.png').convert_alpha()
   s3 = pygame.image.load('s3.png').convert_alpha()
   s4 = pygame.image.load('s4.png').convert_alpha()
   s5 = pygame.image.load('s5.png').convert_alpha()
   s6 = pygame.image.load('s6.png').convert_alpha()
   s7 = pygame.image.load('s7.png').convert_alpha()
   s8 = pygame.image.load('s8.png').convert_alpha()
   s9 = pygame.image.load('s9.png').convert_alpha()
   s10 = pygame.image.load('s10.png').convert_alpha()

   myfont = pygame.font.SysFont("monospace", 40)
   p = myfont.render("Number of Players:", 1, (255,255,255))
   b = myfont.render("Number of Balls:", 1, (255,255,255))
   s = myfont.render("Ball Speed:", 1, (255,255,255))

   screen.blit(p, (40, 100))
   screen.blit(p1, (160, 150))
   screen.blit(p2, (210, 150))
   screen.blit(p3, (260, 150))
   screen.blit(p4, (310, 150))

   screen.blit(b, (60, 210))
   screen.blit(b1, (160, 260))
   screen.blit(b2, (210, 260))
   screen.blit(b3, (260, 260))
   screen.blit(b4, (310, 260))

   screen.blit(s, (125, 320))
   screen.blit(s1, (5, 370))
   screen.blit(s2, (55, 370))
   screen.blit(s3, (105, 370))
   screen.blit(s4, (155, 370))
   screen.blit(s5, (205, 370))
   screen.blit(s6, (255, 370))
   screen.blit(s7, (305, 370))
   screen.blit(s8, (355, 370))
   screen.blit(s9, (405, 370))
   screen.blit(s10, (455, 370))

   pygame.display.flip()

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.MOUSEBUTTONDOWN or e.type == EVENT_CHANGE_STATE:
         if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = tuple(e.pos)
            if x >= 0 and x <= 175 and y >= 0 and y <= 40:
               state = 3
            elif y >= 150 and y <= 190:
               if x >= 160 and x <= 200:
                  input_list[0] = 1
               elif x >= 210 and x <= 250:
                  input_list[0] = 2
               elif x >= 260 and x <= 300:
                  input_list[0] = 3
               elif x >= 310 and x <= 350:
                  input_list[0] = 4
            elif y >= 260 and y <= 300:
               if x >= 160 and x <= 200:
                  input_list[1] = 1
               elif x >= 210 and x <= 250:
                  input_list[1] = 2
               elif x >= 260 and x <= 300:
                  input_list[1] = 3
               elif x >= 310 and x <= 350:
                  input_list[1] = 4
            elif y >= 370 and y <= 410:
               if x >= 5 and x <= 45:
                  input_list[2] = 3
               elif x >= 55 and x <= 95:
                  input_list[2] = 4
               elif x >= 105 and x <= 145:
                  input_list[2] = 5
               elif x >= 155 and x <= 195:
                  input_list[2] = 6
               elif x >= 205 and x <= 245:
                  input_list[2] = 7
               elif x >= 255 and x <= 295:
                  input_list[2] = 8
               elif x >= 305 and x <= 345:
                  input_list[2] = 9
               elif x >= 355 and x <= 395:
                  input_list[2] = 10
               elif x >= 405 and x <= 455:
                  input_list[2] = 11
               elif x >= 455 and x <= 495:
                  input_list[2] = 12
            else:
               state = 0
         if state == 0:
            rect_list, state = menu.update(e, state)
         elif state == 3:
            print 'Start Game!'
            state = 0
            return [3, input_list]
         else:
            print 'Quit!'
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      # Update the screen
      pygame.display.update(rect_list)
