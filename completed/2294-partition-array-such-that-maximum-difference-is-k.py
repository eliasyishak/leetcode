# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k
"""
This problem tries to be a little tricky by saying that you have to find the
subsequences that satisfy the condition. You don't really need to keep the valid
subsequences in the same order, so by sorting, you know the minimum value of a given
subsequence, and once you find a value that is going to be greater than k, you can
increment the number of sequences we would need.
"""

from typing import TypedDict


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prev = nums[0]
        res = 1
        for i in range(1, n):
            if nums[i] - prev > k:
                res += 1

                # You have to only set prev within this conditional because
                # subsequence needs to include the smallest val in the subsequence
                prev = nums[i]

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        nums: list[int]
        k: int

    test_case_1: TestCase = {
        "nums": [3, 6, 1, 2, 5],
        "k": 2,
    }  # 2

    cls = Solution()
    ans = cls.partitionArray(**test_case_1)
    print("------")
    print(ans)
