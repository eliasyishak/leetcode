# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i
"""
A straight forward problem when you think about using a data structure to keep track of the
values we have banned. The trick here is to convert the banned list of integers into a hashset
so that we can perform an O(1) lookup, which makes this an O(n) algorithm. If we did not convert
to a hash set and looked up the entry in the list, it would take this algorithm to an O(n^2)
"""
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)

        curr = 0
        count = 0
        for val in range(1, n + 1):
            if val not in banned_set:
                if curr + val == maxSum:
                    return count + 1
                if curr + val > maxSum:
                    return count

                curr += val
                count += 1

        return 0 if curr > maxSum else count


if __name__ == "__main__":
    test_case_1 = {
        "banned": [1, 6, 5],
        "n": 5,
        "maxSum": 6,
    }  # 2
    test_case_2 = {
        "banned": [11],
        "n": 7,
        "maxSum": 50,
    }  # 7

    test_case = test_case_2
    cls = Solution()
    ans = cls.maxCount(
        banned=test_case["banned"],
        maxSum=test_case["maxSum"],
        n=test_case["n"],
    )
    print("-----")
    print(ans)
