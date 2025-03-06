# https://leetcode.com/problems/find-missing-and-repeated-values
"""
Straightforward easy problem. Using a set allows to find values that
have been found twice AND values that we have not found yet
"""


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        ROWS = len(grid)
        COLS = len(grid[0])
        n = ROWS * COLS

        n_set = set(range(1, n + 1))
        A = -1

        for i in range(ROWS):
            for j in range(COLS):
                val = grid[i][j]

                # Found once
                if val in n_set:
                    n_set.remove(val)
                # Found twice
                else:
                    A = val

        return [A, min(n_set)]


if __name__ == "__main__":
    test_case_1 = [[1, 3], [2, 2]]  # [2, 4]

    cls = Solution()
    ans = cls.findMissingAndRepeatedValues(test_case_1)
    print("-----")
    print(ans)
