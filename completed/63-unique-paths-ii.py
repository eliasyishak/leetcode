# https://leetcode.com/problems/unique-paths-ii
"""
A fairly straightforward follow up from the previous problem 62-unique-paths.py
where we did not have any obstacles. In this variation, we adjust our dp
grid so that we don't populate the answers if there was an obstacle in the way.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # Initialize the top row and first column, if there is an obstacle in
        # the way, then everything after the obstacle is
        # unreachable
        for j in range(COLS):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        # Traverse the grid now using the previous values
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    test_case_1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]  # 2

    test_case_2 = [
        [0, 1],
        [0, 0],
    ]  # 1

    cls = Solution()
    ans = cls.uniquePathsWithObstacles(test_case_2)
    print("------")
    print(ans)
