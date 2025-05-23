# https://leetcode.com/problems/minimum-falling-path-sum
"""
Great problem where the dp solution was actually easier than the slower
traversal approach using a flavor of djikstras algorithm. Drawing this
problem out makes it much easier to understand.
"""

import heapq


class Solution:
    def minFallingPathSumSlow(self, matrix: list[list[int]]) -> int:
        """
        This approach implements djisktra's algorithm to solve it. But this could
        potentially visit every cell so it is not the most time efficient or memory efficient
        approach.
        """
        n = len(matrix)
        min_cost: list[list[float]] = [[float("inf")] * n for _ in range(n)]
        heap: list[tuple[int, int, int]] = []
        for j, val in enumerate(matrix[0]):
            heapq.heappush(heap, (val, 0, j))
            min_cost[0][j] = val

        res = float("inf")
        while heap:
            curr_sum, i, j = heapq.heappop(heap)

            # If at last row, update result
            if i == n - 1:
                res = min(res, curr_sum)
                continue

            for column_offset in [-1, 0, 1]:
                next_i = i + 1
                next_j = j + column_offset
                if 0 <= next_i < n and 0 <= next_j < n:
                    next_sum = curr_sum + matrix[next_i][next_j]
                    if next_sum < min_cost[next_i][next_j]:
                        min_cost[next_i][next_j] = next_sum
                        heapq.heappush(heap, (next_sum, next_i, next_j))

        return int(res)

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)  # n x n matrix

        for i in range(1, n):  # Skip the first row since we are not updating anything
            for j in range(n):
                # Update the current cells value as the sum of the smallest neighbors above it

                # Only two cells to check for the leftmost cell
                if j == 0:
                    matrix[i][j] += min(
                        matrix[i - 1][j],
                        matrix[i - 1][j + 1],
                    )

                # Only two cells to check for the rightmost cell
                elif j == n - 1:
                    matrix[i][j] += min(
                        matrix[i - 1][j - 1],
                        matrix[i - 1][j],
                    )

                # The middle cells require us to check the top 3 cells above it
                else:
                    matrix[i][j] += min(
                        matrix[i - 1][j - 1],
                        matrix[i - 1][j],
                        matrix[i - 1][j + 1],
                    )

        return min(matrix[-1])  # Take the minimum from the last row


if __name__ == "__main__":
    test_case_1 = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9],
    ]  # 13

    test_case_2 = [
        [-19, 57],
        [-40, -5],
    ]  # -59

    test_case_3 = [
        [-51, -35, 74],
        [-62, 14, -53],
        [94, 61, -10],
    ]  # -98  -35 -> -53 -> -10

    cls = Solution()
    ans = cls.minFallingPathSum(test_case_3)
    print("--------")
    print(ans)
