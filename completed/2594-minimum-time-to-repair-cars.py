# https://leetcode.com/problems/minimum-time-to-repair-cars
"""
Another great binary search problem to continue to learn how search spaces
are more than just data structures. In this problem, we try to guess how long it
will take for a job to be done and try to use math to see if we can achieve the
number of cars we need.
"""

from typing import TypedDict


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        lower_bound = 1
        # We can use any of the ranks from the list as the upperbound
        # because the answer will be lower than any one mechanic fixing
        # all of the cars
        upper_bound = ranks[0] * cars**2
        res = upper_bound

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            # Determine how many cars can be fixed by each mechanic
            # in the provided time
            #
            # If the sum of all of the cars they can finish within a
            # a given time exceeds the number of cars, then we will
            # continue to search the search space to the left
            curr_cars_fixed = 0
            for rank in ranks:
                curr_cars_fixed += ((mid / rank) ** 0.5) // 1

            if curr_cars_fixed >= cars:
                res = mid
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return res


class TestCaseType(TypedDict):
    ranks: list[int]
    cars: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "ranks": [4, 3, 2, 1],
        "cars": 10,
    }  # 16

    cls = Solution()
    ans = cls.repairCars(**test_case_1)
    print("------")
    print(ans)
