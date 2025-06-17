# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array
"""
Very easy.
"""


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        nums.append(nums[0])

        res = 0
        for i in range(1, len(nums)):
            curr = abs(nums[i - 1] - nums[i])

            res = max(res, curr)

        return res
