# https://leetcode.com/problems/count-ways-to-build-good-strings/?envType=daily-question&envId=2024-12-30
"""
Finally starting to get the hang of the DFS + dynamic programming questions.
During my first attempt of this problem, I correctly had setup the cache to
short circuit additional recursive calcuations BUT I used the wrong key for
storing the data.  I originally had used the current string we have been building
but that was incorrect. The correct key should be the length of the string we are
currently on.

It doesn't matter if our string is "1111" or "0000", we really care that both of
those strings have a length of 4.
"""


class Solution:
    def __init__(self):
        self.cache = {}
        self.MOD = 10**9 + 7

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def dfs(length: int) -> int:
            if length > high:
                return 0

            if length in self.cache:
                return self.cache[length]

            # Count current string if it's within range
            curr_count = 1 if low <= length <= high else 0

            # Recursive cases: add zeros, ones, and current count
            good_strings = (
                dfs(length + zero)  # Add zeros
                + dfs(length + one)  # Add ones
                + curr_count
            ) % self.MOD

            self.cache[length] = good_strings

            return good_strings

        return dfs(0)


if __name__ == "__main__":
    test_case_1 = {
        "low": 3,
        "high": 3,
        "zero": 1,
        "one": 1,
    }  # 8

    test_case_2 = {
        "low": 2,
        "high": 3,
        "zero": 1,
        "one": 2,
    }  # 5

    test_case_3 = {
        "low": 200,
        "high": 200,
        "zero": 10,
        "one": 1,
    }  # 764_262_396

    cls = Solution()
    ans = cls.countGoodStrings(**test_case_3)
    print("-----")
    print(ans)
