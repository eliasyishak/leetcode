# https://leetcode.com/problems/continuous-subarrays
"""
Good two pointer/sliding window problem that can be easily understood once
you understand that incrementing the right pointer to a valid substring

For example, let's assume that nums = [5, 4, 3] and that we currently have
the first two items in our subarray [5, 4]; we have already confirmed that these two
are valid since 5 - 4 <= 2  at this point, we have 3 valid subarrays, [5], [4], and [5, 4]

Next we increment the right index so that our subarray is now [5, 4, 3];
we will be adding (right - left + 1) subarrays. You can think of this as adding
[3], [4, 3], and [5, 4, 3] to our initial 3 valid subarrays. This gives us a total of 6 valid
subarrays
"""

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = right = 0
        count_obj = {}
        subarray_counts = 0

        while right < len(nums):
            if nums[right] not in count_obj:
                count_obj[nums[right]] = 0

            count_obj[nums[right]] += 1

            # If the current window is not valid, we will move the left
            # pointer to the right
            #
            # Note, I wanted to initially set a left_val variable at the top of the
            # while loop but we can't really do that unless we also reset it in this
            # while loop to update that variable
            while max(count_obj) - min(count_obj) > 2:
                count_obj[nums[left]] -= 1
                if count_obj[nums[left]] == 0:
                    del count_obj[nums[left]]
                left += 1

            # Once we have validated that our window is valid, we can determine
            # how many valid subarrays by taking the difference between the left
            # and right index (+ 1)
            subarray_counts += right - left + 1
            right += 1

        return subarray_counts


if __name__ == "__main__":
    test_case_1 = [
        5,
        4,
        2,
        4,
    ]  # 8
    test_case_2 = [65, 66, 67, 66, 66, 65, 64, 65, 65, 64]  # 43

    cls = Solution()
    ans = cls.continuousSubarrays(nums=test_case_2)
    print("----")
    print(ans)
