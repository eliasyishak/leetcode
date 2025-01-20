# https://leetcode.com/problems/jump-game
"""
This question can be solved a few ways. You can take a BFS type of
approach where you treat each index as a node in a graph and attempt
to do level order traversal.

You can also do a greedy approach where you look at the furthest you can
go from each index and iterate through it one by one. This is the accepted
solution since it has the lowest time complexity.

I also implemented a DFS solution with memoization which doesn't meet the time
complexity needed for this problem.
"""

from typing import Dict, List


class Solution:
    def canJumpGreedy(self, nums: List[int]) -> bool:
        max_reachable_index = 0
        for i, max_jump in enumerate(nums):
            # If the max reachable index value is less than our
            # current index, meaning we can't reach it, then it
            # will not be possible to reach the end
            if max_reachable_index < i:
                return False

            max_reachable_index = max(max_reachable_index, i + max_jump)

        return True

    def canJump(self, nums: List[int]) -> bool:
        memo: Dict[int, bool] = {}

        def dfs(index) -> bool:
            if index in memo:
                return memo[index]

            if index == len(nums) - 1:
                return True

            if index >= len(nums):
                return False

            jump = 1
            respones = []
            for _ in range(nums[index]):
                _ans = dfs(index + jump)
                memo[index] = _ans

                respones.append(_ans)
                jump += 1

            return True in respones

        return dfs(0)

    def canJumpBFS(self, nums: List[int]) -> bool:
        """
        This approach is pretty slow, I attempted to solve
        this by using a BFS approach with an iterative queue
        """

        queue = [(nums[0], 0)]

        visited = set()
        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                jumps, current_index = queue.pop(0)
                if current_index in visited:
                    continue

                visited.add(current_index)

                if current_index == len(nums) - 1:
                    return True

                for i in range(jumps):
                    next_index = current_index + i + 1
                    if next_index < len(nums) and next_index not in visited:
                        queue.append((nums[next_index], next_index))

        return False


if __name__ == "__main__":
    test_case_1 = [2, 3, 1, 1, 4]  # true
    test_case_2 = [3, 2, 1, 0, 4]  # false
    test_case_3 = [2, 0]  # true

    cls = Solution()
    ans = cls.canJumpGreedy(test_case_1)
    print("-----")
    print(ans)
