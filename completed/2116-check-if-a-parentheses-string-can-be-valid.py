# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid
"""
Tough problem for me to understand, could probably benefit from additional review
on this problem.
"""


class Solution:
    def canBeValid(self, s, locked):
        n = len(s)

        # If length of string is odd, return false.
        if n % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(n):
            if locked[i] == "0":
                unlocked.append(i)

            elif s[i] == "(":
                open_brackets.append(i)

            elif s[i] == ")":
                # We must check for the open brackets first and then fall back
                # to use the unlocked characters
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        #
        # We need to ensure that the matching unlocked character is after the locked
        # open bracket to ensure we can close it
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        # If we have any more open brackets that are locked, then we don't have a valid string
        if open_brackets:
            return False

        return True


if __name__ == "__main__":
    test_case_1 = {
        "s": "))()))",
        "locked": "010100",
    }  # true

    test_case_2 = {
        "s": "((()(()()))()((()()))))()((()(()",
        "locked": "10111100100101001110100010001001",
    }  # true

    cls = Solution()
    ans = cls.canBeValid(**test_case_1)
    print("-----")
    print(ans)
