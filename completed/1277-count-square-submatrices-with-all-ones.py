# https://leetcode.com/problems/count-square-submatrices-with-all-ones
"""
There is probably a more optimal approach here that uses DP to solve the problem.

But this solution seems for intuitive to me. Iterate through each cell and
try to expand the square to the bottom right from that index by checking each
of the new values.
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def calc(i: int, j: int) -> int:
            """

            (i, j) --> (i + 1, j + 1)

            COLS to check = [
                (i, j + 1),
                (i + 1, j + 1) // <-- same
            ]

            ROWS to check = [
                (i + 1, j),
                (i + 1, j + 1) // <-- same
            ]

            """
            # Default to one square at least for the 1x1 case
            curr = 1
            width = 1

            while True:
                new_row = [(i + width, j + y) for y in range(width + 1)]
                new_col = [(i + x, j + width) for x in range(width + 1)]

                break_out = False
                for arr in [new_row, new_col]:
                    for new_i, new_j in arr:
                        if (
                            not 0 <= new_i < ROWS
                            or not 0 <= new_j < COLS
                            or matrix[new_i][new_j] == 0
                        ):
                            return curr

                if break_out:
                    return curr

                width += 1
                curr += 1

        squares = 0
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 1:
                    squares += calc(i, j)

        return squares


if __name__ == "__main__":
    test_case_1 = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]  # 15

    test_case_2 = [
        [1, 1],
        [1, 1],
    ]  # 5

    cls = Solution()
    ans = cls.countSquares(test_case_1)
    print("-----")
    print(ans)
