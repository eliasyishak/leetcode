# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        inverse_pairs = {value: key for key, value in pairs.items()}

        stack = []
        for char in s:
            # Opening character
            if char in pairs:
                stack.append(char)

            # Closing char
            else:
                if len(stack) == 0:
                    return False

                if stack[-1] == inverse_pairs[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    test_case_1 = "()[]{}"  # true
    test_case_2 = "([])"  # true
    test_case_3 = "[[[]"  # false
    test_case_4 = "(])"  # false

    cls = Solution()
    ans = cls.isValid(test_case_4)
    print("-----")
    print(ans)
