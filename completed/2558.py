# https://leetcode.com/problems/take-gifts-from-the-richest-pile
"""
Classic heap problem
"""

from typing import List
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1 * val for val in gifts]

        heapq.heapify(gifts)
        for _ in range(k):
            biggest_item = heapq.heappop(gifts)
            reduced = int(abs(biggest_item) ** 0.5)
            heapq.heappush(gifts, -reduced)

        return sum([abs(val) for val in gifts])


if __name__ == "__main__":
    test_case = {
        "gifts": [25, 64, 9, 4, 100],
        "k": 4,
    }  # 29

    cls = Solution()
    ans = cls.pickGifts(gifts=test_case["gifts"], k=test_case["k"])
    print("----")
    print(ans)
