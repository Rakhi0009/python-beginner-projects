
# Function to print the current state of the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("_"*5)

# Function to handle single turn for a player
def play_turn(player, board):
    while True:
        position = int(input(f"player {player} Please enter a number between 1-9 = ")) - 1
        if 0 <= position <= 8:
            break
        else:
            print("Invalid move. Please enter a number between 1-9")
            
    row = position//3
    column = position%3
    board[row][column] = player
    print_board(board)

# Function to check if current player has won
def check_if_win(player, board):
    if any([all(cell == player for cell in row) for row in board]):
        return True
    if any([all(board[row][col] == player for col in range(0,3)) for row in range(0,3)]):
        return True
    if all([board[i][i] == player for i in range(0,3)]):
        return True
    if all([board[i][2-i] == player for i in range(0,3)]):
        return True
    return False

# Main game loop
def play_tic_tac_toe():
    board = [[" " for j in range(0,3)] for i in range(0,3)]
    players = ["X", "0"]
    turn = 0

    while turn < 9:
        player = players[turn%2]
        play_turn(player,board)
        if check_if_win(player, board):
            print(f"Congratulations player {player}!! you are a winner.")
            return
        turn +=1
    print(f"Well played, both players! It's a draw — no losers this time!")
    return

# Entry point: this block runs only when the script is executed directly
if __name__ == "__main__":
    play_tic_tac_toe()



