# https://leetcode.com/problems/maximum-matrix-sum
from typing import List


class Solution:
    def max_matrix_sum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        matrix_sum = 0
        negatives = 0
        min_value = float("infinity")
        for i in range(ROWS):
            for j in range(COLS):
                cell_value = matrix[i][j]
                matrix_sum += abs(cell_value)
                if cell_value < 0:
                    negatives += 1
                if abs(cell_value) < min_value:
                    min_value = abs(cell_value)

        # If we have an odd number of negatives, that means the smallest
        # value we have found in the matrix will need to be taken from the sum
        #
        # Important to note that we need to reduce the total sum by DOUBLE the min
        # value, it is not enough to just subtract it once since that would only
        # make it look like the cell didn't exist
        if negatives % 2 == 1:
            matrix_sum -= 2 * abs(min_value)

        return matrix_sum


if __name__ == "__main__":
    test_case_1 = [[1, -1], [-1, 1]]
    test_case_2 = [[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]
    test_case_3 = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]  # 16
    test_case_4 = [[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]  # 15

    cls = Solution()
    print(cls.max_matrix_sum(matrix=test_case_4))
