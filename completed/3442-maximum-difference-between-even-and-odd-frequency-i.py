# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i
"""
Pretty easy problem. An additional optimization that could have been made
specifically for python is to use the built in Counter(...) but I preferred
to write it myself.
"""

from collections import defaultdict


class Solution:
    def maxDifference(self, s: str) -> int:
        counts: dict[str, int] = defaultdict(int)

        for char in s:
            counts[char] += 1

        largest_odd = -float("inf")
        smallest_even = float("inf")
        for _, count in counts.items():
            if count % 2 == 1 and count > largest_odd:
                largest_odd = count

            if count % 2 == 0 and count < smallest_even:
                smallest_even = count

        res = (int(largest_odd) if largest_odd != float("inf") else 0) - (
            int(smallest_even) if smallest_even != -float("inf") else 0
        )

        return res


if __name__ == "__main__":
    test_case_1 = "aaaaabbc"  # 3

    cls = Solution()
    ans = cls.maxDifference(test_case_1)
    print("-------")
    print(ans)
