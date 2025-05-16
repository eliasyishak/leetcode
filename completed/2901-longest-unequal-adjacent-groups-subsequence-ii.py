# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii
"""
The key to this problem is understanding that you need to keep a trail
of the valid strings as well as the dp array.

Once you have that, you can safely trace the result backwards. Tough problem
for sure.
"""


class Solution:
    def getWordsInLongestSubsequence(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        n = len(words)

        def hamming_distance_check(word1: str, word2: str) -> bool:
            if len(word1) != len(word2):
                return False

            diff = 0
            for index, char1 in enumerate(word1):
                if char1 != word2[index]:
                    diff += 1

                if diff > 1:
                    return False

            return True

        dp = [1] * n
        # This holds the previous index that links to the current index
        prev = [-1] * n

        # Iterate through the list and check the values to the
        # left of i for solutions
        for i in range(n):
            outer_word = words[i]
            for j in range(i):
                inner_word = words[j]

                if (
                    hamming_distance_check(outer_word, inner_word)
                    and groups[i] != groups[j]
                    # Makes sure that we found a valid value that is better than the current
                    and dp[j] + 1 > dp[i]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # Get the index of the string that has the longest chain of
        # valid strings
        max_index = dp.index(max(dp))
        res: list[str] = []
        while max_index != -1:
            res.append(words[max_index])
            max_index = prev[max_index]

        return list(reversed(res))


if __name__ == "__main__":
    test_case_1 = {
        "words": ["bab", "dab", "cab"],
        "groups": [1, 2, 2],
    }  # ["bab","cab"] or ["bab","dab"]

    test_case_2 = {
        "words": ["dca", "dc", "bc", "ccd", "dd", "da", "cad"],
        "groups": [4, 5, 1, 4, 6, 7, 3],
    }  # ["dc"(1), "dd"(4), "da"(5)]

    cls = Solution()
    ans = cls.getWordsInLongestSubsequence(**test_case_2)  # type: ignore
    print("------")
    print(ans)
