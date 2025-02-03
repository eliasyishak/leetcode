# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
"""
Not too difficult of a problem if you think about how iterating just one time and keeping track
of the longest increasing and decreasing subarrays at the same time.

If not, you could probably get away with iterating twice and checking for both increasing and
decreasing conditions separately, it will just be O(2n) which is O(n) in the end.
"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1

        curr_inc = 1
        curr_dec = 1

        prev = nums[0]
        for i, val in enumerate(nums):
            if i == 0:
                continue

            # Handle the increasing case
            if val > prev:
                curr_inc += 1
            else:
                curr_inc = 1

            # Handle the decresaing case
            if val < prev:
                curr_dec += 1
            else:
                curr_dec = 1

            increasing = max(increasing, curr_inc)
            decreasing = max(decreasing, curr_dec)
            prev = val

        return max(increasing, decreasing)


if __name__ == "__main__":
    test_case_1 = [1, 4, 3, 3, 2]  # 2
    test_case_2 = [3, 2, 1]  # 3

    cls = Solution()
    ans = cls.longestMonotonicSubarray(test_case_2)
    print("-----")
    print(ans)
