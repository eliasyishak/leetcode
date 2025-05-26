# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words
"""
The key to this problem is understanding how the palindrome is created.
You don't need to actually construct it to understand how to get the longest
possible string.

For example, when you have a string like "cl" you know you will need an equal number
of "lc" strings to form a palindrome. Additionally, for strings that have the same letter
"aa", you can use at most, ONE "aa" in your final string, every other use of an "aa" will
require another matched "aa".

As a result: ["aa", "aa", "aa", "bb", "bb", "bb"] -> you can use 3 "aa" and 2 "bb"
or vice versa, but you cannot use 3 of each.
"""

from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        # Keep track of:
        # 1. words that are double letters
        # 2. hash map to find alternative
        # 3. total counts
        pair_lookup: dict[str, str] = {}
        counts: dict[str, int] = defaultdict(int)
        for word in words:
            counts[word] += 1
            # Double letter words
            if word[0] == word[1]:
                # doubles.add(word)
                pair_lookup[word] = word
            else:
                # Keep the pairs unique
                if word[::-1] not in pair_lookup:
                    pair_lookup[word] = word[::-1]

        # Use the lookup object to get a count of the pairs
        # print(pair_lookup)
        # print(counts)

        # We can only use one word that is a double in a valid palindrome
        single_double_used = False
        pairs = 0
        for word, match in pair_lookup.items():
            # Special handling for doubles
            if word[0] == word[1]:
                if counts[word] % 2:
                    pairs += counts[word] - 1
                    if not single_double_used:
                        pairs += 1
                        single_double_used = True
                else:
                    pairs += counts[word]
            else:
                pairs += min([counts[word], counts[match]]) * 2

        return pairs * 2


if __name__ == "__main__":
    test_case_1 = ["ab", "ty", "yt", "lc", "cl", "ab"]  # 8
    test_case_2 = ["lc", "cl", "gg"]  # 6
    test_case_3 = ["cc", "ll", "xx"]  # 2
    test_case_4 = [
        "aa",
        "aa",
        "aa",
        ##
        "bb",
        "bb",
        "bb",
        ##
        "cc",
        "cc",
        "cc",
        ##
        "dd",
        "dd",
        "dd",
        "dd",
        "dd",
    ]  # 22

    cls = Solution()
    ans = cls.longestPalindrome(test_case_4)
    print("-----")
    print(ans)
