# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit
"""
Relatively straightforward problem, need to prioritize replacing
the most significant digit with a 9 to maximize `num` and to minimize
you just turn the first digit into a 0
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        to_maximize = ""
        for char in num_str:
            if char != "9":
                to_maximize = char
                break

        to_minimize = num_str[0]

        maximized = ["9" if digit == to_maximize else digit for digit in num_str]
        minimized = ["0" if digit == to_minimize else digit for digit in num_str]

        return int("".join(maximized)) - int("".join(minimized))


if __name__ == "__main__":
    test_case_1 = 11891  # 99009
    test_case_2 = 90  # 99

    cls = Solution()
    ans = cls.minMaxDifference(test_case_2)
    print("------")
    print(ans)
