# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
"""
This was a fun problem to work through. It feels like the problem is trying to
trick you into thinking that the grid means something. The first thing I did
was convert that grid into a list and sort it.

We also want to make all of those cell values converge on a number that requires
the minimum number of operations. If you think of a list, that means you would want
to converge towards the middle. I assumed that meant using the average at first, but
quickly realized that median is a better approach. That gaurantees that at least one
of the cells in the grid will have 0 operations performed on it.
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # No need to check anything for grid of one cell
        if ROWS == COLS == 1:
            return 0

        # Each cell in the grid must have the same modulus value
        modulus = grid[0][0] % x

        # Iterate through the cells in the grid and increment the counter
        # and add to the list to sort later
        #
        # Also checking to make sure each number has the same modulus, or
        # early exit if not
        nums: list[int] = [-1] * (ROWS * COLS)
        index = 0
        counter: dict[int, int] = defaultdict(int)
        for i in range(ROWS):
            for j in range(COLS):
                cell_value = grid[i][j]

                # If the current cell is not divisible by x, then we will
                # never be able to converge to one value
                if cell_value % x != modulus:
                    return -1

                nums[index] = cell_value
                index += 1
                counter[cell_value] += 1

        nums.sort()

        # We will use the median of the sorted array as our value
        # that all cells will converge on
        converge_value = nums[len(nums) // 2]

        # Iterate through conuter to add the number operations that
        # need to be made for each value
        res = 0
        for cell_value, count in counter.items():
            res += int(abs(converge_value - cell_value) / x) * count

        return res


class TestCaseType(TypedDict):
    grid: list[list[int]]
    x: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "grid": [[2, 4], [6, 8]],
        "x": 2,
    }  # 4

    test_case_2: TestCaseType = {
        "grid": [[1, 5], [2, 3]],
        "x": 1,
    }  # 5

    test_case_3: TestCaseType = {
        "grid": [[931, 128], [639, 712]],
        "x": 73,
    }  # 12

    cls = Solution()
    ans = cls.minOperations(**test_case_1)
    print("------")
    print(ans)
