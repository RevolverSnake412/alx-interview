#!/usr/bin/python3
"""
Matrix rotation by 90 degrees
"""

from typing import List

def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a 2D matrix by 90 degrees clockwise in place.

    Parameters:
    matrix (List[List[int]]): A 2D list of integers representing the matrix to rotate.

    Returns:
    None
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) == 0:
        return

    if not all(isinstance(row, list) for row in matrix):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    # Transpose the matrix
    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the 90 degrees rotated matrix
    for i in range(rows):
        matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(mat)
    print(mat)
