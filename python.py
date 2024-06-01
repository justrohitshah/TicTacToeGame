# Tic Tac Toe

# Create the Tic Tac Toe board
board = [' ' for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if any player has won
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to check if the board is full
def check_board_full():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()

        # Get the player's move
        move = int(input("Enter your move (0-8): "))

        # Validate the move
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Try again.")
            continue

        # Update the board with the player's move
        board[move] = current_player

        # Check if the current player has won
        if check_winner(current_player):
            display_board()
            print("Player", current_player, "wins!")
            game_over = True
        # Check if the board is full
        elif check_board_full():
            display_board()
            print("It's a tie!")
            game_over = True
        else:
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()