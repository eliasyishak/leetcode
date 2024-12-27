# https://leetcode.com/problems/best-sightseeing-pair
"""
Good logical puzzle to think about, the problem tries to trick you
by adding and subtracting the index for the left and right pointers.

Think of this problem; what two indices give us the highest sum:
[8, 1, 5, 2, 6]

To solve this, you would keep track of two pointers as you traverse the array
from left to right. Left pointer starts at 8 and will remain there since we don't
have a value greater than it while the right one seeks the next highest value

With this problem, instead of the left pointer being on the highest value, it is
on:
- Left = val + i
- Right = val - i

If we encounter a value that is greater, we need to remember to add the original i TWICE.
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = None
        right = None
        res = -float("inf")
        for i, val in enumerate(values):
            if i == 0:
                left = val + i
            else:
                right = val - i
                res = max(res, left + right)

                # Need to add twice because adding only one i gives us 0
                left = max(left, right + i + i)

        return res


if __name__ == "__main__":
    test_case_1 = [8, 1, 5, 2, 6]  # 11
    test_case_2 = [1, 2]  # 2
    test_case_3 = [1, 3, 5]  # 7

    cls = Solution()
    ans = cls.maxScoreSightseeingPair(test_case_3)
    print("-----")
    print(ans)
