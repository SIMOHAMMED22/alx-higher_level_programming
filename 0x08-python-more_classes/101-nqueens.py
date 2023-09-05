#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_util(board, 0, n, solutions)
    return solutions


def solve_util(board, row, n, solutions):
    if row == n:
        solution = ["." * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution[i] = solution[i][:j] + "Q" + solution[i][j + 1:]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_util(board, row + 1, n, solutions)
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solutions = solve_nqueens(n)
        for solution in solutions:
            for row in solution:
                print(row)
            print()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
