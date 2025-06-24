# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k
"""
Good problem for understanding how to get the bounds for a range.
"""

from typing import TypedDict


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        res: list[str] = []
        i = 0
        while True:
            start = k * i
            end = (k - 1) + i * k

            subset = s[start : end + 1]

            if len(subset) == k:
                res.append(subset)
            elif len(subset) > 0:
                subset = subset.ljust(k, fill)
                res.append(subset)
            else:
                break

            i += 1

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        s: str
        k: int
        fill: str

    test_case_1: TestCase = {
        "s": "abcdefghi",
        "k": 3,
        "fill": "x",
    }  # ["abc","def","ghi"]

    test_case_2: TestCase = {
        "s": "abcdefghij",
        "k": 3,
        "fill": "x",
    }  # ["abc","def","ghi","jxx"]

    cls = Solution()
    ans = cls.divideString(**test_case_2)
    print("------")
    print(ans)
