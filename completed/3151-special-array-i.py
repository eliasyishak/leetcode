# https://leetcode.com/problems/special-array-i
"""
Very simple problem, just make sure that if an item in the array is even
that the following item is odd.
"""

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i, val in enumerate(nums):
            if i == 0:
                is_even = val % 2 == 0
            else:
                curr = val % 2 == 0
                if is_even == curr:
                    return False
                is_even = curr

        return True


if __name__ == "__main__":
    test_case_1 = [4, 3, 1, 6]  # false

    cls = Solution()
    ans = cls.isArraySpecial(test_case_1)
    print("----")
    print(ans)
