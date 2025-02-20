# https://leetcode.com/problems/find-unique-binary-string
"""
THis was labeled as a backtracking problem but you could also solve
this as a dfs problem and early exit out of the call stack when you
have found an answer.

For fun, there is a math proof that involes the below solution. Very
clever to create the answer by simply checking each position i in the
ith item in the list. You travel down the diagonal and take a value that is
different at each position.

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)
"""

from typing import List


class Solution:
    def __init__(self):
        self.ans = ""

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)

        def dfs(curr: str):
            if len(self.ans) > 0:
                return

            if len(curr) == n:
                if curr not in nums_set:
                    self.ans = str(curr)
                return

            dfs(curr + "0")
            dfs(curr + "1")

        dfs("")
        return self.ans


if __name__ == "__main__":
    test_case_1 = ["01", "10"]  # "11" or "00"
    test_case_2 = ["00", "01"]  # "11" or "10"
    test_case_3 = ["111", "011", "001"]  # "101", "000", "010", "100", and "110"

    cls = Solution()
    ans = cls.findDifferentBinaryString(test_case_3)
    print("------")
    print(ans)
