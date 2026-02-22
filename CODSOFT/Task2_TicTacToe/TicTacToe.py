board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_board_full():
    return " " not in board
print_board()
def player_move():
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1
            if board[position] == " ":
                board[position] = "X"
                break
            else:
                print("Position already taken.")
        except:
            print("Invalid input. Try again.")
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
def best_move():
    best_score = -float("inf")
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def main():
    print("Tic Tac Toe - You (X) vs AI (O)")
    
    while True:
        print_board()
        player_move()

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break
        best_move()
       

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
