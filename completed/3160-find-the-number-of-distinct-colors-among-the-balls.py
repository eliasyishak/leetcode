# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls
"""
Keeping track of what colors we currently have active along
with their frequency makes this problem easier to understand for me.

Limit is not necessary if you keep track of each index's value in dictionary
instead of a list. The limit would have been used to initialize the list.

current = [0] * (limit + 1) ---->  current = {i: 0}

"""

from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, _limit: int, queries: List[List[int]]) -> List[int]:
        res: List[int] = []

        current: dict[int, int] = defaultdict(int)
        freq: dict[int, int] = defaultdict(int)
        for i, color in queries:
            if current[i] == 0:
                freq[color] += 1
                current[i] = color

            else:
                prev_color = current[i]
                if freq[prev_color] == 1:
                    del freq[prev_color]
                elif freq[prev_color] > 1:
                    freq[prev_color] -= 1

                freq[color] += 1
                current[i] = color

            res.append(len(freq))

        return res


if __name__ == "__main__":
    test_case_1 = {
        "_limit": 4,
        "queries": [[1, 4], [2, 5], [1, 3], [3, 4]],
    }  # [1,2,2,3]

    test_case_2 = {
        "_limit": 1,
        "queries": [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]],
    }  # [1,2,1,2,1]

    cls = Solution()
    ans = cls.queryResults(**test_case_2)  # type: ignore
    print("----")
    print(ans)
