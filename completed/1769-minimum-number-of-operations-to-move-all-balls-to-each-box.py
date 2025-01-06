# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
"""
Good prefix AND suffix problem. To solve this, we keep a running count
going left to right and vice versa. The final answer will be the sum
of the counts from the left and right.
"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        prefix = [0] * n
        left_ones = 0
        for i, char in enumerate(boxes):
            if i == 0:
                prefix[0] = 0
                if char == "1":
                    left_ones += 1
            else:
                prefix[i] = prefix[i - 1] + left_ones
                if char == "1":
                    left_ones += 1

        suffix = [0] * n
        right_ones = 0
        for j, char in enumerate(boxes[::-1]):
            if j == 0:
                suffix[n - 1 - j] = 0
                if char == "1":
                    right_ones += 1

            else:
                suffix[n - 1 - j] = suffix[n - 1 - j + 1] + right_ones
                if char == "1":
                    right_ones += 1

        return [prefix[k] + suffix[k] for k in range(n)]

    def minOperationsSlow(self, boxes: str) -> List[int]:
        """
        This is the brute force approach that works as well for the problem
        but it has a time complexity of O(n^2)
        """
        n = len(boxes)
        res = [0] * n

        for i in range(n):
            curr = 0
            for j in range(n):
                if i == j:
                    continue

                if boxes[j] == "1":
                    curr += abs(i - j)

            res[i] = curr

        return res


if __name__ == "__main__":
    test_case_1 = "110"  # [1,1,3]
    test_case_2 = "001011"  # [11,8,5,4,3,4]

    cls = Solution()
    ans = cls.minOperations(test_case_1)
    print("------")
    print(ans)
