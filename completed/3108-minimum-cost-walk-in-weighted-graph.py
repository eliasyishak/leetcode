# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph
"""
The key takeaway from this problem is understanding the nature of what
a bitwise AND operation does to a value. When you bitwise two numbers
together, the max return value will be one of the numbers or LESS

x & y = z   where z will always be either equal to x or y or LESS

So to minimize the cost, we will visit all paths in the connected component,
this may seem uninituitive if we are trying to minimize "distance" traveled
but having this cost be based on the AND operation changes that understanding.

1. Create a dictionary that maps each node to a component
{
    "n1": "component_1",
    "n2": "component_1",
    "n3": "component_2",
    "n4": "component_2"
}

2. Create a dictionary maps each component to the total cost (all of the
    costs AND'ed together)
{
    "component_1": 5,
    "component_2": 1,
}

3. Iterate through the queries and use the dictionary from 2 to get an answer;
    if the 2 nodes belong to different groups then it won't be possible to traverse
    the graph though and results in -1

"""

from typing import TypedDict


class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        # Create an adjaceny list
        adj: dict[int, list[int]] = {i: [] for i in range(n)}
        for n1, n2, _ in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def bfs() -> dict[int, int]:
            res: dict[int, int] = {}
            visited: set[int] = set()
            comp = 0
            for curr_node in range(n):
                if curr_node not in visited:
                    res[curr_node] = comp

                    queue = [*adj[curr_node]]

                    while queue:
                        node = queue.pop(0)
                        visited.add(node)
                        res[node] = comp

                        for nei in adj[node]:
                            if nei not in visited:
                                queue.append(nei)

                    comp += 1

            return res

        # Map each of the nodes to a component
        node_to_comp = bfs()

        # Iterate through the edges and get the bitwise AND operation
        # for each component
        cost_per_comp: dict[int, int] = {}
        for n1, _, cost in edges:
            # We don't need n2 because n1 and n2 will have
            # the same compnent mapped since they are connected
            comp = node_to_comp[n1]
            if comp not in cost_per_comp:
                cost_per_comp[comp] = cost
            else:
                cost_per_comp[comp] &= cost

        res: list[int] = []
        # Iterate through the queries and answer each of them using the cost to node
        # mapping
        for n1, n2 in query:
            if node_to_comp[n1] != node_to_comp[n2]:
                res.append(-1)
            else:
                res.append(cost_per_comp[node_to_comp[n1]])

        return res


class TestCaseType(TypedDict):
    n: int
    edges: list[list[int]]
    query: list[list[int]]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "n": 5,
        "edges": [
            [0, 1, 7],
            [1, 3, 7],
            [1, 2, 1],
        ],
        "query": [[0, 3], [3, 4]],
    }  # [1, -1]

    test_case_2: TestCaseType = {
        "n": 3,
        "edges": [
            [0, 2, 7],
            [0, 1, 15],
            [1, 2, 6],
            [1, 2, 1],
        ],
        "query": [[1, 2]],
    }  # [0]

    test_case_3: TestCaseType = {
        "n": 6,
        "edges": [[4, 0, 3]],
        "query": [
            [4, 0],
            [2, 3],
            [0, 4],
            [2, 0],
            [3, 1],
        ],
    }  # [3,-1,3,-1,-1]

    cls = Solution()
    ans = cls.minimumCost(**test_case_3)
    print("------")
    print(ans)
