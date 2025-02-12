# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits
"""
Room for some optimization if I could figure out how to calculate the sum
of the digits in a number without converting to a string.

But using a heap to keep track of the largest values makes this problem simple.
Could probably further optimize to keep the list two items long but meh :)
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        counts: dict[int, list[int]] = defaultdict(list)
        for val in nums:
            curr = sum(int(char) for char in str(val))

            heapq.heappush(counts[curr], -val)

        res = -1
        for _, vals in counts.items():
            if len(vals) > 1:
                curr = 0
                for _ in range(2):
                    top = -heapq.heappop(vals)

                    curr += top

                res = max(res, curr)

        return res


if __name__ == "__main__":
    test_case_1 = [18, 43, 36, 13, 7]  # 54
    test_case_2 = [10, 12, 19, 14]  # -1
    test_case_3 = [
        229,
        398,
        269,
        317,
        420,
        464,
        491,
        218,
        439,
        153,
        482,
        169,
        411,
        93,
        147,
        50,
        347,
        210,
        251,
        366,
        401,
    ]  # 973

    cls = Solution()
    ans = cls.maximumSum(test_case_2)
    print("-----")
    print(ans)
