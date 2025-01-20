# https://leetcode.com/problems/product-of-array-except-self
"""
Need to use a prefix and suffix product sum array to handle the
calculation for each index.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        for i in range(n):
            left = i
            right = n - 1 - i

            if i > 0:
                prefix[left] = prefix[left - 1] * nums[left - 1]
                suffix[right] = suffix[right + 1] * nums[right + 1]

        return [prefix[i] * suffix[i] for i in range(n)]


if __name__ == "__main__":
    test_case_1 = [1, 2, 3, 4]  # [24, 12, 8, 6]

    cls = Solution()
    ans = cls.productExceptSelf(test_case_1)
    print("------")
    print(ans)
