def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place
    :param matrix:
    :return:
    """
    edge_length = len(matrix)
    top = 0
    bottom = edge_length - 1

    # Vertical Reversal
    while top < bottom:
        """
        - The top pointer starts at the first row and the bottom pointer starts at the last row
        - We swap the corresponding rows for every column
        - The top pointer moves downward, and the bottom pointer moves upward, processing the matrix layer by layer
        """
        for col in range(edge_length):
            temp = matrix[top][col]
            matrix[top][col] = matrix[bottom][col]
            matrix[bottom][col] = temp
        top += 1
        bottom -= 1

    # Transpose
    for row in range(edge_length):
        for col in range(row + 1, edge_length):
            """
            - The row loop ensures we process only the upper triangular matrix (excluding the diagonal).
            - The col loop starts from row + 1 avoiding redundant swaps
            """
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

def rotate_cool_one_line_solution(matrix: list[list[int]]) -> None:
    """
    Just memorize this. This is hilarious.
    """
    matrix[:] = zip(*matrix[::-1])