# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
"""
If the list has been rotated, then we only need to find the pivot point
at which the list should be starting and recreate the list and check if
the list is still in sorted order.
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # Attempt to find the pivot point; where the numbers are not ascending
        #
        # If we fail to find a point where the numbers decrease then we can assume
        # that the array is sorted
        pivot = -1
        for i, val in enumerate(nums):
            if i == 0:
                prev = val
            else:
                if val < prev:
                    pivot = i
                    break
                prev = val

        if pivot == -1:
            return True

        # Create the new list from the pivot point and check if the new list
        # is in sorted condition
        new = nums[pivot:] + nums[0:pivot]
        for i, val in enumerate(new):
            if i == 0:
                prev = val
            else:
                if val < prev:
                    return False
                prev = val

        return True


if __name__ == "__main__":
    test_case_1 = [3, 4, 5, 1, 2]  # true
    test_case_2 = [1, 2, 3]  # true
    test_case_3 = [2, 1, 3, 4]  # false

    cls = Solution()
    ans = cls.check(test_case_3)
    print("------")
    print(ans)
