# https://leetcode.com/problems/two-best-non-overlapping-events
"""
Didn't really understand this one
"""

from typing import List
import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Order the events based on their start times
        events.sort(key=lambda x: x[0])
        print(events)
        max_val = 0
        max_sum = 0
        pq = []

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum


if __name__ == "__main__":
    test_case_1 = [
        [1, 3, 2],
        [4, 5, 2],
        [2, 4, 3],
    ]  # 4

    test_case = test_case_1

    cls = Solution()
    ans = cls.maxTwoEvents(events=test_case)
    print("----")
    print(ans)
