# https://leetcode.com/problems/find-closest-node-to-given-two-nodes
"""
Good problem but it has a lot of steps you need to compute before attempting to solve the answer.

1. First construct the adjacency list
2. Run BFS from each of the starting nodes and collect the paths taken
3. Find all of the common nodes along the paths for both of those starting nodes
4. Find the first node that they meet at
"""

from collections import defaultdict
from typing import TypedDict


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        # Create the adjacency list from the provided edges where each index is the node
        adj: dict[int, list[int]] = defaultdict(list)
        for src, dest in enumerate(edges):
            adj[src].append(dest)
            if dest == -1:
                adj[src].pop()

        def bfs(node: int):
            queue: list[int] = [node]
            levels: list[set[int]] = []
            visited: set[int] = set()
            while queue:
                current_level: set[int] = set()
                n = len(queue)
                for _ in range(n):
                    current_node = queue.pop(0)
                    visited.add(current_node)
                    current_level.add(current_node)

                    for nei in adj[current_node]:
                        if nei not in visited:
                            queue.append(nei)

                levels.append(current_level)

            return levels, visited

        node1_levels, visited1 = bfs(node=node1)
        node2_levels, visited2 = bfs(node=node2)

        # Get the collection of nodes that can be reached from both nodes
        global_common = visited1.intersection(visited2)

        # This means there are no common nodes in the paths visited
        if len(global_common) == 0:
            return -1

        # Only one common means we don't need to try to find the most optimal answer
        if len(global_common) == 1:
            return min(global_common)

        found = {node: [0, 0] for node in global_common}
        for i, level in enumerate(node1_levels):
            common = level.intersection(global_common)
            if len(common) > 0:
                for common_node in common:
                    found[common_node][0] = i
        for i, level in enumerate(node2_levels):
            common = level.intersection(global_common)
            if len(common) > 0:
                for common_node in common:
                    found[common_node][1] = i

        # Sort the keys in the found dictionary so that we always start
        # with the smaller nodes
        found_keys = list(found.keys())
        found_keys.sort()

        res = float("inf")
        max_distance = float("inf")
        # for common_node, (distance_1, distance_2) in found.items():
        for common_node in found_keys:
            distance_1, distance_2 = found[common_node]
            if max(distance_1, distance_2) < max_distance:
                res = common_node
                max_distance = max(distance_1, distance_2)

        return -1 if res == float("inf") else int(res)


if __name__ == "__main__":

    class TestCase(TypedDict):
        edges: list[int]
        node1: int
        node2: int

    test_case_1: TestCase = {
        "edges": [2, 2, 3, -1],
        "node1": 0,
        "node2": 1,
    }  # 2

    test_case_2: TestCase = {
        "edges": [1, 2, -1],
        "node1": 0,
        "node2": 2,
    }  # 2

    test_case_3: TestCase = {
        "edges": [4, 4, 4, 5, 1, 2, 2],
        "node1": 1,
        "node2": 1,
    }  # 1

    test_case_4: TestCase = {
        "edges": [4, 4, 8, -1, 9, 8, 4, 4, 1, 1],
        "node1": 5,
        "node2": 6,
    }  # 1

    test_case_5: TestCase = {
        "edges": [4, 3, 0, 5, 3, -1],
        "node1": 4,
        "node2": 0,
    }  # 4

    test_case_6: TestCase = {
        "edges": [2, 0, 0],
        "node1": 2,
        "node2": 0,
    }  # 0

    cls = Solution()
    ans = cls.closestMeetingNode(**test_case_4)
    print("-------")
    print(ans)
