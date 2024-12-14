# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag
"""
This was a bit difficult to understand at first. Initially I was thinking that
we would want to use a heap and simple divide the largest value in half every time
and take the largest value, but that doesn't work with the first test case of [9]

The real magic is being able to understand the clever calculation to determine how
many operations each bag would need to hit a target value
"""

from typing import List
import math


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        def is_possible(target):
            ops = 0
            for val in nums:
                ops += math.ceil(val / target) - 1
                if ops > maxOperations:
                    return False

            return True

        while left < right:
            mid = (left + right) // 2

            if is_possible(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    test_case_1 = {
        "nums": [9],
        "maxOperations": 2,
    }  # 3

    test_case = test_case_1

    cls = Solution()
    ans = cls.minimumSize(
        maxOperations=test_case["maxOperations"], nums=test_case["nums"]
    )
    print("-----")
    print(ans)
