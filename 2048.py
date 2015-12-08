#	Andrew Repp
#	2048 Game
#	Unix - Project 3
#	12/9/15

import random

state = 0
user = ""
end_num = 64
difficulty = "easy"
messageDisplayed = False
score = 0
boardSize = 4 # 4 x 4 board
gameBoard = [[0 for x in range(boardSize)] for x in range(boardSize)]
endMessage = ""

def initializeBoard():
	addNum()
	addNum()

def addNum():
	num = random.randint(0, 1)
	emptySpotFound = False
	row = random.randint(0, boardSize - 1)
	if (num == 1):
		num = 4
	else:
		num = 2
	col = random.randint(0, boardSize - 1)
	
	if boardFull() == False:
		while (emptySpotFound == False):
			if (gameBoard[row][col] == 0):
				gameBoard[row][col] = num
				emptySpotFound = True
			else:
				row = random.randint(0, boardSize - 1)
				num2 = random.randint(0, boardSize - 1)
				col = random.randint(0, boardSize - 1)
				
def checkForEnd():
	noMoves = True
	if (boardFull() == True):
		for row in range (0, boardSize):
			for col in range (0, boardSize):
				if (gameBoard[row][col] == gameBoard[row+1][col]):
					noMoves = False
				if (gameBoard[row][col] == gameBoard[row][col+1]):
					noMoves = False
		return noMoves
	else:	
		return False

def getWinStatus():
	global endMessage
	win = False
	for row in range (0, boardSize):
		for col in range (0, boardSize):
			if (gameBoard[row][col] == end_num):
				win = True
	if win == True:
		endMessage = "Congratulations, you win!"
	else:
		endMessage = "Sorry, no more moves are available. Try again!"
	return win

def boardFull():
	foundEmpty = False
	for list in gameBoard:
		for x in list:
			if x == 0:
				return False
				foundEmpty = True
	if foundEmpty == False:
		return True

def processInput():
	successful = False
	if ((user == "w") or (user == "W") or (user == "^[[A")): # Up
		#print "Up"
		successful = shiftUp()
		if (successful == True):
			addNum()
	elif ((user == "a") or (user == "A") or (user == "^[[D")): # Left
		#print "Left"
		successful = shiftLeft()
		if (successful == True):
			addNum()
	elif ((user == "s") or (user == "S") or (user == "^[[B")): # Down
		#print "Down"
		successful = shiftDown()
		if (successful == True):
			addNum()
	elif ((user == "d") or (user == "D") or (user == "^[[C")): # Right
		#print "Right"
		successful = shiftRight()
		if (successful == True):
			addNum()
	elif (user == "q"):
		print "Exiting..."
	else:
		print "Error: input not recognized. Please enter W, A, S, or D or q to quit."

