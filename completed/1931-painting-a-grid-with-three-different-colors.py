# https://leetcode.com/problems/painting-a-grid-with-three-different-colors
"""
Tough DP problem that could be done with backtracking without any memoization
as well as standard DP approach.

Working through both solutions was valuable.
"""


class Solution:
    def colorTheGridDFS(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        grid = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def backtrack(i: int, j: int) -> int:
            # Condition for moving down a row
            if j == COLS:
                j = 0
                i += 1

            # Base case; we have completed each cell in the grid
            if i == ROWS:
                return 1

            total = 0
            for color in range(3):
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == color:
                    continue

                # Check the cell above
                if i > 0 and grid[i - 1][j] == color:
                    continue

                grid[i][j] = color
                total += backtrack(i=i, j=j + 1)

            return total

        return backtrack(i=0, j=0)

    def __init__(self) -> None:
        self.valid_columns: list[tuple[int, ...]] = []

    def colorTheGrid(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        MOD = 10**9 + 7

        def get_valid_columns(curr: list[int]):
            """
            Recursive, backtracking approach to
            getting all valid column combinations
            """
            if len(curr) == ROWS:
                self.valid_columns.append(tuple(curr))
                return

            for color in range(3):
                if len(curr) > 0 and curr[-1] == color:
                    continue
                curr.append(color)
                get_valid_columns(curr)
                curr.pop()

        get_valid_columns([])

        # Create a look up object that has each valid column as
        # a key and a list of columns that can be next that key
        # list as the value of the object
        lookup: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
        for option1 in self.valid_columns:
            lookup[option1] = []

            for option2 in self.valid_columns:
                if sum([option1[i] == option2[i] for i in range(ROWS)]) == 0:
                    lookup[option1].append(option2)

        cache: dict[tuple[int, tuple[int, ...]], int] = {}

        def dp(j: int, prev: tuple[int, ...]) -> int:
            if j == COLS:
                return 1

            if (j, prev) in cache:
                return cache[(j, prev)]

            total = 0
            for next_valid_col in lookup[prev]:
                total += dp(j=j + 1, prev=next_valid_col) % MOD

            cache[(j, prev)] = total
            return cache[(j, prev)]

        res = 0
        for first_col in self.valid_columns:
            res += dp(j=1, prev=first_col) % MOD

        return res % MOD


if __name__ == "__main__":
    test_case_1 = {
        "m": 2,
        "n": 2,
    }  # 18

    test_case_2 = {
        "m": 5,
        "n": 5,
    }  # 580_986

    test_case_3 = {
        "m": 2,
        "n": 37,
    }  # 1478020098

    cls = Solution()
    ans = cls.colorTheGrid(**test_case_3)
    print("------")
    print(ans)
