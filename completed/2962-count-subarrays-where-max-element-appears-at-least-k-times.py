# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
"""
Good problem for understanding how to implement the sliding window approach with
different conditions for shrinking and expanding the window. The key here is to
remember that once you have enough in curr_count, you need to collect all of the subarrays
to the right as well since they are also valid.
"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        max_value = max(nums)

        res = 0
        left = 0
        right = 0
        curr_count = 0
        for right in range(n):
            # Add element at right to our window
            if nums[right] == max_value:
                curr_count += 1

            # Once we have k occurrences, count subarrays and then shrink window from left
            # until we have fewer than k occurrences
            while curr_count >= k:
                # All subarrays starting at left and ending at positions right-1, right, ..., n-1 are valid
                res += n - (right - 1)

                # Shrink window from left
                if nums[left] == max_value:
                    curr_count -= 1
                left += 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 3, 2, 3, 3],
        "k": 2,
    }  # 6

    test_case_2 = {
        "nums": [1, 4, 2, 1],
        "k": 3,
    }  # 6

    cls = Solution()
    ans = cls.countSubarrays(**test_case_1)
    print("------")
    print(ans)
