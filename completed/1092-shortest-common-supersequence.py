# https://leetcode.com/problems/shortest-common-supersequence
"""
This is definitely a hard problem that that has some limitations that can have us
run into time and space limit exceptions when running in leetcode.  There are further
optimizations that we can make to have it run within the the constraints but this solution
is what I arrived at on my own so sticking with this :)

The idea here is that we need to make a decision as we iterate through each character
in both strings about including the character from str1 or str2 (if they are different).
So essentially, this becomes something like a backtracking problem but we don't undo our decision,
instead, we need to continue exploring all possible options as we iterate through both
strings.

str1 = "abc" str2 = "xyz"  (not a great example but good for illustration)

We need to check both: res = "a" + rest AND res = "x" + rest
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        cache: dict[tuple[int, int], str] = {}

        def solver(i: int, j: int) -> str:
            if (i, j) in cache:
                return cache[(i, j)]

            # If both indexes are out of bounds we can return an empty string
            if i == n1 and j == n2:
                cache[(i, j)] = ""
                return ""

            # If only one index is out of bounds, return the other one
            if i >= n1:
                res = str2[j] + solver(i=i, j=j + 1)
                cache[(i, j)] = res
                return res
            if j >= n2:
                res = str1[i] + solver(i=i + 1, j=j)
                cache[(i, j)] = res
                return res

            if str1[i] == str2[j]:
                res = str1[i] + solver(i=i + 1, j=j + 1)
                cache[(i, j)] = res
                return res
            else:
                # Try both paths from str1 and str2
                option_one = str1[i] + solver(i=i + 1, j=j)
                option_two = str2[j] + solver(i=i, j=j + 1)

                res = option_one if len(option_one) < len(option_two) else option_two
                cache[(i, j)] = res

                return res

        return solver(i=0, j=0)


if __name__ == "__main__":
    test_case_1 = {
        "str1": "cab",
        "str2": "abac",
    }  # cabac

    test_case_2 = {
        "str1": "aaaaaaaa",
        "str2": "aaaaaaaa",
    }  # aaaaaaaa

    test_case_3 = {
        "str1": "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb",
        "str2": "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa",
    }  # dddbbdcbccaaaccbababaacbdcbacddadcdacbdddcadccacddbadcadcbabdaccbccdcdcbaaabcaccacbbdcbaabb

    cls = Solution()
    ans = cls.shortestCommonSupersequence(**test_case_3)
    print("-----")
    print(ans)
