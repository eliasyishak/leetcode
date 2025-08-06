# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference
"""
Once you sort the list, you are guaranteeing that the nearby elements
have the smallest difference between each other. For each chunk of 3 elements
you just need to ensure that the first and last elements don't have a difference
that is greater than k.
"""

from typing import TypedDict


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res: list[list[int]] = []
        for i in range(n // 3):
            curr = [
                nums[3 * i],
                nums[3 * i + 1],
                nums[3 * i + 2],
            ]

            if curr[2] - curr[0] > k:
                return []

            res.append(curr)

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        nums: list[int]
        k: int

    test_case_1: TestCase = {
        "nums": [1, 3, 4, 8, 7, 9, 3, 5, 1],
        "k": 2,
    }  #  [[1,1,3],[3,4,5],[7,8,9]]

    cls = Solution()
    ans = cls.divideArray(**test_case_1)
    print("------")
    print(ans)
