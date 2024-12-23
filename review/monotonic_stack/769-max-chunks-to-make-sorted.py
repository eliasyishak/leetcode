# https://leetcode.com/problems/max-chunks-to-make-sorted
"""
Seems like there are several ways to approach this problem, my approach uses extra space
with two sets. There is one set that contains all of the values we need and another that
contains all of the values we have seen. If the intersection matches identifically, then we have
all the values we need for that subarray

The below approach is simple enough to understand
```python
class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        chunks = 0
        max_element = 0

        # Iterate over the array
        for i in range(n):
            # Update max_element
            max_element = max(max_element, arr[i])

            if max_element == i:
                # All values in range [0, i] belong to the prefix arr[0:i]; a chunk can be formed
                chunks += 1

        return chunks
```
For example, assume we have [1, 2, 0, 3, 4] as our arr

    If we have the subarray [1, 2], our max value is = 2
    However, if it was a valid subarray with a max of 2, we would need subarray [0, 1, 2] so [1, 2] is not valid

    [1, 2, 0] is however valid because a subarray with a max value of 2 needs 2 + 1 length for the subarray

    max_value = i needs a subarray of length = i + 1
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        left = right = 0
        count = 0
        seen = set()
        need = set()
        while right < len(arr):
            need.add(right)
            seen.add(arr[right])

            # If we have a valid subarray, the two sets will be identical
            if len(seen.intersection(need)) == len(seen) == len(need):
                count += 1
                left = right + 1
                right = left

                seen.clear()
                need.clear()
            else:
                right += 1

        return count


if __name__ == "__main__":
    test_case_1 = [4, 3, 2, 1, 0]  # 1
    test_case_2 = [1, 0, 2, 3, 4]  # 4

    cls = Solution()
    ans = cls.maxChunksToSorted(arr=test_case_2)
    print("-----")
    print(ans)
