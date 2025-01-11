# https://leetcode.com/problems/rotate-array
"""
Input: [1, 2, 3, 4, 5, 6, 7] k = 3

You can reverse the list so you have
[7, 6, 5, 4, 3, 2, 1]
 ^-----^  ^--------^

Now all you have to do here is reverse the two
parts above, you reverse the first k elements in place
and then the next N - k elements separately.

Again, feels like a "trick" you have to know and less about the
algorithm itself. If we wanted to use extra space to solve this, then
this becomes a very trivial problem.

I went too far down with using a for loop and trying to get the math
right, much much easier to use while loops.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse_inplace(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # First reverse the entire list
        reverse_inplace(left=0, right=n - 1)

        # Reverse the first k elements in the list now
        reverse_inplace(left=0, right=k - 1)

        # Reverse the left over n - k elements
        reverse_inplace(left=k, right=n - 1)

    def rotateSlow(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for _ in range(k % n):
            last = nums[-1]
            for i in range(n):
                temp = nums[i]
                nums[i] = last
                last = temp

        print(nums)


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 2, 3, 4, 5, 6, 7],
        "k": 3,
    }  # [5, 6, 7, 1, 2, 3, 4]

    cls = Solution()
    cls.rotate(**test_case_1)
