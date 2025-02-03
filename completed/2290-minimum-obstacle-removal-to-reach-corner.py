# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner
"""
This was not too difficult to understand when you think of traversing the graph
through BFS but with a twist.. when keeping track of our queue, we want to priortize
visiting cells that don't have obstacles in the way. So if we pop from the queue and find
a cell that has an obstacle, that would mean the entire queue is full of obstacles.
"""

from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([(0, 0, 0)])  # i, j, obstacles_encountered
        min_obstacles = [[float("inf")] * COLS for _ in range(ROWS)]

        while queue:
            i, j, obstacles_encountered = queue.popleft()

            if i == ROWS - 1 and j == COLS - 1:
                return obstacles_encountered

            for x, y in directions:
                new_i, new_j = i + x, j + y

                if (
                    0 <= new_i < ROWS
                    and 0 <= new_j < COLS
                    and min_obstacles[new_i][new_j] == float("inf")
                ):
                    if grid[new_i][new_j] == 0:
                        min_obstacles[new_i][new_j] = obstacles_encountered
                        queue.appendleft((new_i, new_j, obstacles_encountered))
                    else:
                        min_obstacles[new_i][new_j] = obstacles_encountered + 1
                        queue.append((new_i, new_j, obstacles_encountered + 1))
        return -1


if __name__ == "__main__":
    test_case_1 = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]  # 2
    test_case_2 = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]  # 0

    test_case = test_case_1

    cls = Solution()
    ans = cls.minimumObstacles(grid=test_case)
    print("----")
    print(ans)
