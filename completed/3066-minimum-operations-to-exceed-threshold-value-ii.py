# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii
"""
Using a heap to keep track of the values we have left to process helps a ton with
this problem. To make sure all of the values we have in our list are greater than
k, we set our condition for the while loop to just check the top of heap, which will
be our smallest value in the list.
"""

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        queue: list[int] = []
        for val in nums:
            heapq.heappush(queue, val)

        res = 0
        while queue and queue[0] < k:
            first = heapq.heappop(queue)
            second = heapq.heappop(queue)

            transform = first * 2 + second
            heapq.heappush(queue, transform)

            res += 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 2, 3, 10, 11],
        "k": 10,
    }  # 2

    test_case_2 = {
        "nums": [1, 1, 2, 4, 9],
        "k": 20,
    }  # 4

    cls = Solution()
    ans = cls.minOperations(**test_case_2)  # type: ignore
    print("----")
    print(ans)
