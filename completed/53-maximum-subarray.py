# https://leetcode.com/problems/maximum-subarray
"""
This problem implements Kadane's algorithm which states that
we check if at each index i, the prefix sum up to i + val is
greater than just the value at i

For example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

@ i = 0; prefixSum = -2                         // this is all we can do here
@ i = 1; prefixSum = max(prefixSum + 1, 2)      // at this point, we have to decide if we reset our prefix,
                                                   and in this case, we do because our sum is greater without
                                                   the previous summations
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        curr_sum = nums[0]
        for i, val in enumerate(nums):
            if i == 0:
                continue

            curr_sum = max(val, curr_sum + val)
            res = max(res, curr_sum)

        return res


if __name__ == "__main__":
    test_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6

    cls = Solution()
    ans = cls.maxSubArray(test_case_1)
    print("------")
    print(ans)
