# https://leetcode.com/problems/grid-game
"""
The trick to this problem is not to go down the path I did with WRONGgridGameWRONG

Instead, understand that the problem can be solved when you think of choosing
a path as splitting the grid into two pieces. Honestly too much to explain, it is
explained very well here: https://www.youtube.com/watch?v=B90kG-ZlptE&ab_channel=NeetCodeIO
"""

from typing import List, Tuple


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])

        top = [0] * COLS
        bottom = [0] * COLS
        for i in range(COLS):
            if i == 0:
                top[i] = grid[0][i]
                bottom[i] = grid[1][i]
            else:
                top[i] = top[i - 1] + grid[0][i]
                bottom[i] = bottom[i - 1] + grid[1][i]

        top_sum = top[-1]
        bottom_sum = bottom[-1]

        bot_2_min = top_sum - grid[0][0]
        for i in range(COLS):
            # We immediately go down
            if i == 0:
                bot_2_min = min(bot_2_min, top_sum - grid[0][0])
            # We go down in the last row
            elif i == COLS - 1:
                bot_2_min = min(bot_2_min, bottom_sum - grid[-1][-1])
            # Everything in between
            else:
                # We need to get the top half and second half
                top_half = top_sum - top[i]
                bottom_half = bottom[i - 1]

                bot_2_min = min(bot_2_min, max(top_half, bottom_half))

        return bot_2_min

    def WRONGgridGameWRONG(self, grid: List[List[int]]) -> int:
        """
        This solution is wrong because I assumed that the first robot wants
        to take the path that makes it collect the most points... this is not
        a correct assumption. This may be the case for the examples provided, but
        what we want to do is take the path that ensures we minimize the second bot's
        score. This may result in a path taken by the first bot that does not result
        in the max points collected.
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs() -> List[Tuple[int, int]]:
            # Perform BFS to find the path that collects the most points
            queue: List[
                Tuple[
                    int,
                    int,
                    int,
                    List[Tuple[int, int]],
                ]
            ] = [(0, 0, grid[0][0], [(0, 0)])]
            bot = []
            while queue:
                q_len = len(queue)
                for _ in range(q_len):
                    i, j, points, path = queue.pop(0)

                    if i == ROWS - 1 and j == COLS - 1:
                        bot.append((points, path))

                    # Append the cell to the right
                    if j + 1 < COLS:
                        queue.append(
                            (i, j + 1, points + grid[i][j + 1], [*path, (i, j + 1)])
                        )

                    # Append the cell to teh bottom
                    if i + 1 < ROWS:
                        queue.append(
                            (i + 1, j, points + grid[i + 1][j], [*path, (i + 1, j)])
                        )

            return max(bot)[-1]

        # Get the path that returns the maximum amount of points collected
        bot_1 = bfs()

        # Take the path with the most points and set those values to be zero
        for i, j in bot_1:
            grid[i][j] = 0

        # Now perform the same BFS approach but take the path that is least
        bot_2 = bfs()
        res = 0
        for i, j in bot_2:
            res += grid[i][j]

        return res


if __name__ == "__main__":
    test_case_1 = [[2, 5, 4], [1, 5, 1]]  # 4
    test_case_2 = [[3, 3, 1], [8, 5, 2]]  # 4
    test_case_3 = [[1, 3, 1, 15], [1, 3, 3, 1]]  # 7
    test_case_4 = [
        [20, 3, 20, 17, 2, 12, 15, 17, 4, 15],
        [20, 10, 13, 14, 15, 5, 2, 3, 14, 3],
    ]  # 63

    cls = Solution()
    ans = cls.gridGame(test_case_4)
    print("-----")
    print(ans)
