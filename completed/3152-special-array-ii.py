# https://leetcode.com/problems/special-array-ii
from typing import List

"""
Not too bad of a problem. I took the approach of finding spots in the
nums array where we had mistakes and kept a rolling count as we iterated
through the list.

Then you can use the query's start and end index and see if there was a mistake
in the subarray by finding the difference between mistakes. If the end index has
a greater count of mistakes than the start, that means there was a mistake we encountered.
"""


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Define a list of the same length as nums where which list
        # item is the number of "mistakes" that have occured up to that
        # index
        mistakes = [0 for _ in range(len(nums))]
        for i, val in enumerate(nums):
            if i == 0:
                continue

            if val % 2 == nums[i - 1] % 2:
                mistakes[i] = mistakes[i - 1] + 1
            else:
                mistakes[i] = mistakes[i - 1]

        ans = [None for _ in range(len(queries))]
        for j, (start, end) in enumerate(queries):
            ans[j] = mistakes[end] == mistakes[start]

        return ans


if __name__ == "__main__":
    test_case_1 = {
        "nums": [3, 4, 1, 2, 6],
        "queries": [[0, 4]],
    }  # [false]

    test_case_2 = {
        "nums": [4, 3, 1, 6],
        "queries": [[0, 2], [2, 3]],
    }  # [false,true]

    test_case = test_case_2
    cls = Solution()
    ans = cls.isArraySpecial(nums=test_case["nums"], queries=test_case["queries"])
    print("----")
    print(ans)
