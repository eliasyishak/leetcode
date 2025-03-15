# https://leetcode.com/problems/house-robber-iv
"""
Another good binary search problem that should be attempted to
do in a linear fashion until you reach the TLE. I originally had the
current_max variable getting incremented linearly but the optimization of
doing it in a binary search fashion makes it much faster to converge on
a solution.

The key part of this problem is understanding that if you rob k houses [house_1, house_2, ..., house_k]
that house_k is the variable you want to search for. Once you have that variable
set, you can simply iterate through the entire array looking for any houses
that have less than house_k for the condition.

The binary search condition will be if we actually were able to rob k houses with
having house_k as the max.
"""

from typing import TypedDict


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        # Create a sorted list of nums so that we can get the kth
        # smallest element which will be what we greedly try to solve
        # for; we take the kth smallest because we need to rob at minimum
        # k houses
        sorted_nums = sorted(nums)

        res = sorted_nums[-1]
        lower_bound = sorted_nums[k - 1]
        upper_bound = sorted_nums[-1]

        while lower_bound <= upper_bound:
            current_max = (lower_bound + upper_bound) // 2

            houses_robbed = 0

            # Now that we have our current max, we will try to "rob" from
            # homes that have current_max or less money while skipping the
            # next house if we do rob
            index = 0
            while index < len(nums):
                if nums[index] <= current_max:
                    houses_robbed += 1
                    index += 2
                else:
                    index += 1

            # If we met our constraint, we could possibly reduce the current_max
            # for a smaller value by searching the left space
            if houses_robbed >= k:
                res = min(res, current_max)
                upper_bound = current_max - 1
            else:
                lower_bound = current_max + 1

        return res


class TestCaseType(TypedDict):
    nums: list[int]
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [2, 3, 5, 9],
        "k": 2,
    }  # 5

    test_case_2: TestCaseType = {
        "nums": [2, 7, 9, 3, 1],
        "k": 2,
    }  # 2

    cls = Solution()
    ans = cls.minCapability(**test_case_2)
    print("-----")
    print(ans)
