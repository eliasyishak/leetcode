# https://leetcode.com/problems/most-profitable-path-in-a-tree
"""
Challenging problem for sure, this is essentially having to do two
independent BFS calls for both Bob and Alice. First find Bob's path,
(he will only have one based on the problem description) and then
use that information to check each of Alice's steps in her traversal.
"""

from collections import defaultdict
from typing import TypedDict


class TestCaseInput(TypedDict):
    edges: list[list[int]]
    bob: int
    amount: list[int]


class Solution:
    def __init__(self) -> None:
        self.adjs: dict[int, list[int]] = defaultdict(list)
        self.amount: list[int] = []

    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        for a, b in edges:
            self.adjs[a].append(b)
            self.adjs[b].append(a)

        # Identify the leaf nodes
        leaf_nodes = set(
            val
            for val, neighbors in self.adjs.items()
            if len(neighbors) == 1 and val != 0
        )

        # We begin by first finding the shortest path for Bob to take
        # to go from his current node to node 0
        bobs_path = {
            val: index
            for index, val in enumerate(self.bfs(curr_node=bob, target=set([0])))
        }

        # Begin traversing the graph from Alice's starting position while also
        # traversing bobs_path
        alice_visited: set[int] = set()
        queue: list[tuple[int, int, int]] = [(0, 0, 0)]  # node, curr_price, seconds
        res: list[int] = []
        while queue:
            alice_node, curr_price, seconds = queue.pop(0)

            node_amount = amount[alice_node]
            if alice_node in bobs_path:
                if bobs_path[alice_node] == seconds:
                    node_amount = int(node_amount / 2)
                elif bobs_path[alice_node] < seconds:
                    node_amount = 0

            if alice_node in alice_visited:
                continue
            alice_visited.add(alice_node)

            if alice_node in leaf_nodes:
                res.append(curr_price + node_amount)

            for nei in self.adjs[alice_node]:
                if nei not in alice_visited:
                    queue.append((nei, curr_price + node_amount, seconds + 1))

        return max(res)

    def bfs(self, curr_node: int, target: set[int]) -> list[int]:
        visited: set[int] = set()

        queue: list[tuple[int, list[int]]] = [(curr_node, [])]
        while queue:
            curr_node, curr_path = queue.pop(0)

            if curr_node in target:
                return [*curr_path, curr_node]

            if curr_node in visited:
                continue

            visited.add(curr_node)
            for nei in self.adjs[curr_node]:
                if nei not in visited:
                    queue.append((nei, [*curr_path, curr_node]))

        return []


if __name__ == "__main__":
    test_case_1 = TestCaseInput(
        edges=[
            [0, 1],
            [1, 2],
            [1, 3],
            [3, 4],
        ],
        amount=[-2, 4, 2, -4, 6],
        bob=3,
    )  # 6

    test_case_2 = TestCaseInput(
        edges=[[0, 1]],
        amount=[-7280, 2350],
        bob=1,
    )  # -7280

    cls = Solution()
    ans = cls.mostProfitablePath(**test_case_2)
    print("------")
    print(ans)
