# https://leetcode.com/problems/count-number-of-bad-pairs
"""
The key to this problem is understanding the constraint for what makes a
bad pair. A pair is bad if j - i != nums[j] - nums[i]

Which means a good pair is j - i == nums[j] - nums[i]

If we rewrite this equation, we can ahve j - nums[j] == i - nums[i], using
this preprocessed approach, we can use the frequency off differences
to solve this in linear O(n) time.
"""

from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        total_pairs = 0
        good_pairs = 0

        diff_count: dict[int, int] = defaultdict(int)
        for i in range(n):
            total_pairs += n - i - 1
            diff = nums[i] - i
            good_pairs += diff_count[diff]

            diff_count[diff] += 1

        return total_pairs - good_pairs

    def countBadPairsSlow(self, nums: List[int]) -> int:
        n = len(nums)
        processed = [val - i for i, val in enumerate(nums)]

        bad_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if processed[j] != processed[i]:
                    bad_pairs += 1

        return bad_pairs


if __name__ == "__main__":
    test_case_1 = [4, 1, 3, 3]  # 5
    test_case_2 = [1, 2, 3, 4, 5]  # 0

    cls = Solution()
    ans = cls.countBadPairs(test_case_1)
    print("-----")
    print(ans)
