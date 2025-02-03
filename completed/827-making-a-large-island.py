"""
Conceptually this was not a difficult problem. Creating the solution for this
problem was a bit verbose and could probably be refactored if I wanted but this passed
on the first try :)

The idea here is to first find all of the islands and associate a group with each island.
That group will then have a island ID assigned to them to associate their size. We then
iterate through all the non-island cells and look at the neighbors and see how big of an
island we can create if we flipped that island and summing it with the size of the neighboring
islands.
"""

from typing import List, Optional


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        # Create a copy of the grid so that we can mark the group
        # that current cell belongs to
        curr_island = -1
        islands: List[List[Optional[int]]] = [[None for _ in row] for row in grid]
        visited: set[tuple[int, int]] = set()

        def bfs(i, j) -> int:
            queue: List[tuple[int, int]] = [(i, j)]
            size = 0
            while queue:
                i, j = queue.pop(0)

                if (i, j) in visited:
                    continue

                size += 1

                # Mark the group it belongs to in the copied grid
                islands[i][j] = curr_island
                visited.add((i, j))

                for x, y in directions:
                    next_i, next_j = i + x, j + y
                    if (
                        0 <= next_i < ROWS
                        and 0 <= next_j < COLS
                        and (next_i, next_j) not in visited
                        and grid[next_i][next_j] == 1
                    ):
                        queue.append((next_i, next_j))

            return size

        # The first iteration will identify all of the islands we currently have
        size_by_island: dict[int, int] = {}
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    curr_island += 1
                    size = bfs(i, j)

                    size_by_island[curr_island] = size

        # The second iteration will look at all the spaces that are not
        # land and calculate how big of an island we would have if we flipped
        # that current cell
        res = max(size_by_island.values()) if len(size_by_island) > 0 else 0
        # If we don't have any islands, than the biggest island we can make is one
        if res == 0:
            return 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    # Check in all 4 directions for the island sizes
                    neighbor_size = 0
                    islands_visited: set[int] = set()
                    for x, y in directions:
                        next_i, next_j = i + x, j + y

                        if (
                            0 <= next_i < ROWS
                            and 0 <= next_j < COLS
                            and grid[next_i][next_j] == 1
                        ):
                            island_id = islands[next_i][next_j]
                            if (
                                island_id is not None
                                and island_id not in islands_visited
                            ):
                                neighbor_size += size_by_island[island_id]
                                islands_visited.add(island_id)

                    res = max(res, neighbor_size + 1)

        return res


if __name__ == "__main__":
    test_case_1 = [
        [1, 0],
        [0, 1],
    ]  # 3

    test_case_2 = [
        [1, 1],
        [1, 0],
    ]  # 4

    test_case_3 = [
        [1, 1],
        [1, 1],
    ]  # 4

    test_case_4 = [
        [0, 0],
        [0, 0],
    ]

    cls = Solution()
    ans = cls.largestIsland(test_case_4)
    print("-----")
    print(ans)
