# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros
"""
Taking a greedy approach to this problem helps us find the minimum sum that
we need to make each of the arrays equal to each other. We must start off by
first checking for the -1 case though to ensure that a greedy solution is possible.

The test cases for this problem really help. In this case, I solved for the two provided
test cases and that unlocked the pattern for the rest of the problem.
"""


class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        # Number of zeros in each list
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # Condition for an early exit
        if zeros2 == 0 and sum1 + zeros1 > sum2:
            return -1

        if zeros1 == 0 and sum2 + zeros2 > sum1:
            return -1

        return max(sum2 + zeros2, sum1 + zeros1)


if __name__ == "__main__":
    test_case_1 = {
        "nums1": [3, 2, 0, 1, 0],
        "nums2": [6, 5, 0],
    }  # 12

    test_case_2 = {
        "nums1": [2, 0, 2, 0],
        "nums2": [1, 4],
    }  # -1

    cls = Solution()
    ans = cls.minSum(**test_case_1)
    print("------")
    print(ans)
