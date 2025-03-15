# https://leetcode.com/problems/zero-array-transformation-ii
"""
This solution was a tough one to figure out but the trick was to
use a differences array where you keep track of a when the value
at an index goes up.

For example: nums = [2, 0, 2] and queries = [0, 1, 1]

Then you would have a difference array = [1, 0, -1], you can then
get the prefix sum of this array to be prefix = [1, 1, 0], this means
that we have added 1 to indices 0 and 1.

Furthermore, I took the approach of doing all of the iterations in one
pass and storing them in a hashmap. This results in a memory limit exceeded
but I like this solution so I'm keeping it :)

The alternative that would have worked is to the same thing above but do it
with binary search where we search the queries.
"""

from typing import TypedDict


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        if set(nums) == set([0]):
            return 0

        # Dictionary that holds the prefix sum array at
        # each query
        prefix_obj: dict[int, list[int]] = {}

        # Difference array that will keep track of the update values
        # for the prefix array
        differences = [0] * len(nums)

        for query_index, (left, right, val) in enumerate(queries):
            differences[left] += val

            # We have to reset the val AFTER the right
            # boundary
            if right + 1 < len(nums):
                differences[right + 1] -= val

            prefix = [0] * len(nums)
            for i, val in enumerate(differences):
                if i == 0:
                    prefix[i] = val
                else:
                    prefix[i] = prefix[i - 1] + val

            prefix_obj[query_index] = list(prefix)

        # Iterate through the prefix object and check each
        # position in nums, if we find that we don't meet the value
        # in nums, continue to the next prefix sum from the same value
        current_index = 0
        for query_index, prefix in prefix_obj.items():
            while (
                current_index < len(nums)
                and nums[current_index] <= prefix[current_index]
            ):
                current_index += 1

            if current_index == len(nums):
                return query_index + 1

        return -1


class TestCaseType(TypedDict):
    nums: list[int]
    queries: list[list[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [2, 0, 2],
        "queries": [[0, 2, 1], [0, 2, 1], [1, 1, 3]],
    }  # 2

    test_case_2: TestCaseType = {
        "nums": [4, 3, 2, 1],
        "queries": [[1, 3, 2], [0, 2, 1]],
    }  # -1

    test_case_3: TestCaseType = {
        "nums": [5],
        "queries": [[0, 0, 5], [0, 0, 1], [0, 0, 3], [0, 0, 2]],
    }  # 1

    test_case_4: TestCaseType = {
        "nums": [10],
        "queries": [
            [0, 0, 5],
            [0, 0, 3],
            [0, 0, 2],
            [0, 0, 1],
            [0, 0, 4],
            [0, 0, 1],
            [0, 0, 4],
            [0, 0, 5],
            [0, 0, 3],
            [0, 0, 4],
            [0, 0, 1],
        ],
    }  # 3

    cls = Solution()
    ans = cls.minZeroArray(**test_case_1)
    print("------")
    print(ans)
