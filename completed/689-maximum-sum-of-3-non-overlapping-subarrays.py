# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays
"""
Very tough problem to solve if we want to optimize for time complexity. To do so, we would need
to find a way to cache the results from the dfs but it is a bit of a challenge because we are not
returning anything so it's tough to wrap your mind around it.
"""

from typing import List


class Solution:
    def __init__(self):
        self.res = (-float("inf"), [])

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = []
        for i in range(len(nums) - k + 1):
            subarray = nums[i : i + k]
            sums.append((sum(subarray), i))

        def dfs(index: int, starting_indices: List[int], curr_sum: int):
            if index >= len(sums) or len(starting_indices) == 3:
                if curr_sum > self.res[0]:
                    self.res = (curr_sum, starting_indices)
                return

            # Including the current index
            dfs(
                index=index + k,
                starting_indices=starting_indices + [sums[index][-1]],
                curr_sum=curr_sum + sums[index][0],
            )

            # Not including the current index
            dfs(
                index=index + 1,
                starting_indices=starting_indices,
                curr_sum=curr_sum,
            )

        dfs(0, [], 0)
        return self.res[-1]


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 2, 1, 2, 6, 7, 5, 1],
        "k": 2,
    }  # [0, 3, 5]

    test_case_2 = {
        "nums": [7, 13, 20, 19, 19, 2, 10, 1, 1, 19],
        "k": 3,
    }  # [1, 4, 7]

    cls = Solution()
    ans = cls.maxSumOfThreeSubarrays(**test_case_2)
    print("----")
    print(ans)
