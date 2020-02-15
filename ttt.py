def row(size):
#	row = []
#	for i in range(size):
#		row.append(0)
#	return row
	return [0 for i in range(size)]

def initializeBoard(size):
	return [row(size) for i in range(size)]

# this is used by map() in printBoard, to turn numbers 0, 1, 2
# into human readable characters
#
def makePretty(n):
	letters = [' ', 'X', 'O']
	return letters[n]

# this function prints the board
#
def printBoard(board):
	size = len(board)
	# rows = [' | '.join(map(makePretty, row)) for row in board]
	# chubster = "\n" + ("---" *size) + "-\n"
	# output = chubster.join(rows)
	# print(output)

	for i in range(len(board)):
		# turn all the numbers of this row into characters
		letters = map(makePretty, board[i])
		print(' | '.join(letters))
		# print horizontal divider lines after each row, except the last
		if (i < size -1):
			print("---" *size + "-")
		else:
			print("")

size = 3
board = initializeBoard(size)
# board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

def player1():
	print("Player 1 ready.")
	horizontal = int(input("Pick a row 1, 2 or 3: ")) - 1
	if horizontal != 1 or horizontal != 2 or horizontal != 3:
		horizontal = int(input("Please try again and pick a row 1, 2 or 3: ")) -1
	vertical = int(input("Pick a column 1, 2, 3: ")) -1
	if vertical != 1 or vertical != 2 or vertical != 3:
		vertical = int(input("Please try again and pick a row 1, 2 or 3: ")) -1
	board [horizontal] [vertical] = 1
	printBoard(board)

def player2():
	print("Player 2 ready.")
	horizontal = int(input("Pick a row 1, 2 or 3: ")) - 1
	if horizontal != 1 or horizontal != 2 or horizontal != 3:
		horizontal = int(input("Please try again and pick a row 1, 2 or 3: ")) -1
	vertical = int(input("Pick a column 1, 2, 3: ")) -1
	if vertical != 1 or vertical != 2 or vertical != 3:
		vertical = int(input("Please try again and pick a row 1, 2 or 3: ")) -1
	board [horizontal] [vertical] = 2
	printBoard(board)

def game_won():
	#horizontal
	for row in board:
		if row.count(row[0]) == len(row) and row[0] !=0:
			return(row[0])
#vertical
	for col in range(len(board[0])):
		check = []
	for row in board:
		check.append(row[col])
	if check.count(check[0])== len(check) and check[0] !=0:
		return(row[0])
#diaganol
	diags = []
	diagsr = []
	for ix in range(len(board)):
		diags.append(board[ix][ix])
		if diags.count(diags[0]) == len(diags) and diags[0] !=0:
			return(row[0])
	cols = reversed(range(len(board)))
	rows = range(len(board))
	for col, row in zip(cols, rows):
		diagsr.append(board[row][col])
		if diagsr.count(diagsr[0]) == len(diagsr) and diagsr[0] !=0:
			return(row[0])
	return(False)

play = True

printBoard(board)

while play:
#	game = need to reset the game to 0. It can be done by just having a blank physical printBoard
	# play = game_won() == False
	player1()
	if game_won() != 1:
		player2()
		if game_won() == 2:
			play = False
			print ("The winner is: 2")
	else:
		play=False
		print ("The winner is: 1")
