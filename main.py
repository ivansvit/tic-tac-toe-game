# Declare Tic Tac Toe board dictionary
ticTacToeBoard = {'1': ' ', '2': ' ', '3': ' ',
                  '4': ' ', '5': ' ', '6': ' ',
                  '7': ' ', '8': ' ', '9': ' ',
                  }

gameOn = True


# Create a field game board
def gameField(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print('-----------')
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print('-----------')
    print(f" {board['7']} | {board['8']} | {board['9']} ")


def playerMove(board, user_input, player_letter):
    if board[user_input] == ' ':
        board[user_input] = player_letter
        gameField(board)
    else:
        print("Try another block.")
        gameStep(board)


# Player input and mark the board
def gameStep(board):
    # Player 1
    player_one_letter = 'X'
    player_one_input = input("Player 1, choose a block to mark. Enter number of place from 1 to 9.\n")
    playerMove(board, player_one_input, player_one_letter)

    # Player 2
    player_two_letter = 'O'
    player_two_input = input("Player 2, choose a block to mark. Enter number of place from 1 to 9.\n")
    playerMove(board, player_two_input, player_two_letter)


# Game logic
while gameOn:
    if ticTacToeBoard['1'] == ticTacToeBoard['2'] == ticTacToeBoard['3'] != ' ':
        print(f"{ticTacToeBoard['1']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['4'] == ticTacToeBoard['5'] == ticTacToeBoard['6'] != ' ':
        print(f"{ticTacToeBoard['4']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['7'] == ticTacToeBoard['8'] == ticTacToeBoard['9'] != ' ':
        print(f"{ticTacToeBoard['7']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['1'] == ticTacToeBoard['4'] == ticTacToeBoard['7'] != ' ':
        print(f"{ticTacToeBoard['1']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['2'] == ticTacToeBoard['5'] == ticTacToeBoard['8'] != ' ':
        print(f"{ticTacToeBoard['2']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['3'] == ticTacToeBoard['6'] == ticTacToeBoard['9'] != ' ':
        print(f"{ticTacToeBoard['3']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['1'] == ticTacToeBoard['5'] == ticTacToeBoard['9'] != ' ':
        print(f"{ticTacToeBoard['1']}, You win!!!")
        gameOn = False
    elif ticTacToeBoard['3'] == ticTacToeBoard['5'] == ticTacToeBoard['7'] != ' ':
        print(f"{ticTacToeBoard['3']}, You win!!!")
        gameOn = False

    if gameOn:
        gameStep(ticTacToeBoard)