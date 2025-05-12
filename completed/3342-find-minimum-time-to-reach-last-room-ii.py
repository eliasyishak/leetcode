# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii
"""
Very very similar to the 3341 version of this problem. The only thing we need
to consider here is that we need to alternate the number of seconds we spend
moving between each cell based on the number of steps that have been taken.
"""

import heapq

directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # down
]


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        heap = [(0, 0, 0, 0)]  # time, i, j, steps
        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        visited: set[tuple[int, int]] = set()

        while heap:
            time, i, j, step = heapq.heappop(heap)

            visited.add((i, j))

            if i == ROWS - 1 and j == COLS - 1:
                return time

            for dx, dy in directions:
                next_i, next_j = i + dx, j + dy
                if (
                    0 <= next_i < ROWS
                    and 0 <= next_j < COLS
                    and (next_i, next_j) not in visited
                ):
                    next_time = (
                        moveTime[next_i][next_j] - time
                        if moveTime[next_i][next_j] > time
                        else 0
                    )

                    next_time += 1 if step % 2 == 0 else 2

                    heapq.heappush(heap, (time + next_time, next_i, next_j, step + 1))
                    visited.add((next_i, next_j))

        return 0


if __name__ == "__main__":
    test_case_1 = [
        [0, 4],
        [4, 4],
    ]  # 7

    cls = Solution()
    ans = cls.minTimeToReach(test_case_1)
    print("-----")
    print(ans)
