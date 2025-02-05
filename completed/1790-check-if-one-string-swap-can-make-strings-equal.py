# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal
"""
Straight forward problem, just need to look for exactly two mismatches and ensure
that they are the same characters needed to make them equal.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        first = second = -1

        for i in range(n):
            if s1[i] != s2[i]:
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False

        if first != -1 or second != -1:
            # Need an xor here because we want to ensure that we have two matches
            if first == -1 ^ second == -1:
                return False

            return s1[first] == s2[second] and s1[second] == s2[first]

        return True


if __name__ == "__main__":
    test_case_1 = {
        "s1": "bank",
        "s2": "kanb",
    }  # true

    test_case_2 = {
        "s1": "kelb",
        "s2": "kelb",
    }  # true

    test_case_3 = {
        "s1": "kzzhzsljycjgdagamjjmylkhqhpsimuyxplsvkgkwlwdhtlehphleagbwjgzgcfoybrbldtfrcclociondqsfatgxqsbggazny",
        "s2": "kezhzsljycjgdagamjjmylkhqhpsimuyxplsvkgkwlwdhtlehphlzagbwjgzgcfoybrbldtfrcclociondqsfatgxqsbggazny",
    }  # true

    cls = Solution()
    ans = cls.areAlmostEqual(**test_case_3)
    print("-----")
    print(ans)
