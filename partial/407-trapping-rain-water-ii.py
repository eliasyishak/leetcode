# https://leetcode.com/problems/trapping-rain-water-ii
"""
Tough problem, need to review further. The first version of this problem
in 2D is more intuitive when you can keep a list of maxes on the left and right
but this is tough in 3D
"""

from typing import List, Set, Tuple


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS = len(heightMap)
        COLS = len(heightMap[0])

        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }

        res = 0

        def bfs(i: int, j: int, visited: Set[Tuple[int, int]]) -> int:
            queue = [(i, j)]
            curr_max = 0

            while queue:
                q_len = len(queue)

                for _ in range(q_len):
                    i, j = queue.pop(0)

                    if (i, j) in visited or not 0 <= i < ROWS or not 0 <= j < COLS:
                        continue

                    visited.add((i, j))
                    curr_max = max(curr_max, heightMap[i][j])

                    # Now iterate in all directions and add them to the queue if the
                    # next cell is inbounds AND the neighbor height is greater than the
                    # current cell we are in
                    for _, (x, y) in directions.items():
                        next_i, next_j = i + x, j + y
                        if (
                            0 <= next_i < ROWS
                            and 0 <= next_j < COLS
                            and heightMap[next_i][next_j] > heightMap[i][j]
                        ):
                            queue.append((next_i, next_j))

            return curr_max

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                # For the current cell, find the max wall height
                # in all 4 directions
                current_height = heightMap[i][j]
                wall_maxs = [
                    # Up
                    bfs(i - 1, j, set([(i, j)])),
                    # Right
                    bfs(i, j + 1, set([(i, j)])),
                    # Down
                    bfs(i + 1, j, set([(i, j)])),
                    # Left
                    bfs(i, j - 1, set([(i, j)])),
                ]

                # Take the minimum height and find the difference between
                # the current height
                res += max(0, min(wall_maxs) - current_height)

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

    # TODO: (eliasyishak) this is failing for this test
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
