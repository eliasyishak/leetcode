# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii
"""
Definitely a tough problem to think through. The tough part of
this problem is because we need EXACTLY k non vowels. Instead
of creating a complicated approach though, we can use try to back
into this number by seeing how many substrings have k or more non vowels
and then subtract substrings that have k+1 or more non vowels.
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atleast_k(k) -> int:
            res = 0
            left = 0
            vowels: dict[str, int] = defaultdict(int)
            consonants = 0
            for right in range(n):
                right_char = word[right]

                if word[right] in "aeiou":
                    vowels[right_char] += 1
                else:
                    consonants += 1

                while len(vowels) == 5 and consonants >= k:
                    res += n - right

                    left_char = word[left]

                    if left_char in "aeiou":
                        vowels[left_char] -= 1
                    else:
                        consonants -= 1

                    if vowels[left_char] == 0:
                        vowels.pop(left_char)

                    left += 1

            return res

        return atleast_k(k) - atleast_k(k + 1)


class TestCaseType(TypedDict):
    word: str
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {"word": "ieaouqqieaouqq", "k": 1}  # 3

    cls = Solution()
    ans = cls.countOfSubstrings(**test_case_1)
    print("-----")
    print(ans)
