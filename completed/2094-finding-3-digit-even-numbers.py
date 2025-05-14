# https://leetcode.com/problems/finding-3-digit-even-numbers
"""
Spent some time trying to do this with backtracking, but its tough to
do because the answers can be in any order on the response so it's tough
to enumerate across all of the possible combinations.

The brute force works so fuck it :)
"""


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n = len(digits)
        res: set[int] = set()

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue

                    curr = f"{digits[i]}{digits[j]}{digits[k]}"
                    if digits[i] == 0:
                        continue

                    curr_int = int(curr)
                    if curr_int % 2 == 1:
                        continue

                    res.add(curr_int)

        return sorted(list(res))


if __name__ == "__main__":
    test_case_1 = [2, 1, 3, 0]  # [102,120,130,132,210,230,302,310,312,320]

    cls = Solution()
    ans = cls.findEvenNumbers(test_case_1)
    print("-------")
    print(ans)
