# https://leetcode.com/problems/zero-array-transformation-iii
"""
Very tough problem for me, seems like the key take away here is to be able
to identify queries that are valid for the current values and then use
a heap to choose the queries that go out the furtherest.

I looped back around and found a video that did a great job at explaining this
concept (https://www.youtube.com/watch?v=7jNS2hoM8Yw&t=1862s&ab_channel=Techdose)

The idea here is to use 2 heaps (max and a min heap) to keep track of what we have
available to us for each index. The max heap will store the queries we have available
to select from and the min heap is what we will use to keep track of the currently
active queries for that timeframe.
"""

from heapq import heappop, heappush
from typing import List, TypedDict


class Solution:
    def maxRemovalLC(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        The leetcode solution
        """
        queries.sort(key=lambda x: x[0])
        heap: list[int] = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]

            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1

            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1

            if operations < num:
                return -1

        return len(heap)

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        available_heap: list[int] = []  # max heap on end
        used_heap: list[int] = []  # min heap on end
        j = 0  # index for queries
        n = len(nums)

        for i in range(n):
            # Add all of the end queries to the available heap
            while j < len(queries) and queries[j][0] == i:
                heappush(available_heap, -queries[j][1])
                j += 1

            # First check if we have any available queries we can use
            # to turn the current index in nums to zero
            nums[i] -= len(used_heap)

            # If we still haven't turned nums[i] to zero, we can attempt
            # to use what is available
            while nums[i] > 0 and len(available_heap) > 0 and -available_heap[0] >= i:
                heappush(used_heap, -available_heap[0])
                heappop(available_heap)
                nums[i] -= 1

            # If we have not turned nums[i] to 0, then it is not possible
            if nums[i] > 0:
                return -1

            # We need to now remove any used queries that are no longer valid
            #
            # This step is very important!
            while len(used_heap) > 0 and used_heap[0] <= i:
                heappop(used_heap)

        return len(available_heap)


if __name__ == "__main__":

    class TestCaseType(TypedDict):
        nums: List[int]
        queries: List[List[int]]

    test_case_1: TestCaseType = {
        "nums": [2, 0, 2],
        "queries": [[0, 2], [0, 2], [1, 1]],
    }  # 1

    test_case_2: TestCaseType = {
        "nums": [1, 1, 1, 1],
        "queries": [[1, 3], [0, 2], [1, 3], [1, 2]],
    }  # 2

    test_case_3: TestCaseType = {
        "nums": [1, 2, 3, 4],
        "queries": [[0, 3]],
    }  # -1

    test_case_4: TestCaseType = {
        "nums": [1, 2],
        "queries": [[1, 1], [0, 0], [1, 1], [1, 1], [0, 1], [0, 0]],
    }  # 4

    test_case_5: TestCaseType = {
        "nums": [1, 3],
        "queries": [[0, 1], [0, 1]],
    }  # -1

    test_case_6: TestCaseType = {
        "nums": [3, 2],
        "queries": [[0, 1], [0, 1], [0, 1]],
    }  # 0

    test_case_7: TestCaseType = {
        "nums": [0, 0, 1, 1, 0],
        "queries": [[3, 4], [0, 2], [2, 3]],
    }  # 2

    cls = Solution()
    ans = cls.maxRemoval(**test_case_7)
    print("------")
    print(ans)
