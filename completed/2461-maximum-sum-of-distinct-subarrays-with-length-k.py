# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
"""
Sliding window problem that has extra conditions on what allows the right side
to continue growing. Just a little tricky setting up the logic but conceptually,
it is pretty straightforward.
"""

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        res = 0
        curr_sum = 0
        num_set = set()
        while right < len(nums):
            curr_sum += nums[right]

            while right - left >= k or nums[right] in num_set:
                curr_sum -= nums[left]
                num_set.remove(nums[left])
                left += 1
            # Immediately add the number into the set; consider this a conditional where we are
            # checking to see if a key exists in a dictionary, if not present, add it after
            num_set.add(nums[right])

            # We can only check for a valid subarray sum if we have met the length k, we cannot
            # take the sum of a subarray smaller than length k
            if right - left + 1 == k:
                res = max(res, curr_sum)

            right += 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 5, 4, 2, 9, 9, 9],
        "k": 3,
    }  # 15
    test_case_2 = {
        "nums": [4, 4, 4],
        "k": 3,
    }  # 0

    cls = Solution()
    ans = cls.maximumSubarraySum(**test_case_1)
    print("-----")
    print(ans)
