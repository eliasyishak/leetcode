# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet
import heapq
from typing import List


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        max_idx = []  # Min-heap to simulate priority queue
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        # Store the mappings for all queries in store_queries.
        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append((max(heights[a], heights[b]), idx))

        for idx, height in enumerate(heights):
            # If the heap's smallest value is less than the current height, it is an answer to the query.
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx
            # Push the queries with their maximum index as the current index into the heap.
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)

        return results


if __name__ == "__main__":
    test_case_1 = {
        "heights": [6, 4, 8, 5, 2, 7],
        "queries": [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
    }  # [2,5,-1,5,2]
    test_case_2 = {
        "heights": [3, 4, 1, 2],
        "queries": [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [3, 0],
            [3, 1],
            [3, 2],
            [3, 3],
        ],
    }  # [0,1,-1,-1,1,1,-1,-1,-1,-1,2,3,-1,-1,3,3]

    cls = Solution()
    ans = cls.leftmostBuildingQueries(**test_case_2)
    print("----")
    print(ans)
