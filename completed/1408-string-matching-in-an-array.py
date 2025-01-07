# https://leetcode.com/problems/string-matching-in-an-array
"""
Easy problem that was able to be solved with a brute force approach.
I went a little further and tried to see what it would be like to optimize
the time complexity with extra space being used by storing a trie-like data
structure to find all the indexes for each character in a word. Then we go
through again check each combination of words.

This seems like another O(n^2) approach but having the trie allows us to
short circuit out if we find that we don't have the starting character for
the substring in the larger string.

For example, with test_case_1 = ["mass", "as", "hero", "superhero"],
we find that we have significantly less operations done to check if the
substrings match -- but we trade this for increased space usage.

Operations in V1: 10
Operations in V2: 2
"""

from collections import defaultdict
from typing import List


class Solution:
    def stringMatchingV1(self, words: List[str]) -> List[str]:
        res = []
        ops = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue

                ops += 1
                if word1 in word2:
                    res.append(word1)
                    break

        print("Operations in V1:", ops)
        return res

    def stringMatchingV2(self, words: List[str]) -> List[str]:
        res = set()
        lookup = []
        ops = 0
        for word in words:
            chars = defaultdict(list)
            for i, char in enumerate(word):
                chars[char].append(i)
            lookup.append(dict(chars))

        # Use the look up to find the starting point for
        # each substring
        #
        # We are trying to check if word1 is a substring of word2
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j or len(word1) > len(word2) or word1[0] not in lookup[j]:
                    continue

                ops += 1
                # Loop through starting points for the starting character
                # of word1 to find it within word2
                for index1 in lookup[j][word1[0]]:
                    if word1 == word2[index1 : index1 + len(word1)]:
                        res.add(word1)

        print("Operations in V2:", ops)
        return list(res)


if __name__ == "__main__":
    test_case_1 = ["mass", "as", "hero", "superhero"]  # ["as","hero"]

    cls = Solution()
    ans = cls.stringMatchingV1(test_case_1)
    cls.stringMatchingV2(test_case_1)
    print("----")
    print(ans)
