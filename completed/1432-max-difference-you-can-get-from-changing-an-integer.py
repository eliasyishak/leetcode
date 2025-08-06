# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer
"""
Not too bad of a problem, take the greedy approach to the problem. To maximize for
a, we ned to find the first number going from left to right that is not a 9 and replace
it to be a 9.

To minimize for b, we need to find the first character going from left to right that is
not a 1 or 0. If that character exists at index 0, then we must replace it with a 1
since we cannot have any leading zeros, otherwise, we will swap it with a zero.
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        def get_a() -> int:
            to_replace = ""
            for char in num_str:
                if char != "9":
                    to_replace = char
                    break

            if to_replace == "":
                return num

            return int(num_str.replace(to_replace, "9"))

        def get_b() -> int:
            to_replace = ""
            i = 0  # just to make linting happy
            for i, char in enumerate(num_str):
                if char != "1" and char != "0":
                    to_replace = char
                    break

            if to_replace == "":
                return num

            if i == 0:
                return int(num_str.replace(to_replace, "1"))

            return int(num_str.replace(to_replace, "0"))

        a = get_a()
        b = get_b()

        return a - b


if __name__ == "__main__":
    test_case_1 = 123456  # 820_000
    test_case_2 = 555  # 888
    test_case_3 = 9  # 8
    test_case_4 = 9288  # 8700
    test_case_5 = 1_101_057  # 8_808_050
    test_case_6 = 10_000  # 80_000

    cls = Solution()
    ans = cls.maxDiff(test_case_6)
    print("-----")
    print(f"{ans:_}")
