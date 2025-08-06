# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special
"""
Fairly straightforward when you realize that do nested loops is okay since
the most characters in each loop is limited to 26.
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        res = len(word)

        freq: dict[str, int] = defaultdict(int)
        for char in word:
            freq[char] += 1

        # Iterate through each character and try to make that
        # the minimum in the calculation abs(freq[a] - freq[b]) <= k
        for _, a_count in freq.items():
            curr_deletions = 0
            for _, b_count in freq.items():
                if a_count > b_count:
                    curr_deletions += b_count

                elif b_count > a_count + k:
                    curr_deletions += b_count - (a_count + k)

            res = min(res, curr_deletions)

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        word: str
        k: int

    test_case_1: TestCase = {
        "word": "aabcaba",
        "k": 0,
    }  # 3

    cls = Solution()
    ans = cls.minimumDeletions(**test_case_1)
    print("-----")
    print(ans)
