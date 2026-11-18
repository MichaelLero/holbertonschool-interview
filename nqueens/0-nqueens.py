#!/usr/bin/python3
"""N queens solver: prints every solution to the N queens puzzle."""


import sys


def is_safe(solution, row, col):
    """Checks whether a queen at (row, col) is attacked by placed queens.

    Args:
        solution (list): Columns of the queens already placed, where
            the index is the row.
        row (int): Row of the new queen.
        col (int): Column of the new queen.

    Returns:
        bool: True if no queen attacks the position, else False.
    """
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row=0, solution=None, results=None):
    """Finds all solutions using backtracking, one queen per row.

    Args:
        n (int): Size of the board.
        row (int): Current row being filled.
        solution (list): Columns of the queens placed so far.
        results (list): Collected solutions.

    Returns:
        list: All solutions, each a list of [row, column] pairs.
    """
    if solution is None:
        solution = []
    if results is None:
        results = []

    if row == n:
        results.append([[r, c] for r, c in enumerate(solution)])
        return results

    for col in range(n):
        if is_safe(solution, row, col):
            solution.append(col)
            solve(n, row + 1, solution, results)
            solution.pop()

    return results


def main():
    """Validates the arguments and prints every solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for result in solve(n):
        print(result)


if __name__ == "__main__":
    main()
