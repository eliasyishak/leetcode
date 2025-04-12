# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct
"""
Fun problem to work through using two look up objects. Alternatively, you could have come
up with a solution by traversing the list backwards and keeping track of the elements we have
encountered.
"""

from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        counts: dict[int, int] = defaultdict(int)
        dups: dict[int, int] = {}
        for val in nums:
            counts[val] += 1
            if counts[val] > 1:
                if val not in dups:
                    dups[val] = 1
                dups[val] += 1

        res = 0
        i = 0
        while len(dups) > 0 and i < len(nums):
            res += 1
            next_three_elements = nums[i : i + 3]
            i += 3

            for val in next_three_elements:
                if val not in dups:
                    continue
                dups[val] -= 1

                if dups[val] == 1:
                    del dups[val]

        return res


if __name__ == "__main__":
    test_case_1 = [1, 2, 3, 4, 2, 3, 3, 5, 7]  # 2
    test_case_2 = [4, 5, 6, 4, 4]  # 2

    cls = Solution()
    ans = cls.minimumOperations(test_case_1)
    print("------")
    print(ans)
