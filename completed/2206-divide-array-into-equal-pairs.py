# https://leetcode.com/problems/divide-array-into-equal-pairs
"""
Easy straight forward problem. Just use a hash map and find any values
that have an odd number of values.
"""

from collections import defaultdict


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        counts: dict[int, int] = defaultdict(int)
        if len(nums) % 2 == 1:
            return False

        for val in nums:
            counts[val] += 1

        for _, count in counts.items():
            if count % 2 == 1:
                return False

        return True


if __name__ == "__main__":
    test_case_1 = [3, 2, 3, 2, 2, 2]  # true
    test_case_2 = [4, 3, 2, 1]  # false

    cls = Solution()
    ans = cls.divideArray(test_case_2)
    print("------")
    print(ans)
