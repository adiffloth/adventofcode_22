def can_be_extended_to_solution(board, row, column):
    if board[row][column] == 1:
        if row > 0 and column > 0 and board[row - 1][column - 1] == 1:
            return False

        if row > 0 and board[row - 1][column] == 2:
            return False

        if column > 0 and board[row][column - 1] == 2:
            return False

    if board[row][column] == 2:
        if row > 0 and board[row - 1][column] == 1:
            return False

        if row > 0 and column < n - 1 and board[row - 1][column + 1] == 2:
            return False

        if column > 0 and board[row][column - 1] == 1:
            return False

    return True


def extend(board, row, column, diags):
    n = len(board)

    for k in [2, 1, 0]:
        board[row][column] = k
        if can_be_extended_to_solution(board, row, column):
            if row == n - 1 and column == n - 1:
                # all the board is filled in already
                num_diags = 0
                for i in range(n):
                    for j in range(n):
                        if board[i][j] > 0:
                            num_diags += 1
                if num_diags == diags:
                    symbols = [' ', '\\', '/']
                    for i in range(n):
                        for j in range(n):
                            print(symbols[board[i][j]], end="")
                        print()

                    exit(-1)

                return

            if column < n - 1:
                nextrow, nextcolumn = row, column + 1
            else:
                nextrow, nextcolumn = row + 1, 0

            extend(board, nextrow, nextcolumn, diags)


n = 5
extend([[-1] * n for _ in range(n)], row=0, column=0, diags=16)
