# https://leetcode.com/problems/jump-game
"""
Because this is only looking for a pass/fail, we can simply just take a greedy
approach to the problem and look at how far we can reach based on each index
we pass.

If we end up on an index that we previously did not find a way to reach, then
we can early exit out.
"""


class Solution:
    def canJumpSlow(self, nums: list[int]) -> bool:
        def dfs(i: int) -> bool:
            if i == len(nums) - 1:
                return True

            for val in range(nums[i]):
                res = dfs(i=i + val + 1)
                if res:
                    return True

            return False

        return dfs(i=0)

    def canJump(self, nums: list[int]) -> bool:
        # Define the max reachable index as a variable that we keep pushing down
        # as we iterate through the whole list
        max_reachable_index = 0
        for i, val in enumerate(nums):
            # If we are at an index that we cannot reach, then we can safely exit out
            if max_reachable_index < i:
                return False

            max_reachable_index = max(max_reachable_index, i + val)

        return True


if __name__ == "__main__":
    test_case_1 = [2, 3, 1, 1, 4]  # true
    test_case_2 = [3, 2, 1, 0, 4]  # false

    cls = Solution()
    ans = cls.canJump(test_case_2)
    print("-------")
    print(ans)
