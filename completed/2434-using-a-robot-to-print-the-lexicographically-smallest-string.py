# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string
"""
Good problem for understanding stack management. The key to this problem
is to have a preprocessed frequency dictionary that allows you to "check"
if the current character you are on is the smallest available.

We do this by checking to the right of the current character by looking for
the minimum character leftover in the frequency dictionary.

For my approach to work well, you have to delete the character key out of the
lookup dictionary once we have 0 occurences left.
"""

from collections import defaultdict


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # This ensures that the string is at least
        # 2 characters long which allows us to sort
        if n < 2:
            return s

        # Frequency count
        counts: dict[str, int] = defaultdict(int)
        for char in s:
            counts[char] += 1

        res = ""
        stack: list[str] = []  # this refers to "t" in the problem statement
        for char in s:
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]

            stack.append(char)

            # Condition for adding to the response
            #
            # We do this once we know that there is nothing left
            # in the string that is smaller than what we have on top
            # of the stack
            while counts and stack and min(counts) >= stack[-1]:
                res += stack.pop()

        # Empty out the left over stack
        while stack:
            res += stack.pop()

        return res


if __name__ == "__main__":
    test_case_1 = "bac"  # abc
    test_case_2 = "bydizfve"  # bdevfziy

    cls = Solution()
    ans = cls.robotWithString(test_case_2)
    print("-----")
    print(ans)
