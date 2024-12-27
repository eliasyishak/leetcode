# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target
"""
Simple problem to think about when using two pointers. The problem statement mentions
that for a pair (i, j), j > i but it doesn't really matter since the sum of (i, j) is the
same as (j, i)

Also you won't be incrementing by one when you find a match, instead you will be adding
all the possible pairs

For example: [-1, 1, 2, 3, 1] sorts to [-1, 1, 1, 2, 3]

The first and last items in the sorted array (-1, 3) sum to 2 which breaks our condition.
This means we attempt to make the sum smaller by decrementing the right pointer

Now we have (-1, 2) which is valid. But you'll also notice that (-1, 1), (-1, 1) (TWICE) are valid

So if you take the right index (3) and the left index (0), you can take their differences to get
all the elements between them that can be used form a pair with index 0.

In summary, if you have a sorted list and sum(nums[i], nums[j]) < target, then every index before
j is also valid
"""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            left_val = nums[left]
            right_val = nums[right]

            if left_val + right_val >= target:
                right -= 1
            else:
                res += right - left
                left += 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "nums": [-1, 1, 2, 3, 1],
        "target": 2,
    }  # 3

    cls = Solution()
    ans = cls.countPairs(**test_case_1)
    print("----")
    print(ans)
