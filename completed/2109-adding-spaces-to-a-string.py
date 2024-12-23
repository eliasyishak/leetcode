# https://leetcode.com/problems/adding-spaces-to-a-string
"""
Multipointer type of problem where we are traversing a string and
handling edge cases well
"""

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = [" "] * (len(s) + len(spaces))

        space_index = 0
        write_index = 0
        for i, char in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                write_index += 1
                space_index += 1
            result[write_index] = char
            write_index += 1

        return "".join(result)


if __name__ == "__main__":
    test_case = {"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]}

    cls = Solution()
    ans = cls.addSpaces(s=test_case["s"], spaces=test_case["spaces"])

    print("--")
    print(ans)
