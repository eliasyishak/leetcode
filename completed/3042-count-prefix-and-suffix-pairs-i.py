# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i
"""
Easy problem that can be completed using the brute force approach. It is
not a true O(n^2) because we don't allow j to be less than i in the pair
(i, j) for a valid match.

This seems like we are prepping for creating a trie data structure and
add all of the words into that tree

For example: ["bat", "ball"] can be shown in trie below where we have a common
prefix of "ba" between the two items in the list

      (root)
       |
       b
       |
       a
      / \
     t   l
          \
           l
"""

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i >= j:
                    continue

                res += 1 if self.isPrefixAndSuffix(word1, word2) else 0

        return res

    def isPrefixAndSuffix(self, str1: str, str2: str):
        # Confirm that str1 is shorter than str2 or else
        # it is not possible for str1 to be a substring of str2
        if len(str1) > len(str2):
            return False

        # str1_len = len(str1)
        # if str1 == str2[0:str1_len] and str1 == str2[-str1_len:]:
        #     return True

        # We can use the built in python methods to handle the comparison
        if str2.startswith(str1) and str2.endswith(str1):
            return True

        return False


if __name__ == "__main__":
    test_case_1 = ["a", "aba", "ababa", "aa"]  # 4

    cls = Solution()
    ans = cls.countPrefixSuffixPairs(test_case_1)
    print("-----")
    print(ans)
