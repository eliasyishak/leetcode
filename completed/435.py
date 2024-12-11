# https://leetcode.com/problems/non-overlapping-intervals
"""
Sorting does a lot magic here, it's good to visualize this before
attempting to solve it. We want to take a greedy approach after we
have sorted the array. The key concept to understand here is deciding which
interval to continue with for comparison once we encounter intervals that overlap
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by the start times of each interval
        intervals.sort(key=lambda x: (x[0], x[1]))

        result = 0
        prevEnd = intervals[0][-1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                # We want to make the prevEnd variable equal to the interval
                # with the ealier end because it is less likely for an overlap
                # given that the input list has been sorted
                prevEnd = min(end, prevEnd)

        return result


if __name__ == "__main__":
    test_case_1 = [
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 3],
    ]  # 1

    test_case = test_case_1
    cls = Solution()
    ans = cls.eraseOverlapIntervals(intervals=test_case)
    print("------")
    print(ans)
