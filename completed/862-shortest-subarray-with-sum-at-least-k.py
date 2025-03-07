# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k

from typing import TypedDict


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        stack: list[tuple[int, int]] = []  # (prefix_sum_at_index, index)
        res = float("inf")

        prefix_sum = 0
        for i, val in enumerate(nums):
            prefix_sum += val

            if prefix_sum >= k:
                res = min(res, i + 1)

            while stack and prefix_sum - stack[0][0] >= k:
                _, curr_prefix_index = stack.pop(0)

                res = min(res, i - curr_prefix_index)

            # Ensure that the stack is in monotonic order
            while stack and stack[-1][0] > prefix_sum:
                stack.pop()

            stack.append((prefix_sum, i))

        return int(res) if res != float("inf") else -1


class TestCaseType(TypedDict):
    nums: list[int]
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "nums": [2, -1, 2, 1],
        "k": 3,
    }  # 2 ---> len( [2, 1] )

    cls = Solution()
    ans = cls.shortestSubarray(**test_case_1)
    print("-----")
    print(ans)
