# https://leetcode.com/problems/trapping-rain-water-ii
"""
This was labeled a hard question and it requires to think about how the water
fills up. Instead of thinking of the water as "raining" down in the grid, it is
easier to think of it as the water rising from the perimeter and seeing how it flows
into each cell.

The important thing to note about this problem is that you want to start off by checking
all of the boundary layers first.

This concept is similar to the 2D representation of this problem. For that solution we are
keeping track of the left and right max heights to determine how much water can pool up
in a cell. In the 3D case, we have 3 boundary layers to check.
"""

import heapq
from typing import List, Set, Tuple


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS = len(heightMap)
        COLS = len(heightMap[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        res = 0

        # Begin by adding all of the boundary cells
        visited: Set[Tuple[int, int]] = set()
        min_heap: List[Tuple[int, int, int]] = []
        for i in range(ROWS):
            for j in range(COLS):
                if i in [0, ROWS - 1] or j in [0, COLS - 1]:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        # Assume that water is rising from the outside and try to find
        # the cells that the water will pour into which is why we start
        # by adding all of the boundary layers
        max_height = 0
        while min_heap:
            curr_height, i, j = heapq.heappop(min_heap)

            max_height = max(max_height, curr_height)

            for x, y in directions:
                next_i, next_j = i + x, j + y
                if (
                    0 <= next_i < ROWS
                    and 0 <= next_j < COLS
                    and (next_i, next_j) not in visited
                ):
                    visited.add((next_i, next_j))
                    heapq.heappush(
                        min_heap, (heightMap[next_i][next_j], next_i, next_j)
                    )

                    # If the neighboring cell is lower than the max_height
                    # we are able to fill up the water
                    if heightMap[next_i][next_j] < max_height:
                        res += max_height - heightMap[next_i][next_j]

        return res


if __name__ == "__main__":
    test_case_1 = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1],
    ]  # 4

    test_case_2 = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3],
    ]  # 10

    test_case_3 = [
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13],
    ]  # 14

    cls = Solution()
    ans = cls.trapRainWater(test_case_3)
    print("-----")
    print(ans)
