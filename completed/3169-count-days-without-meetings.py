# https://leetcode.com/problems/count-days-without-meetings
"""
Seems like a fairly straightforward problem where we need to merge intervals
to solve the problem. My first solution works but was hitting TLE, the alternative
solution is able to meet the constraints though and more efficient.

It bypasses the need for creating an extra merged array by just looking at the gaps
when iterating through the sorted meetings array.
"""

from typing import TypedDict


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        res = 0

        # Sort the meetings based on start times
        meetings.sort(key=lambda x: x[0])

        # Create a list for the merged intervals
        merged: list[list[int]] = []
        curr = list(meetings[0])
        for i in range(1, len(meetings)):
            start, end = meetings[i]

            # When we have an overlap, expand the curr end time
            if curr[1] >= start:
                curr[1] = max(end, curr[1])

            # When there is no overlap
            else:
                merged.append(curr)
                curr = list(meetings[i])

        if (len(merged) == 0) or (len(merged) > 0 and merged[-1] != curr):
            merged.append(curr)

        merged_index = 0
        for day in range(1, days + 1):
            for i in range(merged_index, len(merged)):
                start, end = merged[i]

                # Condition for having overlap
                if start <= day <= end:
                    res += 1
                    merged_index = i
                    break

        return days - res

    def countDaysV2(self, days: int, meetings: list[list[int]]) -> int:
        free_days = 0
        latest_end = 0

        # Sort meetings based on starting times
        meetings.sort()

        for start, end in meetings:
            # Add current range of days without a meeting
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            # Update latest meeting end
            latest_end = max(latest_end, end)

        # Add all days after the last day of meetings
        free_days += days - latest_end

        return free_days


class TestCaseType(TypedDict):
    days: int
    meetings: list[list[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "days": 10,
        "meetings": [[5, 7], [1, 3], [9, 10]],
    }  # 2

    test_case_2: TestCaseType = {
        "days": 5,
        "meetings": [[2, 4], [1, 3]],
    }  # 1

    test_case_3: TestCaseType = {
        "days": 57,
        "meetings": [
            [3, 49],
            [23, 44],
            [21, 56],
            [26, 55],
            [23, 52],
            [2, 9],
            [1, 48],
            [3, 31],
        ],
    }  # 1

    cls = Solution()
    ans = cls.countDays(**test_case_3)
    print("-----")
    print(ans)
