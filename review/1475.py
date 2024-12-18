# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
"""
Easy problem if you implemented the brute forced O(n^2) but this can be done in linear
time with a monotonic stack.

Need to review more
"""

from collections import deque
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = deque()

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                top = stack.pop()
                prices[top] -= price
            stack.append(i)

        return prices


if __name__ == "__main__":
    test_case_1 = [8, 4, 6, 2, 3]  # [4,2,4,2,3]

    cls = Solution()
    ans = cls.finalPrices(prices=test_case_1)
    print("-----")
    print(ans)
