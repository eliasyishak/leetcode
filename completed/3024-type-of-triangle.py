# https://leetcode.com/problems/type-of-triangle
"""
equilateral - all sides equal
isosceles   - two sides equal
scalene     - no sides equal

Property of a triangle = any 2 sides summed up > 1 other side
"""

from typing import Literal


class Solution:
    def triangleType(
        self, nums: list[int]
    ) -> Literal["equilateral", "scalene", "isosceles", "none"]:
        nums.sort()
        num_set = set(nums)
        if len(num_set) == 1:
            return "equilateral"

        if len(num_set) == 2 and nums[0] + nums[1] > nums[2]:
            return "isosceles"

        if nums[0] + nums[1] > nums[2]:
            return "scalene"

        return "none"


if __name__ == "__main__":
    test_case_1 = [3, 3, 3]  # equilateral
    test_case_2 = [3, 4, 5]  # scalene

    cls = Solution()
    ans = cls.triangleType(test_case_2)
    print("------")
    print(ans)
