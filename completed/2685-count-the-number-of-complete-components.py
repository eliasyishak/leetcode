# https://leetcode.com/problems/count-the-number-of-complete-components
"""
Feels like a straightforward graph problem that we can use BFS or DFS (I used
BFS) to traverse the entire graph and collect the different components based on
the adjacency list that we preprocess.

The trick here is that each node should be able to visit every node in the connected
component, so once we create our components, we can check each node's adjacency list
to ensure that the length of neighbors is equal to the total number of nodes in the component
minus one
"""

from typing import TypedDict


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Create the adjacency list for each node
        adj: dict[int, list[int]] = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Perform BFS on each node
        component_info = {}
        comp_index = 0
        visited: set[int] = set()
        for node in range(n):
            if node not in visited:
                component_info[comp_index] = set([node])
                visited.add(node)

                queue: list[int] = [*adj[node]]
                while queue:
                    next_node = queue.pop(0)
                    visited.add(next_node)
                    component_info[comp_index].add(next_node)

                    for nei in adj[next_node]:
                        if nei not in visited:
                            queue.append(nei)

                comp_index += 1

        # Iterate through each of the components and check against the
        # adjacency list that each node has the correct number of neighbors
        res = 0
        for _, node_list in component_info.items():
            valid = True
            for node in node_list:
                if len(adj[node]) != len(node_list) - 1:
                    valid = False
                    continue

            if valid:
                res += 1

        return res


class TestCaseType(TypedDict):
    n: int
    edges: list[list[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "n": 6,
        "edges": [[0, 1], [0, 2], [1, 2], [3, 4]],
    }  # 3

    test_case_2: TestCaseType = {
        "n": 6,
        "edges": [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]],
    }  # 1

    cls = Solution()
    ans = cls.countCompleteComponents(**test_case_2)
    print("-------")
    print(ans)
