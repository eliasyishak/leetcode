# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        nodes = {i: [i + 1] if i < n - 1 else [] for i in range(n)}

        res = []
        for from_node, to_node in queries:
            nodes[from_node].append(to_node)

            queue = [(0, 0)]
            visited = set()
            while queue:
                current_node, jumps = queue.pop(0)
                visited.add(current_node)

                if current_node == n - 1:
                    res.append(jumps)
                    break

                # Append the next possible nodes based on the nodes we can reach
                for next_node in nodes[current_node]:
                    if next_node not in visited:
                        queue.append((next_node, jumps + 1))

        return res


if __name__ == "__main__":
    test_case_1 = {"n": 5, "queries": [[2, 4], [0, 2], [0, 4]]}  # [3, 2, 1]

    test_case = test_case_1

    cls = Solution()
    print(
        cls.shortestDistanceAfterQueries(n=test_case["n"], queries=test_case["queries"])
    )
