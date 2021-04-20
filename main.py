# Declare Tic Tac Toe board dictionary
ticTacToeBoard = {'1': ' ', '2': ' ', '3': ' ',
                  '4': ' ', '5': ' ', '6': ' ',
                  '7': ' ', '8': ' ', '9': ' ',
                  }


# Create a field game board
def game_field(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print('-----------')
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print('-----------')
    print(f" {board['7']} | {board['8']} | {board['9']} ")


def player_move(board, user_input, player_letter):
    if board[user_input] == ' ':
        board[user_input] = player_letter
        game_field(board)
    else:
        print("Try another block.")
        game(board)


# Game logic
def check_winner(board):
    if board['1'] == board['2'] == board['3'] != ' ':
        print(f"{board['1']}, You win!!!")
        return False
    elif board['4'] == board['5'] == board['6'] != ' ':
        print(f"{board['4']}, You win!!!")
        return False
    elif board['7'] == board['8'] == board['9'] != ' ':
        print(f"{board['7']}, You win!!!")
        return False
    elif board['1'] == board['4'] == board['7'] != ' ':
        print(f"{board['1']}, You win!!!")
        return False
    elif board['2'] == board['5'] == board['8'] != ' ':
        print(f"{board['2']}, You win!!!")
        return False
    elif board['3'] == board['6'] == board['9'] != ' ':
        print(f"{board['3']}, You win!!!")
        return False
    elif board['1'] == board['5'] == board['9'] != ' ':
        print(f"{board['1']}, You win!!!")
        return False
    elif board['3'] == board['5'] == board['7'] != ' ':
        print(f"{board['3']}, You win!!!")
        return False
    else:
        return True


# Player input and mark the board
def game(board):

    game_field(board)
    while check_winner(board):

        # Player 1
        player_one_letter = 'X'
        player_one_input = input(f"Player {player_one_letter}, choose a block to mark. "
                                 f"Enter a number of block from 1 to 9.\nTop-left block - 1, bottom-right - 9\n")
        player_move(board, player_one_input, player_one_letter)

        if check_winner(board):
            # Player 2
            player_two_letter = 'O'
            player_two_input = input(f"Player {player_two_letter}, choose a block to mark. "
                                     f"Enter a number of block from 1 to 9.\nTop-left block - 1, bottom-right - 9\n")
            player_move(board, player_two_input, player_two_letter)


game(ticTacToeBoard)

# TODO Draw statement of the game
# TODO Player X Winner double printing!