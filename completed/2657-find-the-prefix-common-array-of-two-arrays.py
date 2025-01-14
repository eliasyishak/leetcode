# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
"""
Medium problem that was fun to think through. You can accomplish this algorithm
in linear time O(n) if we make use of a frequncy count dictionary. We can make

"""

from collections import defaultdict
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n

        count = defaultdict(int)
        for i in range(n):
            val_a = A[i]
            val_b = B[i]

            count[val_a] += 1
            count[val_b] += 1

            curr = 0
            # We need to check for matching values or we would double count on the
            # curr variable
            if val_a == val_b:
                if count[val_a] == 2:
                    curr += 1
            else:
                # 2 matches means we have encountered the value in both arrays
                if count[val_a] == 2:
                    curr += 1

                if count[val_b] == 2:
                    curr += 1

            # We need to continue to build on the previous answer since all values that
            # overlapped at i - 1 would also overlap at i
            if i > 0:
                curr += res[i - 1]

            res[i] = curr

        return res


if __name__ == "__main__":
    test_case_1 = {
        "A": [1, 3, 2, 4],
        "B": [3, 1, 2, 4],
    }  # [0,2,3,4]

    cls = Solution()
    ans = cls.findThePrefixCommonArray(**test_case_1)
    print("------")
    print(ans)
