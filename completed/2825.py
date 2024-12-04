# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments
"""
This one was a fun problem to think about. It can be easily solved if you think of having
two pointers, one for each string. The main important idea here is that we want the FULL
str2 to be found str1; even if that means you skip over some characters from str1 to find the
next match in str2
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        i = 0
        j = 0

        while i < len(str1) and j < len(str2):
            char1 = str1[i]
            char2 = str2[j]

            char_index_1 = ord(char1) - ord("a")
            char_index_2 = ord(char2) - ord("a")

            # If the current positions match up
            if char_index_1 == char_index_2:
                i += 1
                j += 1
            # If they match up after a transformation
            elif (char_index_1 + 1) % 26 == char_index_2:
                i += 1
                j += 1
            # Continue to search the first string
            else:
                i += 1

        return j == len(str2)


if __name__ == "__main__":
    test_case = {
        "str1": "abbbc",
        "str2": "ad",
    }  # True

    cls = Solution()
    ans = cls.canMakeSubsequence(
        str1=test_case["str1"],
        str2=test_case["str2"],
    )
    print("----")
    print(ans)
