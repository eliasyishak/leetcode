# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k
"""
Using a set to keep track of all of the values that are greater than k tells us how
many operations we need to make to get towards k.

We are also able to immediately exit if we find that a value is less than k because
we cannot increase our numbers, only can decrease them.
"""

from typing import TypedDict


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # Collect the numbers that are greater
        s: set[int] = set()
        for val in nums:
            if val < k:
                return -1
            elif val > k:
                s.add(val)

        return len(s)


class TestCaseType(TypedDict):
    nums: list[int]
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [5, 2, 5, 4, 5],
        "k": 2,
    }  # 2

    cls = Solution()
    ans = cls.minOperations(**test_case_1)
    print("-----")
    print(ans)
