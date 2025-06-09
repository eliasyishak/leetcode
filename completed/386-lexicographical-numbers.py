# https://leetcode.com/problems/lexicographical-numbers
"""
This problem becomes an easier problem when you use n as the
upperbound and just attempt to create all possible values.

For example, start with 1, 10, 100 until you hit a number
that is great than n (n = 110)

Then you go 101, 102, 103 from where we left off at 100
"""


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res: list[int] = []

        def dfs(val: int) -> None:
            if val > n:
                return

            res.append(val)
            val *= 10
            for next_digit in range(10):
                dfs(val=val + next_digit)

        for first_digit in range(1, 10):
            dfs(val=first_digit)

        return res


if __name__ == "__main__":
    test_case_1 = 13  # [1,10,11,12,13,2,3,4,5,6,7,8,9]

    cls = Solution()
    ans = cls.lexicalOrder(test_case_1)
    print("------")
    print(ans)
