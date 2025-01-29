# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid
"""
Straight forward BFS problem where you look to start at group of cells
you have not visited yet.
"""

from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def search(i: int, j: int) -> int:
            res = 0
            queue = deque([(i, j)])

            while queue:
                q_len = len(queue)

                for _ in range(q_len):
                    i, j = queue.popleft()
                    if (i, j) in visited:
                        continue

                    visited.add((i, j))
                    res += grid[i][j]

                    for x, y in directions:
                        next_i, next_j = i + x, j + y
                        if (
                            0 <= next_i < ROWS
                            and 0 <= next_j < COLS
                            and (next_i, next_j) not in visited
                            and grid[next_i][next_j] > 0
                        ):
                            queue.append((next_i, next_j))

            return res

        visited: set[tuple[int, int]] = set()
        max_fish = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] > 0 and (i, j) not in visited:
                    max_fish = max(max_fish, search(i, j))

        return max_fish


if __name__ == "__main__":
    test_case_1 = [
        [0, 2, 1, 0],
        [4, 0, 0, 3],
        [1, 0, 0, 4],
        [0, 3, 2, 0],
    ]  # 7

    test_case_2 = [
        [8, 6],
        [2, 6],
    ]  # 22

    cls = Solution()
    ans = cls.findMaxFish(test_case_2)
    print("----")
    print(ans)
