# https://leetcode.com/problems/zero-array-transformation-i
"""
Example walk through of the first test case
[0, 0, 0, 0]

[0, 1, 0, 0] q=0
[1, 1, 0, -1] q=1 (notice that end is index 2 but we apply the update on the index after)

Prefix = [1, 2, 1, 0]


The key to this problem is computing a temporary list for the queries array before
creating the actual prefix array.  The editorial refers to this as a delta array. Also
important to note that have to one index after the end in the query since the bounds are
inclusive.
"""

from typing import TypedDict


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        delta: list[int] = [0] * len(nums)

        for start, end in queries:
            delta[start] += 1
            if end + 1 < len(nums):
                delta[end + 1] -= 1

        prefix = [0] * len(nums)
        for i, val in enumerate(delta):
            if i == 0:
                prefix[0] = val
            else:
                prefix[i] = prefix[i - 1] + val

        for i, prefix_sum in enumerate(prefix):
            if prefix_sum < nums[i]:
                return False

        return True


class TestCaseType(TypedDict):
    nums: list[int]
    queries: list[list[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [4, 3, 2, 1],
        "queries": [[1, 3], [0, 2]],
    }  # False

    test_case_2: TestCaseType = {
        "nums": [1, 0, 1],
        "queries": [[0, 2]],
    }  # True

    cls = Solution()
    ans = cls.isZeroArray(**test_case_1)
    print("------")
    print(ans)
