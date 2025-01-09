# https://leetcode.com/problems/counting-words-with-a-given-prefix
"""
Easy problem and straightforward, implementing a trie for this question
to get the practice, but prefixCount solution is the most optimal for
leetcode solution.
"""

import json
from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def __str__(self):
        return json.dumps(self.root)

    def add_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {"count": 0}

            current_node[char]["count"] += 1
            current_node = current_node[char]

    def get_prefix_count(self, pref: str):
        current_node = self.root
        for char in pref:
            if char not in current_node:
                return 0

            current_node = current_node[char]

        return current_node["count"]


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            if word.startswith(pref):
                res += 1

        return res

    def prefixCountTrie(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        # Use the trie to look up the prefix one character at a time and
        # return the count at the last character index
        return trie.get_prefix_count(pref)


if __name__ == "__main__":
    test_case_1 = {
        "words": ["pay", "attention", "practice", "attend"],
        "pref": "at",
    }

    cls = Solution()
    # ans = cls.prefixCount(**test_case_1)
    ans = cls.prefixCountTrie(**test_case_1)
    print("-----")
    print(ans)
