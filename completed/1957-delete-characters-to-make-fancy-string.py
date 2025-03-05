# https://leetcode.com/problems/delete-characters-to-make-fancy-string
"""
Labeled an easy problem but definitely at least a medium if you do it
"in place".  You can't really do it in place in python because you can't
change values by index in strings in python. However, if you imagine that
the input was a list of strings, you can then do all the operations in place.

This is a two pointer problem where the lagging pointer is what writes characters
that are valid. We can then chop off anything to the right that we removed.
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        # This is pointing to the pointer in the final
        # string that we can to return as i is free to iterate
        # through the whole thing
        #
        # j will only be incremented if the characters to its left
        # are all valid
        s_list = list(s)
        j = 2
        for i in range(2, len(s)):
            # The current index is valid
            if not (s[i] == s_list[j - 2] and s[i] == s_list[j - 1]):
                s_list[j] = s[i]
                j += 1

        return "".join(s_list[:j])


if __name__ == "__main__":
    test_case_1 = "leeetcode"  # leetcode
    test_case_2 = "aaabaaaa"  # aabaa

    cls = Solution()
    ans = cls.makeFancyString(test_case_2)
    print("-----")
    print(ans)
