# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row
"""
The illustration for this problem really helps when trying to conceptualize the solution.
We start with a sanity check by first checking the first two dominos and finding all of our
"possible" values by finding common values. If we don't have any common values in the first two
dominos, then we automatically know that the problem won't be solvable.

From there, we check each of these possible values by attempting to perform a swap to the
row that has the most counts of the converge value.
"""

from collections import defaultdict


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        # Begin by confirming if it is possible to have a solution by checking
        # the first two dominos, if they don't have a common value, then it is
        # not possible
        converge_values = set([tops[0], bottoms[0]]).intersection(
            set([tops[1], bottoms[1]])
        )

        # No common values between the first two dominos so exit early
        if len(converge_values) == 0:
            return -1

        # Create a count object for each value in the current top and bottom
        top_freq: dict[int, int] = defaultdict(int)
        bottom_freq: dict[int, int] = defaultdict(int)
        for i in range(n):
            top_freq[tops[i]] += 1
            bottom_freq[bottoms[i]] += 1

        # Iterate through each of the possible converge values and find the
        # side that has more of that value
        res = n + 1
        for val in converge_values:
            # We will iterate through the side that has less of current val
            top_count = top_freq[val]
            bottom_count = bottom_freq[val]
            moves = 0

            # If we have more on top, we will try to make top_count --> n
            if top_count >= bottom_count:
                for i in range(n):
                    if bottoms[i] == val and tops[i] != val:
                        moves += 1
                        top_count += 1

                if top_count == n:
                    res = min(res, moves)
            else:
                for i in range(n):
                    if tops[i] == val and bottoms[i] != val:
                        moves += 1
                        bottom_count += 1

                if bottom_count == n:
                    res = min(res, moves)

        return res if res != n + 1 else -1


if __name__ == "__main__":
    test_case_1 = {
        "tops": [2, 1, 2, 4, 2, 2],
        "bottoms": [5, 2, 6, 2, 3, 2],
    }  # 2

    test_case_2 = {
        "tops": [3, 5, 1, 2, 3],
        "bottoms": [3, 6, 3, 3, 4],
    }  # -1

    test_case_3 = {
        "tops": [1, 2, 1, 1, 1, 2, 2, 2],
        "bottoms": [2, 1, 2, 2, 2, 2, 2, 2],
    }  # 1

    cls = Solution()
    ans = cls.minDominoRotations(**test_case_3)
    print("----")
    print(ans)
