# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i
"""
A pretty intuitive sliding window problem when you come to understand that you have
an upperbound on the length of the substring given that it must appear 3 times. The maximum
substring length == length of input string - 2.

The examples below illustrate that pretty well when you draw it out.
-------
aaaa (4 --> 2)

aa aa
a aa a
aa aa
-------
aaaa (4 --> 2)

aa aa
a aa a
aa aa
-------
aaaaa (5 --> 3)

aaa aa
a aaa a
aa aaa
-------
aaaaaa (6 --> 4)

aaaa aa
a aaaa a
aa aaaa
-------
aaaaaaa (7 --> 5)

aaaaa aa
a aaaaa a
aa aaaaa
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        # The longest possible substring we can make for a given string of a
        # given length will be len(s) - 2
        max_possible_len = len(s) - 2

        results = {}
        left = 0
        right = 0
        while left < len(s) and right < len(s):
            substring = s[left : right + 1]
            if substring not in results:
                results[substring] = 0
            results[substring] += 1

            # If we can expand the current window
            if (
                right + 1 < len(s)
                and s[right] == s[right + 1]
                and (right - left + 1 + 1) <= max_possible_len
            ):
                right += 1
            else:
                left += 1
                right = left

        ans = -1
        for substring, occurences in results.items():
            if occurences >= 3:
                ans = max(len(substring), ans)

        return ans


if __name__ == "__main__":
    test_case_1 = "aaaa"  # 2
    test_case_2 = "abcdef"  # -1, not possible
    test_case_3 = "abcaba"  # 1
    test_case_4 = "abcccccdddd"  # 3

    test_case = test_case_4
    cls = Solution()
    ans = cls.maximumLength(s=test_case)
    print("----")
    print(ans)


