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
#insert_chip(col_num)
#Highest # row we can drop it into
#check if there is a 1 or 2
#for loop to go through list
#only write in selected column
