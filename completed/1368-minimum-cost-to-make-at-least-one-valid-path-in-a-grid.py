# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid
"""
Need to implement a solution using Dijkstra's algorithm where we attempt
to check all of the directions that don't cost anything first before attempting
routes that have a cost
"""

import heapq
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and (i, j) not in visited

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }

        queue = [(0, 0, 0)]  # cost, i, j
        visited = set()  # (i, j)

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                cost, i, j = heapq.heappop(queue)
                curr = grid[i][j]

                if (i, j) in visited:
                    continue

                if i == ROWS - 1 and j == COLS - 1:
                    return cost

                visited.add((i, j))

                # At each position, we can either go the direction the cell
                # specifies or take the cost and change the direction
                #
                # So at each cell, we will add to the queue the direction the
                # cell points to (if valid), and all directions that are unvisted
                # with an additional cost

                # First we will attempt to add the cell the current cell points to
                next_i, next_j = (i + directions[curr][0], j + directions[curr][1])
                if valid(next_i, next_j):
                    heapq.heappush(queue, (cost, next_i, next_j))

                # Now iterate through all the possible directions that are valid and
                # add them to the queue and increment the cost
                for _, (x, y) in directions.items():
                    next_i, next_j = i + x, j + y
                    if valid(next_i, next_j):
                        heapq.heappush(queue, (cost + 1, i + x, j + y))

        return 0


if __name__ == "__main__":
    test_case_1 = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [1, 1, 1, 1],
        [2, 2, 2, 2],
    ]  # 3

    test_case_2 = [
        [1, 1, 3],
        [3, 2, 2],
        [1, 1, 4],
    ]  # 0

    test_case_3 = [
        [1, 2],
        [4, 3],
    ]  # 1

    cls = Solution()
    ans = cls.minCost(test_case_1)
    print("-----")
    print(ans)
