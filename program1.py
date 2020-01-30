from random import randint

board = []


for x in range(6):
  board.append([0] * 7) #7 are the collumns, 6 are the rows

print board

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
#insert_chip(col_num)
#Highest # row we can drop it into
#check if there is a 1 or 2
#for loop to go through list
<<<<<<< HEAD
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
#     # Print (turn + 1) here!
# #
=======
#only write in selected column
>>>>>>> 8486031f0efb4af65fcf4fb6400c07a80f976ded
