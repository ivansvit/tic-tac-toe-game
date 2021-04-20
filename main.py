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

# Player move function
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
        return False
    elif board['4'] == board['5'] == board['6'] != ' ':
        return False
    elif board['7'] == board['8'] == board['9'] != ' ':
        return False
    elif board['1'] == board['4'] == board['7'] != ' ':
        return False
    elif board['2'] == board['5'] == board['8'] != ' ':
        return False
    elif board['3'] == board['6'] == board['9'] != ' ':
        return False
    elif board['1'] == board['5'] == board['9'] != ' ':
        return False
    elif board['3'] == board['5'] == board['7'] != ' ':
        return False
    else:
        return True


# Game function. Player input and mark the board.
def game(board):
    step = 0
    player_one_name = input("Player 1, please enter your name. ")
    player_two_name = input("Player 2, please enter your name. ")
    game_field(board)
    while check_winner(board):

        # Draw statement
        if step == 4:
            print("Draw!")
            break

        # Player 1
        player_one_letter = 'X'
        player_one_input = input(f"{player_one_name}, choose a block to mark. "
                                 f"Enter a number of block from 1 to 9.\nTop-left block - 1, bottom-right - 9\n")
        player_move(board, player_one_input, player_one_letter)
        if not check_winner(board):
            print(f"{player_one_name} you win!!!")

        # Player 2
        if check_winner(board):
            player_two_letter = 'O'
            player_two_input = input(f"{player_two_name}, choose a block to mark. "
                                     f"Enter a number of block from 1 to 9.\nTop-left block - 1, bottom-right - 9\n")
            player_move(board, player_two_input, player_two_letter)
            if not check_winner(board):
                print(f"{player_two_name} you win!!!")

        step += 1


# Play again function
def restart_game():
    player_answer = input("Do you want to play again? Enter Y/N. ").upper()
    if player_answer == 'Y':
        for key in ticTacToeBoard:
            ticTacToeBoard[key] = ' '
        game(ticTacToeBoard)
        restart_game()
    else:
        print("See you later!")


game(ticTacToeBoard)
restart_game()

# Draw statement of the game
# Add players name input
# Play again function