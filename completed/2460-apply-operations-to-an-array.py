# https://leetcode.com/problems/apply-operations-to-an-array
"""
Straightforward problem, first of the month for March 2025 so easily
to follow along in the code.
"""


class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            if i + 1 == n:
                continue

            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        res = [0] * n
        i = 0
        for j in range(n):
            if nums[j] > 0:
                res[i] = nums[j]
                i += 1

        return res


if __name__ == "__main__":
    test_case_1 = [1, 2, 2, 1, 1, 0]  # [1,4,2,0,0,0]

    cls = Solution()
    ans = cls.applyOperations(test_case_1)
    print("------")
    print(ans)
