# https://leetcode.com/problems/map-of-highest-peak
"""
This problem can be solved by understanding that the answer for each
cell is the shortest distance to a water cell. This is easily understood
in the 1D case

The original array followed by the answer to this question in 2D
[0, 0, 0, 1, 0, 0]
       |
       V
[3, 2, 1, 0, 1, 2]

If we did this in 2D, that means we would need to consider the up and down
directions as well as the left and right.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        queue: Deque[Tuple[int, int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()
        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    isWater[i][j] = 0
                    visited.add((i, j))

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                i, j, distance = queue.popleft()
                distance += 1
                for x, y in directions:
                    new_i, new_j = i + x, j + y

                    if (
                        0 <= new_i < ROWS
                        and 0 <= new_j < COLS
                        and (new_i, new_j) not in visited
                    ):
                        isWater[new_i][new_j] = distance
                        queue.append((new_i, new_j, distance))
                        visited.add((new_i, new_j))

        return isWater


if __name__ == "__main__":
    test_case_1 = [[0, 1], [0, 0]]  # [[1,0],[2,1]]
    test_case_2 = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 0],
    ]  # [[1,1,0],[0,1,1],[1,2,2]]

    cls = Solution()
    ans = cls.highestPeak(test_case_2)
    print("------")
    print(ans)
