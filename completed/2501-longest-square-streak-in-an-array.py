# https://leetcode.com/problems/longest-square-streak-in-an-array
"""
I made this problem more difficult than it needed to be initially by thinking
that I should not be sorting the list. Ultimately I just sorted the list initially
which makes time complexity jump to O(N*log(n)) but the solution becomes so much simpler
when you do that since you only have to iterate through the list once.

Looking at the editorial, looks all recommended solutions are also sorting.
"""


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        num_set = set(nums)

        res = -1
        for i in range(n):
            val = nums[i]
            curr = 1
            while val**2 in num_set:
                curr += 1
                res = max(res, curr)

                val **= 2

        return res


if __name__ == "__main__":
    test_case_1 = [4, 3, 6, 16, 8, 2]  # 3
    test_case_2 = [2, 3, 5, 6, 7]  # -1

    cls = Solution()
    ans = cls.longestSquareStreak(test_case_2)
    print("------")
    print(ans)
