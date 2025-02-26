# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray
"""
An extension of Kadane's algorithm where we also now look for the max
and min sums for the subarrays. Related to 53-maximum-subarry.py.

The idea here is to reset our current sum (either max or min) when we find
a new value that is better for that max/min or keep adding to prefix
"""

"""
Copied from 53 for finding the maximum sum only
For example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

@ i = 0; prefixSum = -2                         // this is all we can do here
@ i = 1; prefixSum = max(prefixSum + 1, 2)      // at this point, we have to decide if we reset our prefix,
                                                   and in this case, we do because our sum is greater without
                                                   the previous summations
"""


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return abs(nums[0])

        res = nums[0]

        curr_sum_max = nums[0]
        curr_sum_min = nums[0]

        for i, val in enumerate(nums):
            if i == 0:
                continue

            curr_sum_max = max(val, curr_sum_max + val)
            curr_sum_min = min(val, curr_sum_min + val)

            res = max(res, abs(curr_sum_max), abs(curr_sum_min))

        return res


if __name__ == "__main__":
    test_case_1 = [1, -3, 2, 3, -4]  # 5
    test_case_2 = [2, -5, 1, -4, 3, -2]  # 8

    cls = Solution()
    ans = cls.maxAbsoluteSum(test_case_2)
    print("------")
    print(ans)
