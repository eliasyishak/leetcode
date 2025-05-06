# https://leetcode.com/problems/number-of-equivalent-domino-pairs
"""
The tricky part here is to ensure you are adding to res properly as you
are adding more pairs. You can't simply just +1 for every pair you find.
"""

from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        res = 0
        counts: dict[tuple[int, ...], int] = defaultdict(int)

        for pair in dominoes:
            pair_sorted = [pair[0], pair[1]]
            pair_sorted.sort()
            pair_tuple = tuple(pair_sorted)

            if counts[pair_tuple]:
                res += counts[pair_tuple]

            counts[pair_tuple] += 1

        return res


if __name__ == "__main__":
    test_case_1 = [[1, 2], [2, 1], [3, 4], [5, 6]]  # 1
    test_case_2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]  # 3

    cls = Solution()
    ans = cls.numEquivDominoPairs(test_case_2)
    print("-----")
    print(ans)
