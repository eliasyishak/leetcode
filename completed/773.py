# https://leetcode.com/problems/sliding-puzzle
"""
Not the most efficient code, we could have taken some shortcuts because we know that
the grid will be limited to 2 x 3, but this works for me :)
"""

from typing import List


class Solution:
    def __init__(self):
        self.ROWS = 2
        self.COLS = 3

    def findZero(self, board):
        # Find the position of the current zero
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if board[i][j] == 0:
                    return [i, j]

    def copy_board(self, board):
        return [[cell for cell in row] for row in board]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Create a list to hold the board layouts we have seen
        boards_checked = []

        transforms = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1],
        ]

        queue = [(board, 0)]
        while queue:
            cur, moves = queue.pop(0)

            if cur == [[1, 2, 3], [4, 5, 0]]:
                return moves

            i, j = self.findZero(cur)
            boards_checked.append(cur)

            for x, y in transforms:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < self.ROWS and 0 <= new_j < self.COLS:
                    temp_board = self.copy_board(cur)
                    temp_board[i][j] = cur[new_i][new_j]
                    temp_board[new_i][new_j] = 0

                    if temp_board not in boards_checked:
                        queue.append((temp_board, moves + 1))

        return -1


if __name__ == "__main__":
    test_case_1 = [[1, 2, 3], [4, 0, 5]]  # 1
    test_case_2 = [[1, 2, 3], [5, 4, 0]]  # -1 (not possible)
    test_case_3 = [[4, 1, 2], [5, 0, 3]]  # 5

    test_case = test_case_3
    cls = Solution()
    ans = cls.slidingPuzzle(board=test_case)

    print("ANS =", ans)
