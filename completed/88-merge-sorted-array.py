"""
"nums1": [1, 2, 3, 0, 0, 0],
"nums2": [2, 5, 6],

Processing nums1 one iteration at a time

Initially: [1, 2, 3, 0, 0, 0]

1.         [1, 2, 3, 0, 0, 6]
2.         [1, 2, 3, 0, 5, 6]
3.         [1, 2, 3, 3, 5, 6]
4.         [1, 2, 2, 3, 5, 6]

"""

from typing import List, TypedDict


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums2) == 0:
            return

        last_index = m + n - 1

        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index] = nums2[n - 1]
                n -= 1

            last_index -= 1


class TestCase(TypedDict):
    nums1: List[int]
    m: int
    nums2: List[int]
    n: int


if __name__ == "__main__":
    test_case_1: TestCase = {
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
    }

    cls = Solution()
    cls.merge(**test_case_1)
