# https://leetcode.com/problems/find-eventual-safe-states
"""
Challenging problem labeled as a medium.

Initially, I tried to perform a BFS starting from the terminal nodes but this was
a bit of challenge. Instead, using a DFS approach starting from each node works better.
"""

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cache: dict[int, bool] = {}

        def dfs(i: int, visited: set[int]):
            if i in cache:
                return cache[i]

            if i in visited:
                return False

            visited.add(i)
            for next_node in graph[i]:
                if not dfs(next_node, visited):
                    cache[i] = False
                    return False

            cache[i] = True
            return True

        res: list[int] = []
        for i in range(n):
            if dfs(i, set()):
                res.append(i)

        return res


if __name__ == "__main__":
    test_case_1 = [[1, 2], [2, 3], [5], [0], [5], [], []]  # [2,4,5,6]
    test_case_2 = [[1], [2, 5], [], [1], [], [3], [3], [6]]  # [2,4]
    test_case_3 = [[], [0, 2, 3, 4], [3], [4], []]  # [0,1,2,3,4]

    cls = Solution()
    ans = cls.eventualSafeNodes(test_case_1)
    print("-----")
    print(ans)
