#!/usr/bin/python3
import sys


def check_horizontal(board, position):
    x, y = position
    for i in range(x):
        if board[y][i] == 1:
            return True
    return False


def check_top_left_diagonal(board, position):
    x, y = position
    while y >= 0 and x >= 0:
        if board[y][x] == 1:
            return True
        y -= 1
        x -= 1
    return False


def check_bottom_left_diagonal(board, position, size):
    x, y = position
    while y < size and x >= 0:
        if board[y][x] == 1:
            return True
        y += 1
        x -= 1
    return False


def checker(board, position, size):
    return (check_horizontal(board, position) or
            check_top_left_diagonal(board, position) or
            check_bottom_left_diagonal(board, position, size))


def backtrack(board, x, size, positions=[]):
    if x == size:
        print(positions)
        return True
    for y in range(size):
        if not checker(board, (x, y), size):
            board[y][x] = 1
            backtrack(board, x + 1, size, positions + [[x, y]])
            board[y][x] = 0
    return False


def main(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    backtrack(board, 0, size)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
    else:
        try:
            number = int(sys.argv[1])
            if number < 4:
                print("N must be at least 4")
            else:
                main(number)
        except (TypeError, ValueError):
            print("N must be a number")
