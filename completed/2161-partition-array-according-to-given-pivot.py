# https://leetcode.com/problems/partition-array-according-to-given-pivot
"""
Simple problem. I tried to solve this without using extra space (outside of the
res variable). Still O(n) time complexity but a lot of redudant looping O(3n).

If we use extra space, we can solve this in one loop

```python
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        same = []

        for i in nums:
            if i > pivot:
                more.append(i)
            elif i < pivot:
                less.append(i)
            else:
                same.append(i)

        return less + same + more
```
"""

from typing import TypedDict


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n = len(nums)

        i = 0
        res = [0] * n

        # Handle the values before the pivot
        pivot_count = 0
        for val in nums:
            if val == pivot:
                pivot_count += 1
            elif val < pivot:
                res[i] = val
                i += 1
            else:
                pass

        # Handle the pivots
        for _ in range(pivot_count):
            res[i] = pivot
            i += 1

        # Handle the values after the pivot
        for val in nums:
            if val > pivot:
                res[i] = val
                i += 1

        return res


class TestCaseType(TypedDict):
    nums: list[int]
    pivot: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [9, 12, 5, 10, 14, 3, 10],
        "pivot": 10,
    }  # [9,5,3,10,10,12,14]

    cls = Solution()
    ans = cls.pivotArray(**test_case_1)
    print("-----")
    print(ans)
