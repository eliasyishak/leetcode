# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements
"""
The trick to this problem is to create "groups" of numbers that are within the limit
differences of each other and use those values to sort from high to low in the same positions
they were in the original list

For example, the test case 1 has the following groups

[[1, 3, 5], [8, 9]]

and we can use the index object to find where to place them where the key below is the index
and value is the group that it maps to

{
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 1,
}

"""

from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        temp = [(val, i) for i, val in enumerate(nums)]
        temp.sort()
        groups = []
        index_to_group = {}
        for i, (val, index) in enumerate(temp):
            if i == 0:
                groups.append(deque([val]))
            else:
                # Condition for extending last group
                if val - groups[-1][-1] <= limit:
                    groups[-1].append(val)
                else:
                    groups.append(deque([val]))

            index_to_group[index] = len(groups) - 1

        # Create the response list to be the same size
        print(index_to_group)
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = groups[index_to_group[i]].popleft()

        return res


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 5, 3, 9, 8],
        "limit": 2,
    }  # [1,3,5,8,9]

    cls = Solution()
    ans = cls.lexicographicallySmallestArray(**test_case_1)  # type: ignore
    print("----")
    print(ans)
