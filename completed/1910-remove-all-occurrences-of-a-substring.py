"""
Use a stack to keep track of the characters we have found so far
and use a while loop to always make sure the last n items in the stack
is not equal to the part string (part_list)
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_list = [char for char in part]
        n = len(part_list)

        stack: list[str] = []
        for char in s:
            stack.append(char)

            if len(stack) >= len(part_list):
                while stack[-n:] == part_list:
                    for _ in range(n):
                        stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    test_case_1 = {
        "s": "daa" "bcb" "aab" "cbc",
        "part": "abc",
    }  # dab

    test_case_2 = {
        "s": "axx" "xxy" "yyyb",
        "part": "xy",
    }  # ab

    cls = Solution()
    ans = cls.removeOccurrences(**test_case_1)
    print("-----")
    print(ans)
