# https://leetcode.com/problems/rotating-the-box
from typing import List


class Solution:
    def rotate_the_box(self, box: List[List[str]]) -> List[List[str]]:
        ROWS = len(box)
        COLS = len(box[0])

        for i in range(ROWS):
            right = COLS - 1
            left = right - 1
            while right >= 0 and left >= 0:
                right_val = box[i][right]
                left_val = box[i][left]

                # Ensure that the right spot is a valid spot we
                # can swap a value with
                if right_val != ".":
                    right -= 1
                    left -= 1
                elif left_val == ".":
                    left -= 1
                elif left_val == "#":
                    box[i][right] = "#"
                    box[i][left] = "."
                    right -= 1
                    left -= 1
                elif left_val == "*":
                    left -= 1
                    right = left

        # Rotating a matrix == Transposing entire matrix and then reversing each row
        transposed_box = [[None for _ in range(ROWS)] for _ in range(COLS)]
        for i in range(ROWS):
            for j in range(COLS):
                transposed_box[j][i] = box[i][j]

        rotated_box = [row[::-1] for row in transposed_box]

        return rotated_box


if __name__ == "__main__":
    test_case_1 = [["#", ".", ".", ".", "#"]]
    test_case_2 = [["#", ".", "*", "."], ["#", "#", "*", "."]]

    cls = Solution()
    cls.rotate_the_box(box=test_case_2)
