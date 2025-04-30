# https://leetcode.com/problems/find-numbers-with-even-number-of-digits
"""
Pretty straightforward problem, you could have also converted the integers
into strings and took the length. I think this is faster though..?
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        res = 0

        for val in nums:
            curr = int(val)
            count = 0
            while curr > 0:
                curr //= 10
                count += 1

            if count % 2 == 0:
                res += 1

        return res


if __name__ == "__main__":
    test_case_1 = [12, 345, 2, 6, 7896]  # 2

    cls = Solution()
    ans = cls.findNumbers(test_case_1)
    print("-----")
    print(ans)
