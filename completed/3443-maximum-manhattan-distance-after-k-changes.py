# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes
"""
Use a greedy approach to try to maximize the distance. We try to go in all four
diagonal directions away from the point of origin.
"""

from typing import TypedDict


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # The list below will emphasis each direction we want to try to maximize
        directions = ["NW", "NE", "SE", "SW"]

        res = 0
        for direction in directions:
            remaining = k
            curr_distance = 0
            for char in s:
                # If character is in the direction string, that means
                # we will be swapping; we could do the opposite as well
                # since we will be checking all directions equally
                if char in direction:
                    if remaining > 0:
                        curr_distance += 1
                        remaining -= 1
                    else:
                        curr_distance -= 1
                else:
                    curr_distance += 1

                res = max(res, curr_distance)

        return res


if __name__ == "__main__":

    class TestCase(TypedDict):
        s: str
        k: int

    test_case_1: TestCase = {
        "s": "NSWWEW",
        "k": 3,
    }  # 6

    test_case_2: TestCase = {
        "s": "NWSE",
        "k": 1,
    }  # 3

    cls = Solution()
    ans = cls.maxDistance(**test_case_2)
    print("------")
    print(ans)
