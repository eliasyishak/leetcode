# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii
"""
If you look at this mathematically when looking at the formula we want to maximize
    (nums[i] - nums[j]) * nums[k]

We want to minimize nums[j] and maximize the values at i and k. With some preprocessing
to get the max value at each index before for the prefix... and do the same for k by finding
the largest value to the right of each index. With those preprocessed lists, we can them simply
iterate through the list one more time and find the max result.

Good problem.
"""


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        prefix = [0] * n
        suffix = [0] * n

        # Preprocess and keep track of the largest number at each
        # index to the left and right of i
        for i in range(n):
            left = i
            right = n - i - 1

            # We skip i = 0 because we are looking values to the left (and right)
            # of i
            if i > 0:
                prefix[left] = max(nums[left - 1], prefix[left - 1])
                suffix[right] = max(nums[right + 1], suffix[right + 1])

        # Use the prefix and suffix lists to find the max value
        for i in range(1, n - 1):
            res = max(res, (prefix[i] - nums[i]) * suffix[i])

        return res


if __name__ == "__main__":
    test_case_1 = [12, 6, 1, 2, 7]  # 77
    test_case_2 = [10, 13, 6, 2]  # 14

    cls = Solution()
    ans = cls.maximumTripletValue(test_case_1)
    print("-------")
    print(ans)
