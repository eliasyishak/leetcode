# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i
"""
Taking the greedy approach here feels natural. Fairly straightforward, queues us
up for the second variation of this problem.

Overall an easy problem though.
"""


class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        res = [words[0]]
        last_group = groups[0]
        n = len(words)

        for i in range(1, n):
            if groups[i] != last_group:
                res.append(words[i])
                last_group = groups[i]

        return res


if __name__ == "__main__":
    test_case_1 = {
        "words": ["e", "a", "b"],
        "groups": [0, 0, 1],
    }  # ["e","b"] or ["a", "b"]

    cls = Solution()
    ans = cls.getLongestSubsequence(**test_case_1)  # type: ignore
    print("------")
    print(ans)
