# https://leetcode.com/problems/maximum-score-after-splitting-a-string
"""
Easy problem using the suffix sum concept by iterating once over the array
keeping a running count of ones encountered.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for char in s:
            if char == "1":
                ones += 1

        res = 0
        zeros = 0
        # Make sure to stop one short of the end of the character since index=0
        # means that the first character is in the left substring
        for i in range(len(s) - 1):
            char = s[i]
            if char == "0":
                zeros += 1
            else:
                ones -= 1

            res = max(res, zeros + ones)

        return res


if __name__ == "__main__":
    test_case_1 = "011101"  # 5
    test_case_2 = "00"  # 1

    cls = Solution()
    ans = cls.maxScore(test_case_2)
    print("-----")
    print(ans)
