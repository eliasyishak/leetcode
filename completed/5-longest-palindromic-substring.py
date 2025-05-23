# https://leetcode.com/problems/longest-palindromic-substring
"""
There is a dp approach to this problem that involves using a 2D
dp grid. Tough for me to follow how that works but the more intuitive
approach from me was iterating through the whole array and expanding
from what would be the center of the palindromic string.

With this approach, it is important to consider both odd and even length
strings.
"""

from typing import Literal


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(length_parity: Literal["even", "odd"], left: int, right: int) -> str:
            # Gets the value in the middle since 1 char is a palindrome of length = 1
            curr = s[left + 1] if length_parity == "odd" else ""

            while left >= 0 and right < n and s[left] == s[right]:
                curr = f"{s[left]}{curr}{s[right]}"
                left -= 1
                right += 1

            return curr

        res = ""
        for i in range(n):
            odd_length = expand(length_parity="odd", left=i - 1, right=i + 1)
            even_length = expand(length_parity="even", left=i, right=i + 1)

            if len(odd_length) > len(res):
                res = odd_length

            if len(even_length) > len(res):
                res = even_length

        return res


if __name__ == "__main__":
    test_case_1 = "racecar"  # racecar
    test_case_2 = "cbbd"  # bb

    cls = Solution()
    ans = cls.longestPalindrome(test_case_1)
    print("-------")
    print(ans)
