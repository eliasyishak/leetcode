# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k
"""
This is a great greedy problem that emphasizes an understanding of binary numbers.
If you start by first convert the entire string into an integer, you can then greedily
remove the most significant bits one at a time until you get an integer that is less
than k
"""

from typing import TypedDict


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        deletions = 0
        current_total = int(s, 2)
        for i, val in enumerate(s):
            if val == "1":
                curr = int(val) * 2 ** (len(s) - i - 1)

                if current_total > k:
                    current_total -= curr
                    deletions += 1
                else:
                    return len(s) - deletions

        return len(s) - deletions


if __name__ == "__main__":

    class TestCase(TypedDict):
        s: str
        k: int

    test_case_1: TestCase = {
        "s": "00101001",
        "k": 1,
    }  # 6

    test_case_2: TestCase = {
        "s": "1001010",
        "k": 5,
    }  # 5

    cls = Solution()
    ans = cls.longestSubsequence(**test_case_2)
    print("------")
    print(ans)
