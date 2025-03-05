# https://leetcode.com/problems/count-total-number-of-colored-cells
"""
There are two ways to approach this problem. We can take the approach with
the iterations where we keep a running count of the cells and increasing them
as we iterate left to right.

The other option is to simply do it with math. If you look at the diagram that comes
with this problem, it should be fairly easy to figure the math.
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        rows = (n - 1) * 2 + 1

        long_rows = -(-rows // 2)
        short_rows = rows - long_rows

        return long_rows * n + short_rows * (n - 1)

    def coloredCellsIterative(self, n: int) -> int:
        width = (n - 1) * 2 + 1
        middle = n - 1

        res = 0
        cells = 1
        for i in range(width):
            res += cells

            if i < middle:
                cells += 2
            else:
                cells -= 2

        return res


if __name__ == "__main__":
    test_case_1 = 3  # 13

    cls = Solution()
    ans = cls.coloredCells(test_case_1)
    print("------")
    print(ans)
