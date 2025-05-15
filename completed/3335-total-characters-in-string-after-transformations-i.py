# https://leetcode.com/problems/total-characters-in-string-after-transformations-i
"""
Spent some time trying to figure out the math solution to this problem but that isn't
necessary and not really what this problem is trying to test. If we iterate through each
of the transformations and use a new frequency count, we can easily swap them after
each iteration and continue to the operations.

The time complexity becomes O(t*26) ~ O(t)
"""

from typing import TypedDict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        def get_pos(char):
            return ord(char) - ord("a")

        freq = [0] * 26
        for char in s:
            pos = get_pos(char)
            freq[pos] += 1

        new_freq = [0] * 26
        for _ in range(t):
            for index in range(26):
                if freq[index] == 0:
                    continue

                # Special handling for the last char
                if index == 25:
                    new_freq[0] += freq[index]
                    new_freq[1] += freq[index]

                else:
                    new_freq[index + 1] = freq[index]

            # Swap the lists and create a new empty
            freq = list(new_freq)
            new_freq = [0] * 26

        return sum(freq) % MOD


class TestCaseType(TypedDict):
    s: str
    t: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "s": "abcyy",
        "t": 2,
    }  # 7

    test_case_2: TestCaseType = {
        "s": "azbk",
        "t": 1,
    }  # 5

    test_case_3: TestCaseType = {
        "s": "jqktcurgdvlibczdsvnsg",
        "t": 7517,
    }  # 79033769

    cls = Solution()
    ans = cls.lengthAfterTransformations(**test_case_3)
    print("------")
    print(ans)
