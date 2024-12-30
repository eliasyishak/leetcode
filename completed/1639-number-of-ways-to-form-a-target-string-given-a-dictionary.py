# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary
"""
Another tough hard problem that is a mixture of DFS and dynamic programming.

The key to understanding this problem is being able to cache the results of the
DFS. The key we will use for our cache will be the tuple (target_index, lower_bound)

The target_index refers to the index we are looking for in the target string. The lower bound
is the smallest index we can use to pull from our words dictionary
"""

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.freq = {}
        self.cache = {}
        self.MOD = 10**9 + 7  # Add modulo constant

    def numWays(self, words: List[str], target: str) -> int:
        self.freq = defaultdict(list)
        for j, word in enumerate(words):
            for i, char in enumerate(word):
                self.freq[char].append((j, i))

        def dfs(index: int, lower_bound: int):
            if index >= len(target):
                return 1

            # If we have already found the count of ways for this combo, we can
            # use the cache to short circut
            if (index, lower_bound) in self.cache:
                return self.cache[(index, lower_bound)]

            current_count = 0
            for _, char_index in self.freq[target[index]]:
                if char_index > lower_bound:
                    current_count = (
                        current_count + dfs(index=index + 1, lower_bound=char_index)
                    ) % self.MOD

            # Use the current index in the target string and our current
            # lower bound as keys for caching the computations
            self.cache[(index, lower_bound)] = current_count
            return current_count

        return dfs(index=0, lower_bound=-1)


if __name__ == "__main__":
    test_case_1 = {
        "words": ["acca", "bbbb", "caca"],
        "target": "aba",
    }  # 6

    test_case_2 = {
        "words": [
            "dcdcbaddbc",
            "abcabcdddb",
            "cdbbccdadc",
            "bbcddccbcd",
            "addbcddabc",
            "dbddddcbdc",
            "dadcbddddb",
            "caabccdbdd",
            "ddcdcdabbc",
            "cbabbaddda",
            "cccaabdbca",
            "cabdbcabbc",
            "bcdcabadab",
            "baadadbabc",
            "aabaaabbdb",
            "adacdbbbcb",
            "aacdbcbcbc",
            "cdabdccadc",
            "baacacadbb",
            "dacadadccc",
            "caccaccadb",
            "aabaaacddd",
            "dcbcdbabaa",
            "badcacbbdd",
            "adcabddcac",
            "ccccbabbbd",
            "ccaaddbcab",
        ],
        "target": "dcbdbdcc",
    }  # 129_914_496

    test_case_3 = {
        "words": [
            "cbabddddbc",
            "addbaacbbd",
            "cccbacdccd",
            "cdcaccacac",
            "dddbacabbd",
            "bdbdadbccb",
            "ddadbacddd",
            "bbccdddadd",
            "dcabaccbbd",
            "ddddcddadc",
            "bdcaaaabdd",
            "adacdcdcdd",
            "cbaaadbdbb",
            "bccbabcbab",
            "accbdccadd",
            "dcccaaddbc",
            "cccccacabd",
            "acacdbcbbc",
            "dbbdbaccca",
            "bdbddbddda",
            "daabadbacb",
            "baccdbaada",
            "ccbabaabcb",
            "dcaabccbbb",
            "bcadddaacc",
            "acddbbdccb",
            "adbddbadab",
            "dbbcdcbcdd",
            "ddbabbadbb",
            "bccbcbbbab",
            "dabbbdbbcb",
            "dacdabadbb",
            "addcbbabab",
            "bcbbccadda",
            "abbcacadac",
            "ccdadcaada",
            "bcacdbccdb",
        ],
        "target": "bcbbcccc",
    }  # 677_452_090

    cls = Solution()
    ans = cls.numWays(**test_case_1)
    print("------")
    print(ans)
