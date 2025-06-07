# https://leetcode.com/problems/lexicographically-smallest-equivalent-string
"""
Good problem for understanding how the union find works.

Possibly should review this some more to understand the union find
algorithm. The first approach shows that it works with the first 2 test
cases but it fails on the third one due to the transitive property
"""


class Solution:
    def smallestEquivalentStringWrong(self, s1: str, s2: str, baseStr: str) -> str:
        ABC = "abcdefghijklmnopqrstuvwxyz"

        # First create the sets based on the s1 and s2

        # Each set will be numbered 0,n and each set number will
        # have a minimum tracked in the dictionary
        set_minimums: dict[int, int] = {}

        # This list below indicates if we have already covered that character
        #
        # 26 length, 1 position for each character; -1 means it has not been assigned
        chars_assigned = [-1] * 26
        curr_set = 0
        for char1, char2 in zip(s1, s2):
            pos1 = ord(char1) - ord("a")
            pos2 = ord(char2) - ord("a")

            # Skip the character if they are the same
            if pos1 == pos2:
                continue

            # The case when neither character has been recorded yet
            if chars_assigned[pos1] == -1 and chars_assigned[pos2] == -1:
                chars_assigned[pos1] = curr_set
                chars_assigned[pos2] = curr_set
                set_minimums[curr_set] = min(pos1, pos2)
                curr_set += 1
            else:
                if chars_assigned[pos1] == -1:
                    chars_assigned[pos1] = chars_assigned[pos2]
                    looked_up_set = chars_assigned[pos2]
                    set_minimums[looked_up_set] = min(pos1, set_minimums[looked_up_set])

                if chars_assigned[pos2] == -1:
                    chars_assigned[pos2] = chars_assigned[pos1]
                    looked_up_set = chars_assigned[pos1]
                    set_minimums[looked_up_set] = min(pos2, set_minimums[looked_up_set])

        res = list(baseStr)
        for index, char in enumerate(baseStr):
            pos = ord(char) - ord("a")

            assigned_set = chars_assigned[pos]

            smallest_pos = set_minimums.get(assigned_set)
            if smallest_pos is not None:
                res[index] = ABC[smallest_pos]

        return "".join(res)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent: list[int] = [-1] * 26  # parent[i] = -1 initially

        def find(x: int) -> int:
            if parent[x] == -1:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            # Always attach the larger to the smaller (lex smallest)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord("a"), ord(b) - ord("a"))

        res: list[str] = []
        for c in baseStr:
            smallest = find(ord(c) - ord("a"))
            res.append(chr(smallest + ord("a")))
        return "".join(res)


if __name__ == "__main__":
    test_case_1 = {
        "s1": "parker",
        "s2": "morris",
        "baseStr": "parser",
    }  # makkek

    test_case_2 = {
        "s1": "leetcode",
        "s2": "programs",
        "baseStr": "sourcecode",
    }  # makkek

    test_case_3 = {
        "s1": "aba",
        "s2": "abb",
        "baseStr": "buq",
    }  # auq

    cls = Solution()
    ans = cls.smallestEquivalentStringWrong(**test_case_3)
    print("-----")
    print(ans)
