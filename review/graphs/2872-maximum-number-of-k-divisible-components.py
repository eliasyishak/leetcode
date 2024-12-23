# https://leetcode.com/problems/maximum-number-of-k-divisible-components
"""
A very challenging problem to understand, it requires a lot more thought than just
programming, you have to understand the properties behind graphs and subtrees

Great explanations below
- https://youtu.be/uXz9VUVBes0?si=HlrgHOZLNbvwPeOO
- https://youtu.be/xlgOaIK-inc?si=yE1MA2gdkJ5ipu2k
"""

from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        if n == 1:
            return n

        adj = {}
        for node_1, node_2 in edges:
            if node_1 not in adj:
                adj[node_1] = []
            if node_2 not in adj:
                adj[node_2] = []

            adj[node_1].append(node_2)
            adj[node_2].append(node_1)

        def dfs(node, parent):
            print(node, [val for val in adj[node] if val != parent])
            total = values[node]

            for child in adj[node]:
                if child != parent:
                    total += dfs(child, node)

            print("**", node, "-->", total, end="\n\n")
            if total % k == 0:
                self.res += 1

            return total

        dfs(0, None)
        return self.res


if __name__ == "__main__":
    test_case_1 = {
        "n": 5,
        "k": 6,
        "edges": [[0, 2], [1, 2], [1, 3], [2, 4]],
        "values": [1, 8, 1, 4, 4],
    }  # 2
    test_case_2 = {
        "n": 7,
        "k": 3,
        "edges": [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
        "values": [3, 0, 6, 1, 5, 2, 1],
    }  # 3

    cls = Solution()
    ans = cls.maxKDivisibleComponents(**test_case_1)
    print("-----")
    print(ans)
