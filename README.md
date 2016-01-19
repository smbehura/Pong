# Pong
4-person pong

"""
Overview:
•	up to 4 players
•	up to 3 balls
•	ball speed determined by user
•	multiplayer game is played in knockout rounds

Components:
•	Ball Class: represents the floating ball and keeps a record of its location and color
  	move(): moves ball in the correct direction
  	changeColor(): changes color of ball based on which color paddle hit it last
  	isOffBoard(): checks if ball is on or off the pong board
•	Player Class: represents player who has a paddle and a win/neutral/loss state
  	loss(): sets state variable to loss
  	neutral(): sets state variable to neutral
  	win(): sets state variable to win
  	getState(): returns state of Player
•	Paddle Class: represents each player’s paddle and keeps a record of paddle’s location and color; also contains variable representing   orientation of paddle (top, bottom, right, and left) 
  	move(): moves paddle based on user input keys and orientation of paddle
  	isPaddleofPlayer(player): returns True if paddle belongs to player and False if not
•	Pong Board Class: represents full Pong Board containing paddles, ball and state of game and also contains information like how many   players
  	setNumPlay(num): sets number of players in game
  	changeToLoss(player): sets player’s state variable to loss
  	checkForWin(): loops through all players and checks state variable of each player; if all players except one have a state of loss     than the one neutral player’s state is changed to win 

User Interface:
•	Player 1 (right): up/down keys
•	Player 2 (bottom): C/V keys
•	Player 3 (top): </> keys
•	Player 4 (left): Q/A keys
Once a player misses the ball, the player’s paddle will disappear and the game will turn into a 3 player game. The side that the paddle disappears from will just end up being a wall that the ball will bounce off of. 

Flow Control:
When the game first starts, a text box will appear where one of the players can choose the speed of the ball by inputting a number between 1 to 10. After inputting a number, the user will also be prompted to choose between having 1 to 3 balls. After the user has decided these two values, the game will begin. A white ball will begin to bounce around the screen, and each player’s paddle will be a different color. The ball will take on the color of whatever paddle it hits, and a player will lose if they fail to hit the ball. 

Work Distribution:
•	Graphics: Candace Okumko
  o	Classes: Pong Board
•	Game Functionality
  o	Ball Movement: Patrick Shin
    	Classes: Ball
  o	User Input: Catherine Yao
    	Classes: Paddle, Player
  o	Game Rules/Mechanics: Soma Mitra-Behura
    	Classes: Pong Board, Player

Checkpoint/MVP
By the checkpoint meeting, we hope to have finished the very basics of the game (i.e. interpreting user input, coding the physics of the pong ball, etc). Depending on how far we get, it is also possible for us to have a very basic GUI for us to use in testing the methods necessary to playing the game. The minimum requirements are the user input functionality, a basic GUI, and the physics which is why we have chosen to address these and have them completed by the checkpoint meeting.
"""


