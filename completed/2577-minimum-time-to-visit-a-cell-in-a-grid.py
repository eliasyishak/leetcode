# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid
from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Early exit if we find that we can't move from the first cell
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = [
            (0, 0, 0),
        ]  # turns, i, j
        visited = set()

        ops = 0
        while queue:
            turns, i, j = heapq.heappop(queue)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            ops += 1
            if i == ROWS - 1 and j == COLS - 1:
                print("Operations completed", ops)
                return turns

            for x, y in directions:
                new_i, new_j = i + x, j + y

                if (
                    0 <= new_i < ROWS
                    and 0 <= new_j < COLS
                    and (new_i, new_j) not in visited
                ):
                    # Calculate the time it would take to get to the
                    # next cell by taking the difference between the current cell
                    # and the next cell and adding 1 if that difference is even

                    # This conditional is for the case we need to "waste time" before entering the cell
                    if grid[new_i][new_j] > turns + 1:
                        wait_time = 1 if (grid[new_i][new_j] - turns) % 2 == 0 else 0
                        heapq.heappush(
                            queue,
                            (grid[new_i][new_j] + wait_time, new_i, new_j),
                        )
                    else:
                        heapq.heappush(
                            queue,
                            (turns + 1, new_i, new_j),
                        )

        return -1


if __name__ == "__main__":
    test_case_1 = [
        [0, 1, 3, 2],
        [5, 1, 2, 5],
        [
            4,
            3,
            8,
            6,
        ],
    ]  # 7

    test_case = test_case_1

    cls = Solution()
    ans = cls.minimumTime(grid=test_case)
    print("---")
    print(ans)
