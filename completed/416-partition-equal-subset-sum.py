# https://leetcode.com/problems/partition-equal-subset-sum


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        # If sum is odd, it can't be divided into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # dp[i] = True if we can make sum i from the numbers
        dp = [False] * (target + 1)
        dp[0] = True  # We can always make sum 0 (by taking no elements)

        for num in nums:
            # Going backward to avoid counting the same element multiple times
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


if __name__ == "__main__":
    test_case_1 = [1, 5, 5, 11]  # true [1, 5, 5] and [11]
    test_case_2 = [1, 2, 5]  # false

    cls = Solution()
    ans = cls.canPartition(test_case_2)
    print("-----")
    print(ans)
