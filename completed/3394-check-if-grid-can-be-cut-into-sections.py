# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections
"""
Fairly straightforward intervals problem. The key insight is in the comment on
line 16.
"""


class Solution:
    def checkValidCuts(self, rectangles: list[list[int]]) -> bool:
        xaxis = [(r[0], r[2]) for r in rectangles]
        yaxis = [(r[1], r[3]) for r in rectangles]

        xaxis.sort()
        yaxis.sort()

        def helper(arr: list[tuple[int, int]]) -> int:
            # We start at -1 so we can count the first interval; we are
            # counting regions that are blocked off by a non-overlap boundary
            prev_end = -1
            count = 0
            for start, end in arr:
                if prev_end <= start:
                    count += 1

                prev_end = max(prev_end, end)

            return count

        return max(helper(xaxis), helper(yaxis)) >= 3


if __name__ == "__main__":
    test_case_1 = [
        [1, 0, 5, 2],
        [0, 2, 2, 4],
        [3, 2, 5, 3],
        [0, 4, 4, 5],
    ]  # true

    cls = Solution()
    ans = cls.checkValidCuts(test_case_1)
    print("------")
    print(ans)
