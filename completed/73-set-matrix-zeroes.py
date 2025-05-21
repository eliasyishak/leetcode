# https://leetcode.com/problems/set-matrix-zeroes
"""
This is a fairly trivial problem if we decided to use extra space for the solution
but the problem challenged to use no extra space (ie: O(1)).

To do this, we need to make modifications to the input matrix itself to keep state
in the row and columns that need to be flipped to zeroes.

Personally, I think this is a very stupid approach to the problem, this would be terrible
production code and testing this skill is purely for academic purposes.
"""

from typing import Any


class Solution:
    def setZeroes(self, matrix: list[list[Any]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # We need special handling for the first row and column
        first_row = False
        first_col = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if not first_row:
                        first_row = i == 0
                    if not first_col:
                        first_col = j == 0

                    # Set the flag for the row
                    if not isinstance(matrix[i][0], tuple):
                        matrix[i][0] = (matrix[i][0], 1)
                    # Set the flag for the column
                    if not isinstance(matrix[0][j], tuple):
                        matrix[0][j] = (matrix[0][j], 1)

        # Go through the rows first and set zeroes (not including the first row)
        for i in range(1, ROWS):
            if isinstance(matrix[i][0], tuple):
                for j in range(COLS):
                    matrix[i][j] = 0

        # Go through the columns second (not including the first column)
        for j in range(1, COLS):
            if isinstance(matrix[0][j], tuple):
                for i in range(ROWS):
                    matrix[i][j] = 0

        if first_row:
            for j in range(COLS):
                matrix[0][j] = 0
        if first_col:
            for i in range(ROWS):
                matrix[i][0] = 0

        print("-----")
        for row in matrix:
            print(row)


if __name__ == "__main__":
    test_case_1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    """
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
    """

    test_case_2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    """
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0],
    """

    cls = Solution()
    cls.setZeroes(test_case_2)
