# https://leetcode.com/problems/unique-paths
"""
Great dynamic programming example where you can really break down the
subproblems. The inner cells can only be reached from the top and the
left neighboring cells so if you know how many ways there are to get
to those neighboring cells, you can take the sum of those values
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n = cols, m = rows

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize the first row with 1s since there is only one way to
        # traverse each cell in the first row
        for j in range(n):
            dp[0][j] = 1

        # Do the same with the first column
        for i in range(m):
            dp[i][0] = 1

        # Traverse the grid now using the previous values
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    test_case_1 = {
        "m": 3,
        "n": 7,
    }  # 28

    cls = Solution()
    ans = cls.uniquePaths(**test_case_1)
    print("------")
    print(ans)
