# https://leetcode.com/problems/clear-digits
"""
Simple stack problem where we need to keep track of the most
recent character we saw as we iterate through the list from
left to right.
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    test_case_1 = "cb34"

    cls = Solution()
    ans = cls.clearDigits(test_case_1)
    print("----")
    print(ans)
