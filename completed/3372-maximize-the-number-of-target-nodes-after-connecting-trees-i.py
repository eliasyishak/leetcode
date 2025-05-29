# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i
"""
Actually a great problem to learn from. The problem description provided was complete ass
but once you understand that it is really just a BFS problem on two trees, it becomes easier
to understand.
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def maxTargetNodes(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]],
        k: int,
    ) -> list[int]:
        def construct_adj(edges: list[list[int]]):
            adj: dict[int, list[int]] = defaultdict(list)
            for src, dest in edges:
                adj[src].append(dest)
                adj[dest].append(src)

            return adj

        adj1 = construct_adj(edges1)
        adj2 = construct_adj(edges2)

        def bfs(node: int, adj: dict[int, list[int]], hops: int) -> int:
            """
            Helper function to calculate the number of reachable
            nodes from the initial node
            """

            visited: set[int] = set()
            queue = [(node, 0)]
            reached = 0
            while queue:
                curr_node, curr_hops = queue.pop(0)
                visited.add(curr_node)
                reached += 1

                for nei in adj[curr_node]:
                    if nei not in visited and curr_hops + 1 <= hops:
                        queue.append((nei, curr_hops + 1))

            return reached

        # Get the number of neighbors for each node in tree1
        neighbors1 = [0] * len(adj1)
        for node in adj1:
            neighbors1[node] = bfs(node=node, adj=adj1, hops=k)

        # Get the number of neighbors from each node for tree2
        # at the distance of k - 1 hops away; we lose 1 avaiable
        # hop for tree2 because we are creating a link that takes up
        # one of the available hops
        #
        # We don't need to collect the neighbors in a list since we
        # only need the node that has the most neighbors
        max_neighbors = 0
        for node in adj2:
            max_neighbors = max(bfs(node=node, adj=adj2, hops=k - 1), max_neighbors)

        # If we don't have any hops available then we are just left
        # with the neighbors1 list
        if k == 0:
            return neighbors1

        return [nei1 + max_neighbors for nei1 in neighbors1]


if __name__ == "__main__":

    class TestCase(TypedDict):
        edges1: list[list[int]]
        edges2: list[list[int]]
        k: int

    test_case_1: TestCase = {
        "edges1": [[0, 1], [0, 2], [2, 3], [2, 4]],
        "edges2": [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        "k": 2,
    }  # [9, 7, 9, 8, 8]

    test_case_2: TestCase = {
        "edges1": [[0, 1]],
        "edges2": [[0, 1]],
        "k": 0,
    }  # [1, 1]

    cls = Solution()
    ans = cls.maxTargetNodes(**test_case_2)
    print("-------")
    print(ans)
