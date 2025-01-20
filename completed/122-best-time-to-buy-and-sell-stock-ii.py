# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""
To understand this problem, you have to really take advantage of the fact
that you can buy and sell multiple times within the time range.
If we take advantage of that property, then we are essentially summing all
of the times that the price difference between consecutive days is greater than
0.

The sum of all the positive slopes will always be the most money you can make.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])

        return res


if __name__ == "__main__":
    test_case_1 = [7, 1, 5, 3, 6, 4]  # 7

    cls = Solution()
    ans = cls.maxProfit(test_case_1)
    print("-----")
    print(ans)
