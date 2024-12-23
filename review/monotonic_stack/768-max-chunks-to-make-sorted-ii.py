# https://leetcode.com/problems/max-chunks-to-make-sorted-ii
"""
You can view this problem as a monotonic stack problem and it becomes pretty simple
to understand. Going from left to right, every item in the stack should be increasing,
if something violates that rule, then we keep popping until that assumption holds again.
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            max_val = num
            # While stack not empty and current number is less than stack top,
            # we need to merge chunks by keeping the maximum value
            while stack and stack[-1] > num:
                max_val = max(max_val, stack.pop())
            stack.append(max_val)

        return len(stack)


if __name__ == "__main__":
    test_case_1 = [3, 2, 1, 3, 5, 4]  # 3
    test_case_2 = [5, 4, 3, 2, 1]  # 1
    test_case_3 = [2, 1, 3, 4, 4]  # 4

    cls = Solution()
    ans = cls.maxChunksToSorted(arr=test_case_3)
    print("-----")
    print(ans)
