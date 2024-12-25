# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows
"""
Kind of an annoying problem, you had to know the "trick" here about flipping the
columns to create rows that are uniform.

Note: all of the rows don't have to have the same values, just each row

0 0 0
0 0 1
1 1 0

The trick here is to keep a count of all the uniform rows that currently exist
AND any inverse rows. For example above, the second and third rows are inverses
of each other

[0 0 1] is the inverse of [1 1 0]

The trick is to understand that the flips we make to make those two
equal are independent to those rows, that is why we check for all possible
pairs by keeping a running count in the dictionary.
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = defaultdict(int)
        for row in matrix:
            # Create the lookup key for each row and create its inverse
            # if it starts with a zero
            if row[0] == 0:
                row_key = ",".join([str(val) for val in row])
            else:
                row_key = ",".join(["0" if val == 1 else "1" for val in row])

            counts[row_key] += 1

        return max(counts.values())


if __name__ == "__main__":
    test_case_1 = [
        [0, 0, 0],
        [0, 0, 1],
        [1, 1, 0],
    ]  # 2

    cls = Solution()
    ans = cls.maxEqualRowsAfterFlips(matrix=test_case_1)
    print("-----")
    print(ans)
