# https://leetcode.com/problems/number-of-ways-to-split-array
"""
Simple problem to solve with the use of a prefix and suffix sum array. We can
further optimize this problem if we wanted to and only use one of the sum arrays
if we wanted to.

And an even further optimization can get rid of the arrays entirely and use
variables to keep a running value

```python
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        # Keep track of sum of elements on left and right sides
        left_sum = right_sum = 0

        # Initially all elements are on right side
        right_sum = sum(nums)

        # Try each possible split position
        count = 0
        for i in range(len(nums) - 1):
            # Move current element from right to left side
            left_sum += nums[i]
            right_sum -= nums[i]

            # Check if this creates a valid split
            if left_sum >= right_sum:
                count += 1

        return count
```

Above we are able to simulate what the suffix sum array does for us by initially
setting the sum of the entire list to the right sum and decrement as we move forward.
"""

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [-1] * n
        suffix = [-1] * n

        for k in range(n):
            j = n - 1 - k

            if k == 0:
                prefix[k] = nums[k]
                suffix[j] = nums[j]
            else:
                prefix[k] = prefix[k - 1] + nums[k]
                suffix[j] = suffix[j + 1] + nums[j]

        res = 0
        for k in range(0, n - 1):
            if prefix[k] >= suffix[k + 1]:
                res += 1

        return res


if __name__ == "__main__":
    test_case_1 = [10, 4, -8, 7]  # 2
    test_case_2 = [0, 0]  # 1

    cls = Solution()
    ans = cls.waysToSplitArray(test_case_2)
    print("----")
    print(ans)
