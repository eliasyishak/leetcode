# https://leetcode.com/problems/target-sum/?envType=daily-question&envId=2024-12-26
"""
This is pretty straightforward DFS algorithm that uses a cache for dynamically
storing the results for the inputs into the helper function

The cache uses the input parameters as the lookup key instead of the path string
of the values because each of the paths will be unique. What is not unique is their
current sum up until a given index in `nums`.

Take the below for example, we encountered the first combination once already so if we
use the computed value for that input of (index=4, cur_sum=4), we can save ourselves more
recursive computations.

curr_str (index, cur_sum)
+1+2+2-1 (4, 4)
-1+2+2+1 (4, 4)

+1+2-2 (3, 1)
+1-2+2 (3, 1)

Full print out
 (0, 0)
+1 (1, 1)
+1+2 (2, 3)
+1+2+2 (3, 5)
+1+2+2+1 (4, 6)
+1+2+2+1+3 (5, 9)
+1+2+2+1-3 (5, 3)
+1+2+2-1 (4, 4)
+1+2+2-1+3 (5, 7)
+1+2+2-1-3 (5, 1)
+1+2-2 (3, 1)
+1+2-2+1 (4, 2)
+1+2-2+1+3 (5, 5)
+1+2-2+1-3 (5, -1)
+1+2-2-1 (4, 0)
+1+2-2-1+3 (5, 3)
+1+2-2-1-3 (5, -3)
+1-2 (2, -1)
+1-2+2 (3, 1)
+1-2-2 (3, -3)
+1-2-2+1 (4, -2)
+1-2-2+1+3 (5, 1)
+1-2-2+1-3 (5, -5)
+1-2-2-1 (4, -4)
+1-2-2-1+3 (5, -1)
+1-2-2-1-3 (5, -7)
-1 (1, -1)
-1+2 (2, 1)
-1+2+2 (3, 3)
-1+2+2+1 (4, 4)
-1+2+2-1 (4, 2)
-1+2-2 (3, -1)
-1+2-2+1 (4, 0)
-1+2-2-1 (4, -2)
-1-2 (2, -3)
-1-2+2 (3, -1)
-1-2-2 (3, -5)
-1-2-2+1 (4, -4)
-1-2-2-1 (4, -6)
-1-2-2-1+3 (5, -3)
-1-2-2-1-3 (5, -9)
"""

from typing import List


class Solution:
    def __init__(self):
        self.cache = {}
        self.ops = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(index, curr_sum, curr_str) -> int:
            print(curr_str, (index, curr_sum))
            if (index, curr_sum) in self.cache:
                return self.cache[(index, curr_sum)]

            self.ops += 1
            if index == len(nums):
                return 1 if curr_sum == target else 0

            res = helper(
                index + 1,
                curr_sum + nums[index],
                curr_str=f"{curr_str}+{nums[index]}",
            ) + helper(
                index + 1,
                curr_sum - nums[index],
                curr_str=f"{curr_str}-{nums[index]}",
            )
            self.cache[(index, curr_sum)] = res

            return res

        return helper(0, 0, "")


if __name__ == "__main__":
    test_case_1 = {
        "nums": [1, 1, 1, 1, 1],
        "target": 3,
    }  # 5
    test_case_2 = {
        "nums": [1, 2, 2, 1, 3],
        "target": 5,
    }  # 3
    test_case_3 = {
        "nums": [
            35,
            42,
            34,
            22,
            35,
            39,
            35,
            44,
            33,
            48,
            46,
            18,
            4,
            39,
            1,
            50,
            28,
            43,
            15,
            37,
        ],
        "target": 36,
    }  # 5115

    cls = Solution()
    ans = cls.findTargetSumWays(**test_case_2)
    print("----")
    print(ans)
    print(f"Operations: {cls.ops}; disable the conditional to see how caching helps")
