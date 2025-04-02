"""
It's been a while since I did some problems, this one is close enough for me
that I don't want to spend more time on it. My solution passes a few test cases
but not all.

Including the LC solution as well
"""

import heapq
from queue import PriorityQueue
from typing import TypedDict


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Sort the queries so that we are checking the small
        # queries first; this allows us to do only BFS
        queries_processed: list[tuple[int, int]] = [
            (val, i) for i, val in enumerate(queries)
        ]
        queries_processed.sort()

        # Use a heap to begin in the top left corner and search for the smallest
        # valued neighbor for the next cell to visit
        heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]  # [cell_value, i, j]

        directions = [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
        ]

        # Define the current index we are for queries
        index = 0
        points = 0
        res: list[int] = [0] * len(queries_processed)
        visited: set[tuple[int, int]] = set()
        while heap and index < len(res):
            cell_value, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue

            visited.add((i, j))

            # Condition for remaining on the same query but increasing the score
            if cell_value < queries_processed[index][0]:
                points += 1

                # Get the neighbors to visit next
                for x, y in directions:
                    next_i, next_j = i + x, j + y
                    if (
                        0 <= next_i < ROWS
                        and 0 <= next_j < COLS
                        and (next_i, next_j) not in visited
                    ):
                        heapq.heappush(
                            heap,
                            (grid[next_i][next_j], next_i, next_j),
                        )

            # Condition for moving to the next query (if possible)
            elif cell_value >= queries_processed[index][0]:
                # Record the score of the current query index before moving
                # to the next one
                res[queries_processed[index][1]] = points
                index += 1

                # Add the current cell back into the heap and remove it
                # from the visited set so we can process it again
                heapq.heappush(
                    heap,
                    (cell_value, i, j),
                )
                visited.remove((i, j))

        return res

    def maxPointsLC(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        row_count, col_count = len(grid), len(grid[0])
        result = [0] * len(queries)
        # Directions for movement (right, down, left, up)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Store queries along with their original indices to restore order
        # later
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        # Min-heap (priority queue) to process cells in increasing order of
        # value
        min_heap: PriorityQueue[tuple[int, int, int]] = PriorityQueue()
        visited = [[False] * col_count for _ in range(row_count)]
        # Keeps track of the number of cells processed
        total_points = 0
        # Start from the top-left cell
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = True

        # Process queries in sorted order
        for query_value, query_index in sorted_queries:
            # Expand the cells that are smaller than the current query value
            while not min_heap.empty() and min_heap.queue[0][0] < query_value:
                cellValue, current_row, current_col = min_heap.get()

                # Increment count of valid cells
                total_points += 1

                # Explore all four possible directions
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = (
                        current_row + row_offset,
                        current_col + col_offset,
                    )

                    # Check if the new cell is within bounds and not visited
                    if (
                        new_row >= 0
                        and new_col >= 0
                        and new_row < row_count
                        and new_col < col_count
                        and not visited[new_row][new_col]
                    ):
                        min_heap.put((grid[new_row][new_col], new_row, new_col))
                        # Mark as visited
                        visited[new_row][new_col] = True
            # Store the result for this query
            result[query_index] = total_points

        return result


class TestCaseType(TypedDict):
    grid: list[list[int]]
    queries: list[int]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "grid": [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
        "queries": [5, 6, 2],
    }  # [5, 8, 1]

    test_case_2: TestCaseType = {
        "grid": [[5, 2, 1], [1, 1, 2]],
        "queries": [3],
    }  # [0]

    cls = Solution()
    ans = cls.maxPoints(**test_case_1)
    print("------")
    print(ans)
