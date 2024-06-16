def print_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")


def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("This spot is already taken.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        row, col = get_move(board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
