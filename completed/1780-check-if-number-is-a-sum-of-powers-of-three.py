# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three
"""
If you take the backtracking approach, it is a pretty simple problem to solve.

There is a better way to solve this using math that involves ternary operations
(binary but for 3 states in bits 0, 1, or 2).
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(curr_sum: int, power: int, vals: list[int]) -> bool:
            curr_val = 3**power

            if curr_sum + curr_val == n:
                print([*vals, curr_val])
                return True

            if curr_sum + curr_val > n:
                return False

            return backtrack(
                curr_sum=curr_sum + curr_val, power=power + 1, vals=[*vals, curr_val]
            ) or backtrack(curr_sum=curr_sum, power=power + 1, vals=vals)

        res = backtrack(curr_sum=0, power=0, vals=[])
        return res


if __name__ == "__main__":
    test_case_1 = 12  # True
    test_case_2 = 91  # True
    test_case_3 = 21  # False

    cls = Solution()
    ans = cls.checkPowersOfThree(test_case_3)
    print("------")
    print(ans)
