#!/usr/bin/python3
"""Practice n queens algos"""


def solve_n_queens_optimized(n):
    """Solve n queens problem using optimized backtracking"""
    solutions = []
    board = [-1] * n  # No queens placed yet
    cols = [False] * n  # Tracks columns under attack
    main_diag = [False] * (2 * n - 1)  # Tracks main diagonal under attack
    anti_diag = [False] * (2 * n - 1)  # Tracks anti diagonal under attack

    place_queens_optimized(board, 0, n, solutions, cols, main_diag, anti_diag)

    return solutions


def place_queens_optimized(
        board, row, n, solutions, cols, main_diag, anti_diag):
    """Place queens on the board"""
    if row == n:
        # Found a valid solution, add it to the list
        solutions.append(board[:])
        return

    for col in range(n):
        if cols[col] or main_diag[row - col + n - 1] or anti_diag[row + col]:
            continue  # Skip if the column or diagonals are under attack

        # Place the queen
        board[row] = col
        cols[col] = True
        main_diag[row - col + n - 1] = True
        anti_diag[row + col] = True

        # Recursively place queens in the next row
        place_queens_optimized(
            board, row + 1, n, solutions, cols, main_diag, anti_diag)

        # Backtrack by removing the queen
        cols[col] = False
        main_diag[row - col + n - 1] = False
        anti_diag[row + col] = False


# Run the algorithm
n = 4
solutions = solve_n_queens_optimized(n)
for solution in solutions:
    print(solution)
