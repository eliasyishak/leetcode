# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i
"""
Relatively straightforward djisktra's algorith approach. Tricky part here is to
understand that the time at 0,0 is really not important since you already started there.

For example, the below test case does not require you to wait 56 seconds before moving,
you only need to wait 3 seconds to move to the next open position.

test_case_4 = [
    [56, 93],
    [3, 38],
]  # 39
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
        heap = [(0, 0, 0)]  # time, i, j
        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        visited: set[tuple[int, int]] = set()

        while heap:
            time, i, j = heapq.heappop(heap)

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
                    ) + 1

                    heapq.heappush(heap, (time + next_time, next_i, next_j))
                    visited.add((next_i, next_j))

        return 0


if __name__ == "__main__":
    test_case_1 = [
        [0, 4],
        [4, 4],
    ]  # 6

    test_case_2 = [
        [0, 0, 0],
        [0, 0, 0],
    ]  # 3

    test_case_3 = [
        [17, 56],
        [97, 80],
    ]  # 81

    test_case_4 = [
        [56, 93],
        [3, 38],
    ]  # 39

    cls = Solution()
    ans = cls.minTimeToReach(test_case_2)
    print("-----")
    print(ans)
