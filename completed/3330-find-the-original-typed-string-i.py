# https://leetcode.com/problems/find-the-original-typed-string-i
"""
Easy problem, the tricky part was in the wording, important to be clear
that the "mistake" is made at most ONE time. So with a word like
"abbcccc", you cannot have "abc" because that means the mistake
made twice, once for "b" and once for "c".

Feels like it is setting up for a backtracking problem as a followup?
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i, char in enumerate(word):
            if i > 0 and word[i - 1] == char:
                res += 1

        return res
