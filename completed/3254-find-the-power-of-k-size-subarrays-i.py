# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i
"""
My mind initutively went to approaching this as a sliding window problem. At the worst possible
case, this algorithm could produce a time complexity of O(n^2) since we are performing a subarray
check for each subarray. However, I tried to be clever and prevent this second check by using the
results from the previous answer. The secondary linear scan happens within [is_valid].

However, this problem could be quite simple if you think of just scanning throgh the list one time
and keeping a running count of valid subarrays, the code below is O(n)

```python
    def resultsArray(self, nums, k):
        if k == 1:
            return nums  # If k is 1, every single element is a valid subarray

        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1  # Count of consecutive elements

        for index in range(length - 1):
            if nums[index] + 1 == nums[index + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1  # Reset count if not consecutive

            # If we have enough consecutive elements, update the result
            if consecutive_count >= k:
                result[index - k + 2] = nums[index + 1] # <-- this logic was a little tricky to understand

        return result
```
"""

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res_len = n - k + 1
        res = [-1] * res_len

        for i in range(res_len):
            subarray = nums[i : i + k]
            if len(subarray) == 1:
                res[i] = subarray[0]
            elif i == 0 and self.is_valid(subarray):
                res[i] = subarray[-1]
            else:
                # If the previous response was valid and the next value is greater
                # than the previous window's value, we can use that next value as our answer
                if res[i - 1] != -1 and subarray[-1] == res[i - 1] + 1:
                    res[i] = subarray[-1]
                elif res[i - 1] == -1 and self.is_valid(subarray):
                    res[i] = subarray[-1]

        return res

    def is_valid(self, array):
        prev = None
        for val in array:
            if prev is None:
                prev = val
                continue

            if val != prev + 1:
                return False

            prev = val
        return True


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 2, 3, 4, 3, 2, 5],
        "k": 3,
    }  # [3,4,-1,-1,-1]

    test_case_2 = {
        "nums": [3, 2, 3, 2, 3, 2],
        "k": 2,
    }  # [-1,3,-1,3,-1]
    test_case_3 = {
        "nums": [9, 2],
        "k": 1,
    }  # [9, 2]
    test_case_4 = {
        "nums": [1, 3, 4],
        "k": 2,
    }  # [-1,4]
    test_case_5 = {
        "nums": [5, 6, 27],
        "k": 2,
    }  # [6,-1]

    cls = Solution()
    ans = cls.resultsArray(**test_case_5)
    print("-----")
    print(ans)
