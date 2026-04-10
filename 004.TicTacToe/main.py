X_WIN = "X_WIN"
O_WIN = "O_WIN"
DRAW = "DRAW"
PLAYING = "PLAYING"


X_PLAYER = "x"
O_PLAYER = "o"

board = [[" " for _ in range(3)] for _ in range(3)]


def check_game_status():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] \
                and board[i][2] != " ":
            return X_WIN if board[i][0] == X_PLAYER else O_WIN

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] \
                and board[2][i] != " ":
            return X_WIN if board[0][i] == X_PLAYER else O_WIN

    # Check Digonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] \
            and board[2][2] != " ":
        return X_WIN if board[0][0] == X_PLAYER else O_WIN
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] \
            and board[2][0] != " ":
        return X_WIN if board[1][1] == X_PLAYER else O_WIN

    # Check for draw
    free_cells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_cells += 1

    if free_cells == 0:
        return DRAW
    return PLAYING


def display_board():
    print(f"""
{board[0][0]} | {board[0][1]} | {board[0][2]}
---------
{board[1][0]} | {board[1][1]} | {board[1][2]}
---------
{board[2][0]} | {board[2][1]} | {board[2][2]}
""")


def main():
    print("========== Tic Tac Toe Game ==========")

    current_turn = X_PLAYER
    while True:
        print()
        display_board()
        print("-- Current player:", current_turn)
        row = input("Enter row (1-3): ")
        column = input("Enter column (1-3): ")

        if not row.isdigit() or not column.isdigit():
            print("Invalid input!")
            continue
        row, column = int(row) - 1, int(column) - 1
        if row > 2 or row < 0 or column > 2 or column < 0:
            print("Invalid input!")
            continue

        if board[row][column] != " ":
            print("Cell is already occuppied!")
            continue

        board[row][column] = current_turn

        game_status = check_game_status()
        if game_status == X_WIN:
            print("Player X won!")
            break
        elif game_status == O_WIN:
            print("Player O won!")
            break
        elif game_status == DRAW:
            print("DRAW!")
            break

        if current_turn == X_PLAYER:
            current_turn = O_PLAYER
        else:
            current_turn = X_PLAYER

    display_board()


if __name__ == "__main__":
    main()
