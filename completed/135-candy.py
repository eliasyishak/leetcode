# https://leetcode.com/problems/candy
"""
Prefix and suffix arrays can be used to find the amount to give each child.
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for i in range(1, n):
            left = i
            right = n - 1 - i

            # Increment the prefix list if the current item at left is
            # greater than the item to the left of it
            if ratings[left] > ratings[left - 1]:
                prefix[left] = prefix[left - 1] + 1

            # Do the same but for the suffix array going from right to left
            if ratings[right] > ratings[right + 1]:
                suffix[right] = suffix[right + 1] + 1

        return sum(max(prefix[i], suffix[i]) for i in range(n))


if __name__ == "__main__":
    test_case_1 = [1, 0, 2]  # 5
    test_case_2 = [1, 2, 2]  # 4

    cls = Solution()
    ans = cls.candy(test_case_2)
    print("-----")
    print(ans)
