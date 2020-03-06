#Global Variables
###########################################

player1_score = 0
player2_score = 0

##########################################################################
# preperation to main code block

def change_board(board: list, col: int, player_chip: int): #target = number (ex: 1 or 2)
    #Updating Board
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
        #Detection / Player Score Increase
        for column_num in range(1, 7):
            column = extract_column(column_num, board)
            isscoredCol = check_match_of_column(column, player_chip)
            print(player1_score)
            if isscoredCol == True:
                if player_chip == 1:
                    increase_player1_score()
                elif player_chip == 2:
                    increase_player2_score()
        for row_num in range(1, 6):
            isscoredRow = check_match_of_column(board[row_num], player_chip)
        print (f"Row number is {row_num}")
            if isscoredRow == True:
                if player_chip == 1:
                    increase_player1_score()
                elif player_chip == 2:
                    increase_player2_score()

    return chipin #returns if the chip was placed
#We can change the 2 functions into just the lines of code into the changeboard function
def increase_player1_score():
    global player1_score
    player1_score = player1_score + 1

def increase_player2_score():
    global player2_score
    player2_score += 1

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

  print("Column: " + str(column_number))
  #print (column)
  for item in column:
      print("[" + str(item) +"]")


  #check_match_of_column(2, 1)
  return column

#checks if there are four of the same number in a row
def check_match_of_column(column: list, chip_value: int):
    ctr = 0
    for item in column:
        if item == chip_value:
            ctr = ctr + 1
            print (f"Counter is {ctr}")
            if ctr == 4:
                return True # point
        else:
            ctr = 0
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
