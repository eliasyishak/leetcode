# https://leetcode.com/problems/maximum-average-pass-ratio
"""
This is fairly straightforward priority queue problem using a heap data
structure. This is also a greedy algorithm that can be understood once you
order the queue on the maximum possible gain a new student would add.
"""

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate_gain(passing: int, total: int) -> float:
            return -(((passing + 1) / (total + 1)) - (passing / total))

        queue = [
            [
                calculate_gain(passing, total),
                passing,
                total,
            ]
            for passing, total in classes
        ]
        heapq.heapify(queue)

        for _ in range(extraStudents):
            _, passing, total = heapq.heappop(queue)

            new_passing = passing + 1
            new_total = total + 1
            heapq.heappush(
                queue,
                [
                    calculate_gain(new_passing, new_total),
                    new_passing,
                    new_total,
                ],
            )

        return sum(passing / total for _, passing, total in queue) / len(classes)


if __name__ == "__main__":
    test_case_1 = {
        "classes": [[2, 2], [1, 2], [3, 5]],
        "extraStudents": 2,
    }  # 0.78333

    cls = Solution()
    ans = cls.maxAverageRatio(**test_case_1)
    print("----")
    print(ans)
