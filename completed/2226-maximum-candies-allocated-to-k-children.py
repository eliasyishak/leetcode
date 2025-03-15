# https://leetcode.com/problems/maximum-candies-allocated-to-k-children
"""
The trick to solving these binary search problems is to first try to
solve them in linear time which is what I did. I had defined my upper bound
and started at that point and tried to give out the candy. The solution worked
for the provided test cases but failed on TLE for the submission.

This was due to the large input constraints. At that point, you start to think
of optimizing the `amount_per_child` variable by using binary search.
"""

from typing import TypedDict


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        total = sum(candies)

        # Defines the most we could give everyone given the total
        lower_bound = 1
        upper_bound = total // k

        res = 0

        while lower_bound <= upper_bound:
            # the mid value for binary search
            amount_per_child = (upper_bound + lower_bound) // 2
            print(amount_per_child)

            piles_made = 0

            for candy in candies:
                # The current pile is more than we need
                if candy >= amount_per_child:
                    piles_made += candy // amount_per_child

                # The current pile does not have enough
                else:
                    pass

            # If we have made enough piles, we could try to increase the
            # the number of candy we give out by searching to the right
            if piles_made >= k:
                res = max(res, amount_per_child)
                lower_bound = amount_per_child + 1
            # If we fail to make enough piles, we need to decrease the
            # amount of candy we give out and search to the left of mid
            else:
                upper_bound = amount_per_child - 1

        return res


class TestCaseType(TypedDict):
    candies: list[int]
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "candies": [5, 8, 6],
        "k": 3,
    }  # 5

    test_case_2: TestCaseType = {
        "candies": [4, 7, 5],
        "k": 4,
    }  # 3

    test_case_3: TestCaseType = {
        "candies": [5, 6, 4, 10, 10, 1, 1, 2, 2, 2],
        "k": 9,
    }  # 3

    cls = Solution()
    ans = cls.maximumCandies(**test_case_1)
    print("-----")
    print(ans)
