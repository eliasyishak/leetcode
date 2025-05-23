# https://leetcode.com/problems/house-robber
"""
Good problem where we use a dynamic programming approach along with
making a choice. If we did not do it with dynamic programming, we would need
to essentially implement a backtracking solution that checks each possible
option for each house.
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        if len(nums) <= 2:
            return max(nums)

        # Initialize the first two elements in the dp array
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # We need to choose either one that is valid

        for i in range(2, n):
            dp[i] = max(
                nums[i] + dp[i - 2],
                dp[i - 1],
            )

        return dp[-1]


if __name__ == "__main__":
    test_case_1 = [1, 2, 3, 1]  # 4
    test_case_2 = [2, 7, 9, 3, 1]  # 12
    test_case_3 = [2, 1, 1, 2]  # 4

    cls = Solution()
    ans = cls.rob(test_case_3)
    print("-------")
    print(ans)