def shiftUp():
	global score
	col = 0
	tileMoved = False
	for col in range(0, boardSize):
		topMerged = False
		midMerged = False
		botMerged = False
		i = 0
		for i in range(0, boardSize - 1):
			row = 1
			for row in range(1, boardSize):
				if (gameBoard[row-1][col] == 0):
					gameBoard[row-1][col] = gameBoard[row][col]
					if (gameBoard[row][col] != 0):
						tileMoved = True
						gameBoard[row][col] = 0
				elif (gameBoard[row-1][col] == gameBoard[row][col]):
					if (row == 1):
						if (not topMerged and not midMerged):
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							score = score + gameBoard[row-1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
					elif (row == 2):
						if (not midMerged and not botMerged):
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							score = score + gameBoard[row-1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif (row == 3):
						if (not botMerged):		
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							score = score + gameBoard[row-1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
	return tileMoved

def shiftLeft():
	global score
	row = 0
	tileMoved = False
	for row in range(0, boardSize):
		leftMerged = False
		midMerged = False
		rightMerged = False
		i = 0
		for i in range(0, boardSize - 1):
			col = 1
			for col in range(1, boardSize):
				if (gameBoard[row][col-1] == 0):
					gameBoard[row][col-1] = gameBoard[row][col]
					if (gameBoard[row][col] != 0):
						tileMoved = True
						gameBoard[row][col] = 0
				elif (gameBoard[row][col-1] == gameBoard[row][col]):
					if (col == 1):
						if (not leftMerged and not midMerged):
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							score = score + gameBoard[row][col-1]
							gameBoard[row][col] = 0
							tileMoved = True
							leftMerged = True
					elif (col == 2):
						if (not midMerged and not rightMerged):
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							score = score + gameBoard[row][col-1]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif (col == 3):
						if (not rightMerged):		
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							score = score + gameBoard[row][col-1]
							gameBoard[row][col] = 0
							tileMoved = True
							rightMerged = True
	return tileMoved

def shiftDown():
	global score
	col = 0
	tileMoved = False
	for col in range(0, boardSize):
		topMerged = False
		midMerged = False
		botMerged = False
		i = 0
		for i in range(0, boardSize - 1):
			row = 2
			for row in range(2, -1, -1):
				if (gameBoard[row+1][col] == 0):
					gameBoard[row+1][col] = gameBoard[row][col]
					if (gameBoard[row][col] != 0):
						tileMoved = True
						gameBoard[row][col] = 0
				elif (gameBoard[row+1][col] == gameBoard[row][col]):
					if (row == 2):
						if (not botMerged and not midMerged):
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							score = score + gameBoard[row+1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							botMerged = True
					elif (row == 1):
						if (not midMerged and not topMerged):
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							score = score + gameBoard[row+1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif (row == 0):
						if (not topMerged):		
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							score = score + gameBoard[row+1][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
	return tileMoved

def shiftRight():
	global score
	row = 0
	tileMoved = False
	for row in range(0, boardSize):
		leftMerged = False
		midMerged = False
		rightMerged = False
		i = 0
		for i in range(0, boardSize - 1):
			col = 2
			for col in range(2, -1, -1):
				if (gameBoard[row][col+1] == 0):
					gameBoard[row][col+1] = gameBoard[row][col]
					if (gameBoard[row][col] != 0):
						tileMoved = True
						gameBoard[row][col] = 0
				elif (gameBoard[row][col+1] == gameBoard[row][col]):
					if (col == 2):
						if (not rightMerged and not midMerged):
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							score = score + gameBoard[row][col+1]
							gameBoard[row][col] = 0
							tileMoved = True
							rightMerged = True
					elif (col == 1):
						if (not midMerged and not leftMerged):
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							score = score + gameBoard[row][col+1]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif (col == 0):
						if (not leftMerged):		
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							score = score + gameBoard[row][col+1]
							gameBoard[row][col] = 0
							tileMoved = True
							leftMerged = True
	return tileMoved




def printBoard():
	print "\nScore: " + str(score) + "\tPlaying until: " + str(end_num) + "\n"
	print "-----------------"
	for list in gameBoard:
		for x in list:
			print "| " + str(x),
		print "|"
		print "-----------------"
	
while (user != "q"):
	if state == 0: #Main menu state
		print "\nWelcome to 2048!"
		print "\nMenu\n---------------"
		print "    (1) Play Game"
		print "    (2) Instructions"
		print "    (3) Options"
		print "    (4) Quit"
		
		user = raw_input('')
		if (user == "1"):
			state = 1
		elif (user == "2"):
			state = 2
		elif (user == "3"):
			state = 3
		elif (user == "4"):
			state = 4
		elif (user == "q"):
			state = 4
		else:
			print "Invalid input. Please enter either 1, 2, 3, or 4 or q to quit."

	elif state == 1: #Play Game state
		if messageDisplayed == False:
			print "\nUse W, A, S, and D to move the tiles up, left, down, and right\n"		
			initializeBoard()
			score = 0
			messageDisplayed = True
		if (getWinStatus() == False and checkForEnd() == False):
			printBoard()
			user = raw_input('')
			processInput()
		else:
			printBoard()
			print endMessage
			print "Score: " + str(score)
			user = "q"
		
	elif state == 2: #Instructions state
		print "\nInstructions:"
		print "    Use the W, A, S, and D keys to shift the tiles up,"
		print "    down, left, and right.  Adjacent tiles with the"
		print "    same value into each other will create a new tile"
		print "    equal to the sum of the two that merged.  The game"
		print "    ends when the user creates a tile with the goal "
		print "    value or when there are no moves left.\n"
		print " (1) Back to Menu"

		user = raw_input('')
		if (user == "1"):
			state = 0
		else:
			print "Error: invalid input. Enter 1 to go to the menu or q to quit."

	elif state == 3: #Options state
		print "\nOptions"
		print "    (1) Change difficulty (currently set to  " + difficulty + " (" + str(end_num) + "))"
		print "    (2) Back to Menu "

		user = raw_input('')
		if (user == "1"):
			state = 5
		elif (user == "2"):
			state = 0
		else:
			print "Error: invalid input. Enter 1 to change difficulty, 2 to go to the main menu, or q to quit."
	elif state == 4: #Quit
		user = "q"
	elif state == 5: #Change difficulty
		print "\nChange difficulty"
		print "    Current diffiulty level: " + difficulty
		print "    (1) Easy (64)"
		print "    (2) Medium (512)"
		print "    (3) Hard (2048)"
		print "    (4) Back to Options Menu"

		user = raw_input('')
		if (user == "1"):
			end_num = 64
			difficulty = "easy"
			print "Difficulty set to " + difficulty
			state = 3
		elif (user == "2"):
			end_num = 512
			difficulty = "medium"
			print "Difficulty set to " + difficulty
			state = 3
		elif (user == "3"):
			end_num = 2048
			difficulty = "hard"
			print "Difficulty set to " + difficulty
			state = 3
		elif (user == "4"):
			state = 3
		elif (user == "q"):
			state = 4
		else:
			print "Error: invalid input.  Please enter 1, 2, 3, 4, or q to quit."


	
