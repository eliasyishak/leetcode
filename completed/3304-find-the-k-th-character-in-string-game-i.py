# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
"""
This is defined an easy problem because we can simulate the answer
since the constraints for k are pretty small, but there is an approach
you can use that takes advantage of the fact that the string doubles in
size every time. We'll cross that bridge if that becomes the next problem :)
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        def get_next_char(char: str) -> str:
            pos = ord(char) - ord("a")

            pos += 1
            pos %= 26

            return chr(ord("a") + pos)

        curr = "a"

        while len(curr) < k:
            new = ""
            for char in curr:
                new += get_next_char(char)

            curr += new

        return curr[k - 1]


if __name__ == "__main__":
    test_case_1 = 5  # b
    test_case_2 = 10  # b

    cls = Solution()
    ans = cls.kthCharacter(test_case_2)
    print("-----")
    print(ans)
