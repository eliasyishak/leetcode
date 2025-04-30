# https://leetcode.com/problems/count-complete-subarrays-in-an-array
"""
Interesting problem that still implements the sliding window approach but
in this problem, it is better off to hold the left pointer static when seeking
to the right.

If you try to move the right pointer and lag the left pointer, you won't arrive
at a solution with the below algorithm.
"""

from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        unique = len(set(nums))
        n = len(nums)

        res = 0
        right = 0
        curr: dict[int, int] = defaultdict(int)

        for left in range(n):
            if left > 0:
                remove_val = nums[left - 1]
                curr[remove_val] -= 1
                if curr[remove_val] == 0:
                    del curr[remove_val]

            # Seek to the right to find the first index where the conditions
            # are met for the unique counts
            while right < n and len(curr) < unique:
                right_val = nums[right]
                curr[right_val] += 1
                right += 1

            # You can find all of the valid subarrays to right of "right" because it is gauranteed
            # we won't find any new values that have not been accounted for between left and right index
            if len(curr) == unique:
                res += n - right + 1

        return res

    def countCompleteSubarraysRightStatic(self, nums: list[int]) -> int:
        """
        This approach makes more sense to me with having the left index
        lagging behind
        """
        n = len(nums)
        distinct_count = len(set(nums))

        result = 0
        left = 0
        counter: dict[int, int] = defaultdict(int)

        for right in range(n):
            # Add the current element to our window
            counter[nums[right]] = counter.get(nums[right], 0) + 1

            # While our window has all distinct elements
            while len(counter) == distinct_count:
                # For this valid left position, count all possible valid subarrays
                result += n - right

                # Shrink window from left
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

        return result


if __name__ == "__main__":
    test_case_1 = [1, 3, 1, 2, 2]  # 4
    test_case_2 = [5, 5, 5, 5]  # 10

    cls = Solution()
    ans = cls.countCompleteSubarrays(test_case_1)
    print("------")
    print(ans)
