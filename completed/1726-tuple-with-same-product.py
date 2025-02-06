# https://leetcode.com/problems/tuple-with-same-product
"""
This is almost similar to a 3 sum problem where instead of trying to
find all of the pairs, you can instead try to find the products of those pairs
and make a count of how many pairs give a product.

Only thing tricky about this problem is that you have to use the combination
formula to get the number of combinations of pairs you can make.

For example, if we had the below product counts (only including freqs greater than 1)

{
    12: 2,
    24: 3,
    48: 2,
}

We have to find out how many different days we can select 2 pairs out of 3 pairs for 24.

Formula can be found here:
https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php
"""

import math
from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        counts: dict[int, int] = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                counts[product] += 1

        res = 0
        for product, freq in counts.items():
            if freq > 1:
                numerator = math.factorial(freq)
                denominator = 2 * math.factorial(freq - 2)

                combinations = int(numerator / denominator)
                res += combinations * 8

        return res


if __name__ == "__main__":
    test_case_1 = [2, 3, 4, 6]  # 8
    test_case_2 = [1, 2, 4, 5, 10]  # 16
    test_case_3 = [2, 3, 4, 6, 8, 12]  # 40

    cls = Solution()
    ans = cls.tupleSameProduct(test_case_3)
    print("------")
    print(ans)
