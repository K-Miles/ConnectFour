from random import randint

board = []


for x in range(6):
  board.append([0] * 7) #7 are the collumns, 6 are the rows


def print_board(board):
 r = 0
 for row in board:
  c = 0
  for cell in row:
     print str(r) + " " + str(c)
     print board[r][c]
     c = c + 1
  r=r+1

print "The original board is: \n"


for row in enumerate(board):
    print row
print('________________________________________\n')
#assigning variable of target, first number is row (starting from top) then column next
target = board[1][3]
print("Target is \n")
target = target + 1
#Inserts a number into the board using the coordinates 1, 3
board[1][3] = target
print target

print('________________________________________\n')

print("Changed board is \n")
for row in enumerate(board):
    print row
#new code is under here
num = 0
row = 5

col = int(raw_input("Type the column number you would like to place your chip in: "))

def change_board(board, row, col):
	target = board[row][col]
	if target == 0:
		target = target + 1
	 	board[row][col] = target
	if target == 1:
		row = row - 1
		change_board(board, row, col)
        if row < 0:
            print"That column is full. Please choose another column"
            print"\n"
            col = int(raw_input("Type the column number you would like to place your chip in: "))
            change_board(board, row, col)

print board

print"\n"

print"Player one's turn"

print "________________________\n"

col = int(raw_input("Type the column number you would like to place your chip in: "))

def player1(num):
	num = col
	if num < 7:
		change_board(board, row, col)
		target = target + 1
	else:
            print "The column number must be 0, 1, 2, 3, 4, 5, or 6. Please try again"
        print "\n"
        col = int(raw_input("Type the column number you would like to place your chip in: "))
        player1(num)

player1(num)

print board

print "\n"

print "Player two's turn"

print "________________________\n"

col = int(raw_input("Type the column number you would like to place your chip in: "))

def player2(num):
    num = col
    if num < 7:
        change_board(board, row)
        target = target - 2
    else:
        print "The column number must be 0, 1, 2, 3, 4, 5, or 6. Please try again"
        print "\n"
        col = int(raw_input("Type the column number you would like to place your chip in: "))
        player2(num)

player2(num)
#insert_chip(col_num)
#Highest number row we can drop it into
#check if there is a 1 or 2
#for loop to go through list
#only write in the selected column



#print board[0]
#print_board(board)
# def random_row(board):
#   return randint(0, len(board) - 1)
#
# def random_col(board):
#   return randint(0, len(board[0]) - 1)

# ship_row = random_row(board)
# ship_col = random_col(board)
# #print ship_row
# #print ship_col
#
# # Everything from here on should go in your for loop!
# # Be sure to indent four spaces!for turn in range(x):
# for turn in range(4):
#   print "Turn", turn + 1
#   guess_row = int(raw_input("Guess Row: "))
#   guess_col = int(raw_input("Guess Col: "))
#
#   if guess_row == ship_row and guess_col == ship_col:
#     print "Congratulations! You sunk my battleship!"
#     break
#   else:
#     if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col >   4):
#       print "Oops, that's not even in the ocean."
#     elif(board[guess_row][guess_col] == "X"):
#       print "You guessed that one already."
#     else:
#       print "You missed my battleship!"
#       board[guess_row][guess_col] = "X"
#     print_board(board)
#     if turn == 3:
#       print "Game Over"
#      Print (turn + 1) here!
#
