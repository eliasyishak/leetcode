# https://leetcode.com/problems/rotate-string
"""
My first solution simply found all of the starting points that
could be possible and would iterate from those starting indexes
and checking the initial string. This is a O(n^2) time complexity though.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)

        # Find all the possible starting points in the goal string based
        # on the first string in s
        start_indexes = [i for i, char in enumerate(goal) if char == s[0]]

        for start in start_indexes:
            # Points to the index in s
            i = 0
            while i < n and s[i] == goal[start]:
                i += 1
                start = (start + 1) % n

            if i == n:
                return True

        return False


if __name__ == "__main__":
    test_case_1 = {
        "s": "abcde",
        "goal": "cdeab",
    }  # true

    cls = Solution()
    ans = cls.rotateString(**test_case_1)
    print("-----")
    print(ans)
