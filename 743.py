# https://leetcode.com/problems/network-delay-time
"""
This was not the daily problem for today but it was necessary to understand how
Dijkstra's algorthim worked to have a better understanding of how to solve
problem 2577
"""

from typing import List
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i + 1: [] for i in range(n)}
        for src, dest, t in times:
            edges[src].append((dest, t))

        heap = [(0, k)]  # node, time
        visited = set()
        total_time = 0
        while heap:
            time, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total_time = max(total_time, time)
            for next_node, next_time in edges[node]:
                if next_node not in visited:
                    heappush(heap, (time + next_time, next_node))

        return total_time if len(visited) == n else -1


if __name__ == "__main__":
    test_case_1 = {"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}

    test_case = test_case_1
    cls = Solution()
    ans = cls.networkDelayTime(
        k=test_case["k"], n=test_case["n"], times=test_case["times"]
    )
    print("----")
    print(ans)
