# https://leetcode.com/problems/jump-game-ii
"""
Continuation of the first problem 55-jump-game.py.

This time, we have to use a BFS approach over a greedy
approach since we need to keep a running count of the jumps
we have made.

To make this BFS, you can think of the "range of new values" you
can step as a the next frontier of nodes in BFS
"""

from typing import Dict, List, Tuple, Union


class Solution:
    def jump(self, nums: List[int]) -> Union[int, float]:
        jumps_made = 0

        queue = [0]
        visited = set()
        while queue:
            q_len = len(queue)

            # Collect all of the possible indexes we can reach with the
            # queue's current contents
            for _ in range(q_len):
                index = queue.pop(0)

                for x in range(nums[index]):
                    new_index = index + x + 1

                    if new_index not in visited and new_index < len(nums):
                        queue.append(new_index)
                        visited.add(new_index)

            if len(queue) == 0:
                break

            jumps_made += 1

        return jumps_made

    def jumpDP(self, nums: List[int]) -> Union[int, float]:
        memo: Dict[Tuple[int, int], Union[int, float]] = {}

        def dfs(index, jumps_made) -> Union[int, float]:
            if index >= len(nums) - 1:
                return jumps_made

            if (index, jumps_made) in memo:
                return memo[(index, jumps_made)]

            inc = 1
            respones: List[int] = []
            for _ in range(nums[index]):
                _ans = dfs(index + inc, jumps_made + 1)
                memo[(index, jumps_made)] = _ans
                respones.append(_ans)
                inc += 1

            return min(respones) if len(respones) > 0 else float("inf")

        return dfs(0, 0)


if __name__ == "__main__":
    test_case_1 = [2, 3, 1, 1, 4]  # 2
    test_case_2 = [2, 3, 0, 1, 4]  # 2

    cls = Solution()
    ans = cls.jump(test_case_1)
    print("----")
    print(ans)
