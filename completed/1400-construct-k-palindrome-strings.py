# https://leetcode.com/problems/construct-k-palindrome-strings
"""
Not the biggest fan of this problem, this was rated a medium but you had
to come up with a "clever" way to think of the problem instead of coming up
with a challenging algorithm.

The idea here is first get the character frequencies and look for any
characters that have an odd count. If you have an odd count of characters,
that means to form a palindrome with that character, you will have at some
point, just one of that character

"annabelle" produces the frequency object below
{
    "a": 2,
    "n": 2,
    "b": 1,
    "e": 2,
    "l": 2,
}

Because we have only one "l", it must be in the middle of the string or
be on it's own. However, we only have one of these odd characters so the other
string can be something like "anna" because we can pair them up since we have an
even amount of them.

Wack
"""

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        char_counts = dict(Counter(s))

        odds = 0
        for _, count in char_counts.items():
            if count % 2 == 1:
                odds += 1

        return odds <= k


if __name__ == "__main__":
    test_case_1 = {
        "s": "annabelle",
        "k": 2,
    }  # true; "anna" + "elble", "anbna" + "elle", "anellena" + "b"

    test_case_2 = {
        "s": "leetcode",
        "k": 3,
    }  # false

    cls = Solution()
    ans = cls.canConstruct(**test_case_2)
    print("-----")
    print(ans)
