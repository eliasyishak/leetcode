# https://leetcode.com/problems/trapping-rain-water/description/
"""
I did this problem as a follow up of https://leetcode.com/problems/trapping-rain-water-ii

This helps me understand on a 2D level what I described in 407-trapping-rain-water-ii.py
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        # Define the max values encountered from the left and right
        # for each index in two separate lists
        left_maxes: List[int] = [0 for _ in range(n)]
        right_maxes: List[int] = [0 for _ in range(n)]
        for i in range(n):
            left = i
            right = (n - 1) - i

            if i > 0:
                left_maxes[left] = max(height[left - 1], left_maxes[left - 1])
                right_maxes[right] = max(height[right + 1], right_maxes[right + 1])

        for i in range(n):
            if height[i] < min(left_maxes[i], right_maxes[i]):
                res += min(left_maxes[i], right_maxes[i]) - height[i]

        return res


if __name__ == "__main__":
    test_case_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    test_case_2 = [4, 2, 0, 3, 2, 5]  # 9

    cls = Solution()
    ans = cls.trap(test_case_2)
    print("------")
    print(ans)
