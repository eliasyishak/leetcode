# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation
"""
A fun tricky problem, it is best to start out this problem by drawing it out and seeing
how things overlap. Once you have the intervals sorted, you can iterate through them
going right in the timeline. Keep track of the number of intervals the overlap while keeping
track of how far back we can go to maintain the "beauty" rule.

This can be thought of as a sliding window problem where the right index leads and the left
index lags.
"""

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        intervals = [(val - k, val + k) for val in nums]

        # You don't really need the curr variable here if you used
        # i and left to calculate the distance between them. This was just
        # more intuitve for me to understand by incrementing/decrementing
        # as operations were completed to show the window expanding
        result = 1
        curr = 1
        left = 0
        for i in range(1, len(nums)):
            while len(intervals) > 0 and intervals[left][1] < intervals[i][0]:
                left += 1
                curr -= 1

            curr += 1
            result = max(result, curr)

        return result


if __name__ == "__main__":
    test_case_1 = {
        "nums": [4, 6, 1, 2],
        "k": 2,
    }  # 3
    test_case_2 = {
        "nums": [1, 1, 1, 1],
        "k": 10,
    }  # 4

    test_case = test_case_1
    cls = Solution()
    ans = cls.maximumBeauty(k=test_case["k"], nums=test_case["nums"])
    print("----")
    print(ans)
