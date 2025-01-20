# https://leetcode.com/problems/first-completely-painted-row-or-column
"""
Marked as a medium problem but honestly doesn't feel like it needed to be.

My solution below is what the editorial comes up with for an optimal solution as well.

Just need to keep track of the total number of items we have set in each row and column
and return once we have completed setting all the items.
"""

from typing import Dict, List, Tuple, TypedDict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])

        # The ith item in this list gives us the count
        # of values set in the ith row
        row_count = [0 for _ in range(ROWS)]

        # Same but for columns
        col_count = [0 for _ in range(COLS)]

        lookup: Dict[int, Tuple[int, int]] = {}
        for i in range(ROWS):
            for j in range(COLS):
                val = mat[i][j]
                lookup[val] = (i, j)

        for index, val in enumerate(arr):
            i, j = lookup[val]
            row_count[i] += 1
            col_count[j] += 1

            if row_count[i] == COLS or col_count[j] == ROWS:
                return index

        return -1


class TestCaseType(TypedDict):
    arr: List[int]
    mat: List[List[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "arr": [1, 3, 4, 2],
        "mat": [
            [1, 4],
            [2, 3],
        ],
    }  # 2

    test_case_2: TestCaseType = {
        "arr": [2, 8, 7, 4, 1, 3, 5, 6, 9],
        "mat": [
            [3, 2, 5],
            [1, 4, 6],
            [8, 7, 9],
        ],
    }  # 3

    cls = Solution()
    ans = cls.firstCompleteIndex(**test_case_2)
    print("-----")
    print(ans)
