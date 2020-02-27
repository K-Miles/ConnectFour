##########################################################################
# preperation to main code block
player1_score = 0
player2_score = 0
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
    if chipin == True:
        FourInARowCol(board)
    return chipin #returns if the chip was placed

def print_board(board):
    for r in enumerate(board):
        print (r)
    print ("\n")
    print ("Player One Score = " + str(player1_score))
    print ("Player Two Score = " + str(player2_score))

def player1(board, col, player = 1):
  chipin = change_board(board, col, player)
  return chipin

def player2(board, col):
    chipin = change_board(board, col, 2)
    return chipin

def IsBoardFull(board):

    return False

#deosn't add a point to whichever player gets four in a row
def FourInARowCol(board):
    player1_score = 0
    player2_score = 0
    print("hi")
    for row in range(len(board) - 3):
        for col in range(len(board)):
            if (board[row][col] == board[row + 1][col]) and (board[row + 2][col] == board[row+3][col]) and (board[row][col] == board[row + 2][col]):
                if board[row][col] == 1:
                    print('Player 1 has scored four in a row')
                    player1_score += 1
                elif board[row][col] == 2:
                    player2_score += 1
                else:
                    pass

def FourInARowRow(board):

    return False

def FourInARowDiagonal(board):

    return False

def getColumnValues(board, col):
    #board is a 2dlist.

    column_values = board[:][column]
    return column_values

    #return 1d list of all values in the column

#new functions
#if used we need to change other parts of the code!!!!!!
#______________________________________________________________

#takes a column, then creates a list with all the pieces from that column
def extract_column(column_number, board):
  column = []
  for row in range(len(board)):
    chip = board[row][column_number - 1]
    #print(chip)
    column.append(chip)
  print("hello")
  check_match_of_column(2, 1)
  return column

#checks if there are four of the same number in a row
def check_match_of_column(extracted_column: list, chip_value: int):
    for col in range(len(column) - 3):
        if col == col + 1 and col == col + 2 and col == col + 3:
            return True
        else:
            return False

#will award point
def award_point(check_match_of_column):
    if check_match_of_column == True:
        if chip_value == 1:
            player1_score += 1
        elif chip_value == 2:
            player2_score += 1
    else:
        pass

    #Ex: [0, 1, 1, 1, 1, 0] -> True
    #Ex: [0, 1, 1, 1, 0, 0] -> False
    #Ex: [0, 0, 1, 1, 1, 1] -> True
    #Ex: [1, 1, 1, 0, 1, 1] -> False
    #Ex: [0, 0, 0, 0, 0, 0] -> False
    #Ex: [0, 0, 0, 0, 0, 0]  AND chip_value is 0 -> True
    #Returns true if four in a row, anywhere.
#use loop to check if each column is full
#______________________________________________________
##########################################################################
# main program block
##########################################################################

board = []

for x in range(6):
  board.append([0] * 7) #7 are the columns, 6 are the rows

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
    while not chipin:
        col = -1
        while col < 0 or col > 6:
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
