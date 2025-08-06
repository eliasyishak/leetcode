# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array
"""
Not too bad of a problem, the important thing to consider is that you can do
this in one loop-ish. Find the key you are looking for in the main loop, and
then only add the indexes to the left and right of that index. There is probably
another optimization that can be made instead of using a set to check if a value
has been added.

You can probably intelligently set the left bounds based on what you know about
the largest index added already. But extra space is okay with me :)
"""

from typing import TypedDict


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        res: list[int] = []

        # Iterate through the list once and when we find
        # the key element, add all of the indexes to the
        # left and right (-k <= key_index <= k)
        n = len(nums)
        added: set[int] = set()
        for i, val in enumerate(nums):
            if val == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)

                for j in range(left, right + 1):
                    if j not in added:
                        res.append(j)
                        added.add(j)

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        nums: list[int]
        key: int
        k: int

    test_case_1: TestCase = {
        "nums": [3, 4, 9, 1, 3, 9, 5],
        "key": 9,
        "k": 1,
    }  # [1,2,3,4,5,6]

    test_case_2: TestCase = {
        "nums": [2, 2, 2, 2, 2],
        "key": 2,
        "k": 2,
    }  # [0,1,2,3,4]

    cls = Solution()
    result = cls.findKDistantIndices(**test_case_2)
    print("------")
    print(result)
