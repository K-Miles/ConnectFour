#Global Variables
###########################################
player1_score = 0
player2_score = 0
player1_name = ""
player2_name = ""
###########################################
# preperation to main code block
###########################################
def change_board(board: list, col: int, player_chip: int): #target = number (ex: 1 or 2)
    #Updating Board
    row_default = 5
    chipin = False
    clear_point(player_chip)
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
        for column_num in range(1, 7): #1 to 7 columns
            column = extract_column(column_num, board)
            isScoredCol = check_match_of_column(column, player_chip)
            print(player1_score)
            award_point(isScoredCol, player_chip)

        for row_num in range(1, 6): #1 to 6 Rows
            isScoredRow = check_match_of_column(board[row_num], player_chip)
            print (f"Row number is {row_num}")
            award_point(isScoredRow, player_chip)

        middle_dia = extract_dia(board, 6)
        isScoredDia = check_match_of_column(middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        low_middle_dia = extract_lowmid_dia(board, 6)
        isScoredDia = check_match_of_column(low_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        high_middle_dia = extract_highmid_dia(board, 6)
        isScoredDia = check_match_of_column(high_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        higher_middle_dia = extract_highermid_dia(board, 5)
        isScoredDia = check_match_of_column(higher_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        highest_middle_dia = extract_highestmid_dia(board, 4)
        isScoredDia = check_match_of_column(highest_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        lowest_middle_dia = extract_lowestmid_dia(board, 6)
        isScoredDia = check_match_of_column(lowest_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
    return chipin #returns if the chip was placed
#We can change the 2 functions into just the lines of code into the changeboard function
def print_board(board):
    global player1_name
    global player2_name
    for r in enumerate(board):
        print (r)
    print ("\n")
    print("**********Score Board**********")
    print (f"{player1_name} = " + str(player1_score))
    print (f"{player2_name} = " + str(player2_score))
    print("*******************************")

def newBoard(board, col, playerChipNumber):
    boardUpdated = change_board(board, col, playerChipNumber)
    return boardUpdated

def IsBoardFull(board):

    return False

def getColumnValues(board, col):
    #board is a 2dlist.

    column_values = board[:][column]
    return column_values

    #return 1d list of all values in the column

#takes a column, then creates a list with all the pieces from that column
def extract_column(column_number, board):
  column = []
  for row in range(len(board)):
    chip = board[row][column_number - 1] #Converts index count to regular counting
    #print(chip)
    column.append(chip)

  print("Column: " + str(column_number + 1)) #Converts index count to regular counting
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
def award_point(isScored, player_chip):
    global player1_score
    global player2_score
    if isScored == True:
        if player_chip == 1:
            player1_score += 1
        elif player_chip == 2:
            player2_score += 1

#This function is used to reset player score to award repeated score since change board function--
#scans each column and each row for every instance
def clear_point(player_chip):
    global player1_score
    global player2_score
    if player_chip == 1:
        player1_score = 0
    else:
        player2_score = 0

def extract_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(limit):
        print (str(chip) + ", " + str(chip))
        #print (board[chip][chip])
        diagonal.append(board[chip][chip])
    return diagonal

def extract_lowmid_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(1, limit):
        print(str(chip) + ", " + str(chip - 1))
        diagonal.append(board[chip][chip - 1])
    return diagonal

def extract_highmid_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        print(str(chip) + ", " + str(chip + 1))
        diagonal.append(board[chip][chip + 1])
    return diagonal

def extract_highermid_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        print(str(chip) + ", " + str(chip + 2))
        diagonal.append(board[chip][chip + 2])
    return diagonal

def extract_highestmid_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        print(str(chip) + ", " + str(chip + 3))
        diagonal.append(board[chip][chip + 3])
    return diagonal

def extract_lowestmid_dia(board, limit):
    diagonal = []
    chip = 0
    for chip in range(2, limit):
        print(str(chip) + ", " + str(chip - 2))
        diagonal.append(board[chip][chip - 2])
    return diagonal

##########################################################################
# main program block
##########################################################################

board = []

for x in range(6):
  board.append([0] * 7) #7 are the columns, 6 are the rows

print_board(board)

player1_name = input("Player 1, what is your name: ")
player2_name = input("Player 2, what is your name: ")

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
        chipin = newBoard(board, col, 1)
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
        chipin = newBoard(board, col, 2)
        if chipin == False:
            print ("Player Two: Please pick a different column. This column is full")
        else:
            break

    print ("Player Two: " + str(chipin))

    print_board(board)
