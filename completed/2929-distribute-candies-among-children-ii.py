# https://leetcode.com/problems/distribute-candies-among-children-ii
"""
This one is messing my brain up. Took me a while to figure out what was
happening but the key insight to understand here is in the candy2_min/max
calculation.

After the first loop, you simply only need to count how many different ways you
can distribute candy2, which leaves candy3 to just be the leftover.

So for testcase 1, when candy1 == 1, candy2 MUST be 2
... therefore candy2_max = candy2_min = 2, which means there is only
    ONE way to distribute candy2 when candy1 = 1
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0

        # The top loop determines how many candy items we can give
        # to the first child
        for candy1 in range(min(n, limit) + 1):
            candy_after_child1 = n - candy1

            # If we find that the total number of candies leftover for child2 and child3
            # is greater than double the limit, then it will not be possible to fully distribute
            # all candies so we continue past the current iteration
            #
            # We do 2 times the limit because child2 and child3 can only accept up the limit
            if candy_after_child1 > 2 * limit:
                continue

            candy2_max = min(n - candy1, limit)
            candy2_min = max(0, candy_after_child1 - limit)

            res += (candy2_max - candy2_min) + 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "n": 5,
        "limit": 2,
    }  # 3

    test_case_2 = {
        "n": 3,
        "limit": 3,
    }  # 10

    cls = Solution()
    ans = cls.distributeCandies(**test_case_1)
    print("------")
    print(ans)
