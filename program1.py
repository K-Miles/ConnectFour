##########################################################################
# preperation to main code block
##########################################################################
##########################################################################
 ##if row < 0:
   ##print("That column is full. Please choose another column")
   ##print("\n")
   ##col = int(raw_input("Type the column number you would like to place your chip in: "))
   ##change_board(board, col)
##########################################################################

def change_board(board: list, col: int, player_chip: int): #target = number (ex: 1 or 2)
    row_default = 5
    chipin = False
    while row_default >= 0:
        currentRow = board[row_default]
        if currentRow[col] == 0:
            currentRow[col] = player_chip
            chipin = True
            break
        else:
            row_default = row_default - 1
    return chipin #returns if the chip was placed

def print_board(board):
    for r in enumerate(board):
        print (r)

def player1(board, col):
  #turn = turn + 1
  chipin = change_board(board, col, 1)
  return chipin

def player2(board, col):
  #turn = turn + 1
    chipin = change_board(board, col, 2)
    return chipin

def IsBoardFull(board):

#use loop to check if each column is full

##########################################################################
# main program block
##########################################################################

board = []

for x in range(6):
  board.append([0] * 7) #7 are the columns, 6 are the rows

#new code is under here

num = 0
target = 0

print_board(board)

#use function IsBoardFull in the while condition instead of 1 == 1

while 1 == 1:
    print("\n")

    print ("Player One's turn")

    print ("________________________\n")


    chipin = False
    while chipin == False:
        col = -1
        while col < 0 or col > 6:
            col = int(input("Player One: Type the column number you would like to place your chip in: "))
            if col < 0 or col > 6:
                print ("Player One: Please enter a number between 0 and 6")
        chipin = player1(board, col)
        if chipin == False:
            print ("Player One: Please pick a different column. This column is full")
        else:
            break

    print ("Player One:" + str(chipin))

    print_board(board)

    print ("\n")

    print ("Player Two's turn")

    print ("________________________\n")

    chipin = False
    while chipin == False:
        col = -1
        while col < 0 and col > 6:
            col = int(input("Player Two: Type the column number you would like to place your chip in: "))
            if col < 0 or col > 6:
                print ("\n")
                break
        chipin = player2(board, col)
        if chipin == False:
            print ("Player Two: Please pick a different column. This column is full")
        else:
            break

    print ("Player Two: " + str(chipin))

    print_board(board)

##########################################################################
# change_board function with turn functionality
##########################################################################

# def change_board(board: list, col: int): #target = number (ex: 1 or 2)
#     turn = 0
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
#             turn = turn + 1
#         if turn !% 2:
#         target = target + 2
#         turn = turn + 1
#         currentRow[col] = target
#         else:
#             target = target + 1
#             currentRow[col] = target
#     return board #updated board
