# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii
"""
Good follow up to the first variation of this problem but running into
TLE for this approach because the constraints are also larger. This is good
enough for me though :)
"""

from collections import defaultdict
from typing import Optional


class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        def construct_adj(edges: list[list[int]]):
            adj: dict[int, list[int]] = defaultdict(list)
            for src, dest in edges:
                adj[src].append(dest)
                adj[dest].append(src)

            return adj

        adj1 = construct_adj(edges1)
        adj2 = construct_adj(edges2)

        def dfs(
            node: int,
            prev: Optional[int],
            adj: dict[int, list[int]],
            hops: int,
        ) -> int:
            curr = 0
            for nei in adj[node]:
                if nei != prev:
                    curr += dfs(
                        node=nei,
                        adj=adj,
                        prev=node,
                        hops=hops + 1,
                    )

            return (1 if hops % 2 == 0 else 0) + curr

        # Go through each node in the first tree and return
        # the number of nodes that are an even number of nodes away
        # (includes the first node)
        first_tree = [0] * len(adj1)
        for node in adj1:
            first_tree[node] = dfs(
                node=node,
                prev=None,
                adj=adj1,
                hops=0,
            )

        # Go through the second tree and simply collect the node with
        # the maximum number of neighbors and even distance away
        max_node_neighbors = 0
        for node in adj2:
            curr = dfs(
                node=node,
                prev=None,
                adj=adj2,
                hops=1,
            )
            max_node_neighbors = max(curr, max_node_neighbors)

        return [node_neighbors + max_node_neighbors for node_neighbors in first_tree]


if __name__ == "__main__":
    test_case_1 = {
        "edges1": [
            [0, 1],
            [0, 2],
            [2, 3],
            [2, 4],
        ],
        "edges2": [
            [0, 1],
            [0, 2],
            [0, 3],
            [2, 7],
            [1, 4],
            [4, 5],
            [4, 6],
        ],
    }  # [8,7,7,8,8]
    """
    For i = 0, connect node 0 from the first tree to node 0 from the second tree.
    For i = 1, connect node 1 from the first tree to node 4 from the second tree.
    For i = 2, connect node 2 from the first tree to node 7 from the second tree.
    For i = 3, connect node 3 from the first tree to node 0 from the second tree.
    For i = 4, connect node 4 from the first tree to node 4 from the second tree.
    
    """

    cls = Solution()
    ans = cls.maxTargetNodes(**test_case_1)
    print("-------")
    print(ans)
