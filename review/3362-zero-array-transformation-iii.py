# https://leetcode.com/problems/zero-array-transformation-iii
"""
Very tough problem for me, seems like the key take away here is to be able
to identify queries that are valid for the current values and then use
a heap to choose the queries that go out the furtherest.
"""

from heapq import heappop, heappush
from typing import List, TypedDict


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
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
    ans = cls.maxRemoval(**test_case_1)
    print("------")
    print(ans)
