# https://leetcode.com/problems/number-of-black-blocks/
"""
Good problem with grids that doesn't necessarily require you
to create the whole grid and simulate the black cells and traverse
again to get the answer.

You can instead just use the black cell coordinate list and tabulate
the count of 2x2 grids that have a black grid in them. This is because
the grid is limited to 2x2, if the subgrids were variable, this may not be
the best approach.
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: list[list[int]]
    ) -> list[int]:
        res = [0 for _ in range(5)]

        # Initialize the first index in res to have the total
        # number of empty 2x2 grids if there was nothing in coordinates
        res[0] = (m - 1) * (n - 1)

        # Map from (top-left corner of 2x2 grid) -> count of black cells in that grid
        grid_count: dict[tuple[int, int], int] = defaultdict(int)

        for i, j in coordinates:
            # Each black cell can be part of up to 4 different 2x2 subgrids
            for dx in [0, -1]:
                for dy in [0, -1]:
                    x, y = i + dx, j + dy

                    # Important to notice that we are doing
                    # m - 1 and n - 1
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        # Each value will be the total black cells
                        # that touch x, y
                        grid_count[(x, y)] += 1

        print(dict(grid_count))
        for (_, _), black_counts in grid_count.items():
            res[black_counts] += 1
            res[0] -= 1

        return res


{
    (0, 0): 2,
    (1, 1): 1,
    (1, 0): 1,
    (0, 1): 2,
}  # type: ignore

if __name__ == "__main__":

    class TestCase(TypedDict):
        m: int
        n: int
        coordinates: list[list[int]]

    test_case_1: TestCase = {
        "m": 3,
        "n": 3,
        "coordinates": [
            [0, 0],
            [1, 1],
            [0, 2],
        ],
    }  # [0,2,2,0,0]

    cls = Solution()
    ans = cls.countBlackBlocks(**test_case_1)
    print("-------")
    print(ans)
