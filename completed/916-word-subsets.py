# https://leetcode.com/problems/word-subsets
"""
To solve this problem we can think of the words2 array as one single
word that we want to match on instead of performing an O(n^2) approach

For example the words list = ["lo", "eo"] can be thought of as a
single word with the following character counts
{
    "l": 1,
    "o": 1,
    "e": 1,
}

This means that the words we want to match have to have at least
one "l", "o", and "e" characters to ensure that we can match every word
in the words2 array.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def get_char_counts(self, words: List[str]) -> List[Dict]:
        count_list = []
        for word in words:
            count = defaultdict(int)
            for char in word:
                count[char] += 1

            count_list.append(dict(count))

        return count_list

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []

        words1_char_counts = self.get_char_counts(words1)
        word2_count = defaultdict(int)
        for word in words2:
            curr = defaultdict(int)
            for char in word:
                curr[char] += 1

            for char, count in curr.items():
                word2_count[char] = max(word2_count[char], count)

        for i, word1_count in enumerate(words1_char_counts):
            word1_valid = True

            # We want every character to match from word2 to the word1 in the
            # outer loop for a valid word
            for char, count in word2_count.items():
                if char not in word1_count or count > word1_count[char]:
                    word1_valid = False

            if word1_valid:
                res.append(words1[i])

        return res


if __name__ == "__main__":
    test_case_1 = {
        "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
        "words2": ["e", "o"],
    }  # ["facebook","google","leetcode"]

    test_case_2 = {
        "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
        "words2": ["l", "e"],
    }  # ["apple","google","leetcode"]

    test_case_3 = {
        "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
        "words2": ["e", "oo"],
    }  # ["facebook","google"]

    test_case_4 = {
        "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
        "words2": ["lo", "eo"],
    }  # ["google","leetcode"]

    cls = Solution()
    ans = cls.wordSubsets(**test_case_4)
    print("-----")
    print(ans)
