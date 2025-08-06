# https://leetcode.com/problems/pascals-triangle
"""
Although everyone understands pascals triangle and how it is constructed,
it really is the best example of what dynamic programming is. Small problems
built up on smaller problem solutions.
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res: list[list[int]] = []
        for i in range(numRows):
            res.append([0] * (i + 1))

        # Set the first cell
        res[0][0] = 1

        for i in range(1, numRows):
            curr = res[i]

            for j in range(len(curr)):
                # Handle the ends
                if j == 0 or j == len(curr) - 1:
                    res[i][j] = 1

                # Everything in between
                else:
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res


if __name__ == "__main__":
    test_case_1 = 5  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    test_case_2 = 1  # [[1]]

    cls = Solution()
    ans = cls.generate(test_case_2)
    print("-------")
    print(ans)
