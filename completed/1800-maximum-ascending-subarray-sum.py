# https://leetcode.com/problems/maximum-ascending-subarray-sum
"""
Easy problem; just keep track of the current sum and reset it if we find
that the next value is less than the previous value. Keep track of the max
as we go.
"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i, val in enumerate(nums):
            if i == 0:
                prev = val
                curr = val
            else:
                if val > prev:
                    curr += val
                else:
                    curr = val

                prev = val

            res = max(res, curr)

        return res


if __name__ == "__main__":
    test_case_1 = [10, 20, 30, 5, 10, 50]  # 65

    cls = Solution()
    ans = cls.maxAscendingSum(test_case_1)
    print("-----")
    print(ans)
