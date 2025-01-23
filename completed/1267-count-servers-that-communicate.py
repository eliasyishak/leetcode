# https://leetcode.com/problems/count-servers-that-communicate
"""
First pass you go through the rows and count all of the rows that have more
than one computer on them. Also keep track of these cells.

Then go through the columns and add 1 to the result for each cell in a column
that has more than one set cell AND that cell hasn't already been counted in
the rows.
"""

from typing import List, Set, Tuple

CoordinateSet = Set[Tuple[int, int]]
RowValuesType = List[CoordinateSet]


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        # Collect all of the coordinates for 1 cells by row
        counted: CoordinateSet = set()
        for i in range(ROWS):
            curr_row: CoordinateSet = set()
            for j in range(COLS):
                cell = grid[i][j]
                if cell == 1:
                    curr_row.add((i, j))

            # Register rows that have more than one computer on them to
            # increase our result variable
            if len(curr_row) > 1:
                res += len(curr_row)
                for coord in curr_row:
                    counted.add(coord)

        # Do the same except for column values
        for j in range(COLS):
            curr_col = set()
            for i in range(ROWS):
                cell = grid[i][j]
                if cell == 1:
                    curr_col.add((i, j))

            # For every column that has more than one cell set, iterate through
            # each of the coordinates that have not been accounted for yet
            if len(curr_col) > 1:
                for coord in curr_col:
                    if coord not in counted:
                        res += 1

        return res


if __name__ == "__main__":
    test_case_1 = [
        [1, 0],
        [0, 1],
    ]  # 0
    test_case_2 = [
        [1, 0],
        [1, 1],
    ]  # 3
    test_case_3 = [
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]  # 4

    cls = Solution()
    ans = cls.countServers(test_case_3)
    print("-----")
    print(ans)
