#Global Variables
###########################################
player1_score = 0
player2_score = 0
player1_name = ""
player2_name = ""
###########################################
# functions for the board - begin block
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
            award_point(isScoredCol, player_chip)

        for row_num in range(1, 6): #1 to 6 Rows
            isScoredRow = check_match_of_column(board[row_num], player_chip)
            award_point(isScoredRow, player_chip)

        middle_dia = extract_dia_special(board, 6, 0)
        isScoredDia = check_match_of_column(middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        low_middle_dia = extract_dia_special(board, 6, -1)
        isScoredDia = check_match_of_column(low_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        high_middle_dia = extract_dia_special(board, 6, 1)
        isScoredDia = check_match_of_column(high_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        higher_middle_dia = extract_dia_special(board, 5, 2)
        isScoredDia = check_match_of_column(higher_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        highest_middle_dia = extract_dia_special(board, 4, 3)
        isScoredDia = check_match_of_column(highest_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
        lowest_middle_dia = extract_dia_special(board, 6, -2)
        isScoredDia = check_match_of_column(lowest_middle_dia, player_chip)
        award_point(isScoredDia, player_chip)
    return chipin #returns if the chip was placed
#We can change the 2 functions into just the lines of code into the changeboard function
def print_board(board):
    global player1_name
    global player2_name
    print("\n")
    for row_ctr in range(0, 6):
        row_list = board[row_ctr]
        print("[", end = " ")
        for col_ctr in range(0, 7):
            print(row_list[col_ctr], end = ", ")
        print("]")

def newBoard(board, col, playerChipNumber):
    boardUpdated = change_board(board, col, playerChipNumber)
    return boardUpdated

def setup_board():
    board = []
    for x in range(6):
      board.append([0] * 7)
    return board

###########################################
# functions for the board - end block
###########################################

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
    column.append(chip)
  return column

#checks if there are four of the same number in a row
def check_match_of_column(column: list, chip_value: int):
    ctr = 0
    for item in column:
        if item == chip_value:
            ctr = ctr + 1
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

def extract_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(limit):
        diagonal.append(board[chip][chip])
    return diagonal

def extract_dia_special(board, limit, increment):
    diagonal = []
    chip = 0
    for chip in range(1, limit):
        diagonal.append(board[chip][chip + increment])
    return diagonal

def extract_lowmid_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(1, limit):
        diagonal.append(board[chip][chip - 1])
    return diagonal

def extract_highmid_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        #print(str(chip) + ", " + str(chip + 1))
        diagonal.append(board[chip][chip + 1])
    return diagonal

def extract_highermid_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        diagonal.append(board[chip][chip + 2])
    return diagonal

def extract_highestmid_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(0, limit):
        diagonal.append(board[chip][chip + 3])
    return diagonal

def extract_lowestmid_dia(board, limit): #Not needed
    diagonal = []
    chip = 0
    for chip in range(2, limit):
        diagonal.append(board[chip][chip - 2])
    return diagonal

##########################################################################
# main program block
##########################################################################

board = setup_board()


print_board(board)

print("""Welcome to connectfour.py, made by AW and MK.

In order to play the game, you will input numbers from 1-7 to represent the columns of the Connect Four board.

Player 1 will be named your name, but be represented by a 1. Same with Player 2.

Hope you enjoy playing connectfour.py,
AW and MK""")

print("\n")
player1_name = input("Player 1, what is your name: ")
player2_name = input("Player 2, what is your name: ")

#use function IsBoardFull in the while condition instead of 1 == 1

while 1 == 1:
    print("\n")

    print (f"{player1_name}'s turn")

    print ("________________________\n")


    chipin = False
    while chipin == False:
        col = -1
        while col < 1 or col > 7:
            try:
                col = int(input(f"{player1_name}: Type the column number you would like to place your chip in: "))
                if col < 1 or col > 7:
                    print (f"{player1_name}: Please enter a number between 1 and 7")
            except:
                exit_input = input("Would you like to exit? [Y/N]")
                if exit_input == "y" or exit_input == "Y":
                    exit("Thank you for playing connectfour.py!")

        col = col - 1 #Changes the index to become more user friendly
        chipin = newBoard(board, col, 1)
        if chipin == False:
            print (f"{player1_name}: Please pick a different column. This column is full")
        else:
            break


    print_board(board)

    if player1_score > 0:
        print(f"{player1_name} wins!")
        another_game = input("Would you like to play another game? [Y/N]: ")
        if another_game == "N" or another_game == "n":
            exit(f"Congratulations {player1_name}! Thank you for playing connectfour.py")
        else:
            player1_score = 0
            board = setup_board()

    print ("\n")

    print (f"{player2_name}'s turn")

    print ("________________________\n")

    chipin = False
    while not chipin:
        col = -1
        while col < 1 or col > 7:
            try:
                col = int(input(f"{player2_name}: Type the column number you would like to place your chip in: "))
                if col < 1 or col > 7:
                    print (f"{player2_name}: Please enter a number between 1 and 7")

            # Someone types exit
            except:
                exit_input = input("Would you like to exit? [Y/N]")
                if exit_input == "y" or exit_input == "Y":
                    exit("Thank you for playing connectfour.py!")
            # Break out of everything and end the program
        col = col - 1 #Changes the index to become more user friendly
        chipin = newBoard(board, col, 2)
        if chipin == False:
            print (f"{player2_name}: Please pick a different column. This column is full")
        else:
            break


    print_board(board)

    if player2_score > 0:
        print(f"{player2_name} wins!")
        another_game = input("Would you like to play another game? [Y/N]: ")
        if another_game == "N" or another_game == "n":
            exit(f"Congratulations {player2_name}! Thank you for playing connectfour.py")
        else:
            player2_score = 0
            board = setup_board()
