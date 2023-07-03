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
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and print every possible solution.

    Args:
        N (int): Size of the chessboard.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    def backtrack(row):
        if row == N:
            # All queens are placed, store the solution
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    # Print the solutions
    for solution in solutions:
        print(solution)


# Parse the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Solve the N Queens problem
solve_nqueens(N)

