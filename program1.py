##########################################################################
# preperation to main code block
##########################################################################

#def change_board(board, row, col):
 #if target == 0
 #currentRow[col] = 1
 #if target == 1 or target == 2:
   #row = row - 1
   #change_board(board, row, col)
##########################################################################
 ##if row < 0:
   ##print"That column is full. Please choose another column"
   ##print"\n"
   ##col = int(raw_input("Type the column number you would like to place your chip in: "))
   ##change_board(board, row, col)
##########################################################################

def change_board(board: list, col: int): #target = number (ex: 1 or 2)
    row_default = 5
    target = currentRow[col]
    currentRow = board[row]
    while target == 1 or target == 2:
        row_default = row_default - 1
        #target = currentRow[col]
        if row < 0 or target == 0:
            break
    if target == 0:
        target = target + 1
        currentRow[col] = target
    return board #updated board

def player1(board, col):
  #turn = turn + 1
  if col < 7:
    change_board(board, col)
  else:
    print "The column number must be 0, 1, 2, 3, 4, 5, or 6. Please try again"
    print "\n"
    col = int(raw_input("Type the column number you would like to place your chip in: "))
    player1(board, col)

def player2(board, col):
  #turn = turn + 1
  if col < 7:
    change_board(board, col)
  else:
    print "The column number must be 0, 1, 2, 3, 4, 5, or 6. Please try again"
    print "\n"
    col = int(raw_input("Type the column number you would like to place your chip in: "))
    player2(board, col)

# def print_board(board):
#  r = 0
#  for row in board:
#   c = 0
#   for cell in row:
#      print str(r) + " " + str(c)
#      print board[r][c]
#      c = c + 1
#   r=r+1

##########################################################################
# main program block
##########################################################################
board = []

for x in range(6):
  board.append([0] * 7) #7 are the columns, 6 are the rows

#new code is under here

num = 0
target = 0

#col = int(raw_input("Type the column number you would like to place your chip in: "))

#print board
for r in enumerate(board):
    print r

print"\n"

print"Player one's turn"

print "________________________\n"

col = int(raw_input("Type the column number you would like to place your chip in: "))

player1(board, col)

for r in enumerate(board):
    print r

print "\n"

print "Player two's turn"

print "________________________\n"

col = int(raw_input("Type the column number you would like to place your chip in: "))

player2(board, col)
#insert_chip(col_num)
#Highest number row we can drop it into
#check if there is a 1 or 2
#for loop to go through list
#only write in the selected column

##########################################################################
# change_board function with turn functionality
##########################################################################

# def change_board(board: list, col: int): #target = number (ex: 1 or 2)
#     row_default = 5
#     target = currentRow[col]
#     currentRow = board[row]
#     while target == 1 or target == 2:
#         row_default = row_default - 1
#         #target = currentRow[col]
#         if row < 0 or target == 0:
#             break
#     if target == 0:
#         if turn == 0:
#             target = target + 1
#         if turn !% 2:
#         target = target + 2
#         currentRow[col] = target
#         else:
#             target = target + 1
#             currentRow[col] = target
#     return board #updated board
