# https://leetcode.com/problems/sort-colors
"""
Great problem for understanding how to perform a sorting algorithm
in place by seeking from a given index to the right.

I was stuck on this a bit because I was incorrectly seeking by starting
at `i` when I should have been seeking to the right of `swap_index` smh
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(set(nums)) == 1:
            return

        n = len(nums)
        for i in range(2):
            swap_index = 0
            while swap_index < n and nums[swap_index] <= i:
                swap_index += 1

            # Seek from the current swap index to the right
            # and find values to swap
            for j in range(swap_index + 1, n):
                if nums[j] == i:
                    nums[swap_index], nums[j] = nums[j], nums[swap_index]

                    swap_index += 1
                    while swap_index < n and nums[swap_index] <= i:
                        swap_index += 1


if __name__ == "__main__":
    test_case_1 = [2, 0, 2, 1, 1, 0]  # [0,0,1,1,2,2]
    test_case_2 = [2, 0, 1]  # [0,1,2]
    test_case_3 = [0, 0]  # [0,0]
    test_case_4 = [2, 1]  # [1,2]
    test_case_5 = [0, 1]  # [0,1]

    cls = Solution()
    cls.sortColors(test_case_4)
