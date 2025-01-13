# https://leetcode.com/problems/minimum-length-of-string-after-operations
"""
We use a frequency count for each character in s, for example test_case_1 has
the below frequncy count

{
    "a": 3,
    "b": 4,
    "c": 2,
}

Each time we perform an operation, we remove 2 characters, as a result, we want
to find every character that has more than 3 occurences since we need to have one
char in the middle and 2 on each side of it.

So we will decrease the count to either 1 (if we have an odd freq count) or 2 (for
even counts). We can then keep a running count of the values we removed and subtract
it from the original string's length.
"""

from collections import defaultdict


class Solution:
    def minimumLength(self, s: str) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        removed = 0
        for char, count in freq.items():
            if count % 2 == 0:
                removed += count - 2
            else:
                removed += count - 1

        return len(s) - removed


if __name__ == "__main__":
    test_case_1 = "abaacbcbb"  # 5
    test_case_2 = "aa"  # 2

    cls = Solution()
    ans = cls.minimumLength(test_case_1)
    print("------")
    print(ans)
