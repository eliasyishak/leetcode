# https://leetcode.com/problems/count-the-number-of-good-subarrays
"""
The key to this problem is to use a two pointer sliding window
approach. The left pointer will initially remain anchored while the right pointer
seeks to the right until it has met the condition; having k pairs in the subarray.

Once you have a valid subarray, everything to the right is also a valid subarray as well.
"""

from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        freq: dict[int, int] = defaultdict(int)
        equal_pairs = 0
        left = right = 0
        n = len(nums)
        res = 0
        while left < n:
            # Continue to seek to the right until we have a valid subarray
            while right < n and equal_pairs < k:
                freq[nums[right]] += 1

                if freq[nums[right]] > 1:
                    equal_pairs += freq[nums[right]] - 1

                right += 1

            if equal_pairs >= k:
                res += (
                    n - right + 1
                )  # Need to add 1 more since we are past the exit condition

            freq[nums[left]] -= 1
            # Removing one item removes all of the pairs it made with
            # that removed item
            if freq[nums[left]] > 0:
                equal_pairs -= freq[nums[left]]
            left += 1

        return res
