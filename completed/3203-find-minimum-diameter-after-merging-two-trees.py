# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
"""
The key to this problem to understand what it means to combine two graphs and
calculating your diameter. The first important thing to understand is that you
are not merging the graphs at the node level, you are instead creating a bridge
between the two graphs, maintaining the same number of nodes total.

This code works for all the test cases but hits TLE at some point. For my approach,
I visited each node and calculated the max distance for that node while also maintaing
a variable tracking the graphs maximum diameter. Using these two values, the operation
will have a diameter that results in one of the following

The minimum possible diameter will be THE MAXIMUM of the following:
- The max diameter for graph 1
- The max diameter for graph 2
- Smallest distance in graph 1 + smallest distance in graph 2 + 1 (1 additional for the new edge)

The below code is accepted into leetcode.

```python
class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        # Calculate the number of nodes for each tree
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameters of both trees
        diameter1 = self.find_diameter(n, adj_list1)
        diameter2 = self.find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(self, n, adj_list):
        # First BFS to find the farthest node from an arbitrary node (e.g., 0)
        farthest_node, _ = self.find_farthest_node(n, adj_list, 0)

        # Second BFS to find the diameter starting from the farthest node
        _, diameter = self.find_farthest_node(n, adj_list, farthest_node)
        return diameter

    def find_farthest_node(self, n, adj_list, source_node):
        queue = deque([source_node])
        visited = [False] * n
        visited[source_node] = True

        maximum_distance = 0
        farthest_node = source_node

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                farthest_node = current_node

                for neighbor in adj_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if queue:
                maximum_distance += 1

        return farthest_node, maximum_distance
```

"""

from collections import defaultdict, deque
from typing import Dict, List


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        if len(edges1) == 0 and len(edges2) == 0:
            return 1

        adj1 = self.get_adjacency_list(edges1)
        adj2 = self.get_adjacency_list(edges2)

        min_distance_at_node_1, max_diameter_1 = self.preprocess(adj_obj=adj1)
        min_distance_at_node_2, max_diameter_2 = self.preprocess(adj_obj=adj2)

        return max(
            [
                max_diameter_1,
                max_diameter_2,
                min_distance_at_node_1 + min_distance_at_node_2 + 1,
            ]
        )

    def get_adjacency_list(self, edges: List[List[int]]) -> Dict[str, list]:
        obj = defaultdict(list)
        for n1, n2 in edges:
            obj[n1].append(n2)
            obj[n2].append(n1)

        return obj

    def preprocess(self, adj_obj):
        """
        This will take in the adjacency object and
        return the max diameter along with an array
        for each nodes longest path
        """
        n = len(adj_obj)
        max_diameter = -float("inf")
        min_diameter = float("inf")

        if n == 0:
            return 0, 0

        for i in range(n):
            curr = -1
            queue = deque([(i, 0, None)])

            while queue:
                node, distance, parent = queue.popleft()

                curr = max(curr, distance)
                for neighbor in adj_obj[node]:
                    if neighbor != parent:
                        queue.append((neighbor, distance + 1, node))

            min_diameter = min(min_diameter, curr)
            max_diameter = max(max_diameter, curr)

        return min_diameter, max_diameter


if __name__ == "__main__":
    test_case_1 = {
        "edges1": [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        "edges2": [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
    }  # 5
    test_case_2 = {
        "edges1": [[0, 1]],
        "edges2": [],
    }  # 2
    test_case_3 = {
        "edges1": [],
        "edges2": [[0, 1], [1, 2]],
    }  # 2

    cls = Solution()
    ans = cls.minimumDiameterAfterMerge(**test_case_3)
    print("------")
    print(ans)
