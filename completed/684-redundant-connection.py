# https://leetcode.com/problems/redundant-connection
"""
To solve this problem, consider starting from each src and target in the edges list.

Traverse this edges array backwards so that the first pair we encounter we can remove
is the correct answer.

To solve this, we need to find edges that we can reach the target twice.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(current: int, target: int, visited: set[int]) -> int:
            if current == target:
                return 1

            visited.add(current)

            res: list[int] = []
            for neighbor in adj[current]:
                if neighbor == target or neighbor not in visited:
                    res.append(dfs(neighbor, target, visited))

            return sum(res)

        adj: dict[int, list[int]] = defaultdict(list)
        for src, target in edges:
            adj[src].append(target)
            adj[target].append(src)

        for src, target in edges[::-1]:
            # If we can reach the target twice, that means we can remove one of the edges
            # for that target and we would have our acyclic graph
            if dfs(src, target, set()) == 2:
                return [src, target]

        return []


if __name__ == "__main__":
    test_case_1 = [[1, 2], [1, 3], [2, 3]]  # [2,3]
    test_case_2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]  # [1,4]

    cls = Solution()
    ans = cls.findRedundantConnection(test_case_2)
    print("-----")
    print(ans)
