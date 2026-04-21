"""
Given an m x n integer matrix, if an element is 0,
set its entire row and column to 0's.

You must do it in place.

e.g.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

def my_solution(matrix: list[list[int]]) -> None:
    """
    Solved this on my own first try!
    They just do not use enumerate, and use sets instead of lists
    """
    zero_rows = []
    zero_cols = []
    for row_i, row_val in enumerate(matrix):
        for col_i, col_val in enumerate(row_val):
            if col_val == 0:
                zero_rows.append(row_i)
                zero_cols.append(col_i)

    # Rows
    for zero_row in zero_rows:
        for i in range(len(matrix[zero_row])):
            matrix[zero_row][i] = 0

    # Cols
    for row_i, row_val in enumerate(matrix):
        for col_i, col_val in enumerate(row_val):
            if col_i in zero_cols:
                matrix[row_i][col_i] = 0

def apparently_more_optimal_solution(matrix: list[list[int]]) -> None:
    zero_rows = set()
    zero_cols = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0