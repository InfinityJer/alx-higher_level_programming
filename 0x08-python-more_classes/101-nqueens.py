#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position.

    Args:
        board (list): Current board configuration.
        row (int): Row index.
        col (int): Column index.
        N (int): Size of the board.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem and print all solutions.

    Args:
        N (int): Size of the chessboard.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            # All queens are placed, store the solution
            solution = []
            for i in range(N):
                row_str = ""
                for j in range(N):
                    if board[i][j] == 1:
                        row_str += "Q"
                    else:
                        row_str += "."
                solution.append(row_str)
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()

# Parse the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the N Queens problem
solve_nqueens(N)

