# https://leetcode.com/problems/sum-of-all-subset-xor-totals
"""
Good problem to refresh on backtracking. You should only be collecting the final
subset when you have reached the base case (i == len(nums)). If we collect while
we traverse the options, we will have duplicates
"""


class Solution:
    def __init__(self):
        self.subsets = []

    def subsetXORSum(self, nums: list[int]) -> int:
        def backtrack(i: int, curr: list[int]):
            if i == len(nums):
                # Only collect at the end
                if len(curr) > 0:
                    self.subsets.append(curr)
                return

            # Include the current value at the index i
            backtrack(i + 1, [*curr, nums[i]])

            # Skip the current value
            backtrack(i + 1, [*curr])

        backtrack(0, [])
        total = 0
        for subset in self.subsets:
            curr_xor = subset[0]
            for i in range(1, len(subset)):
                curr_xor ^= subset[i]

            total += curr_xor

        return total


if __name__ == "__main__":
    test_case_1 = [5, 1, 6]  # 28

    cls = Solution()
    ans = cls.subsetXORSum(test_case_1)
    print("-------")
    print(ans)
