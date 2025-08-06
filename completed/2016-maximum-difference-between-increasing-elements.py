# https://leetcode.com/problems/maximum-difference-between-increasing-elements
"""
Relatively easy problem. Can be solved with an easy O(n^2) approach but also
with a prefix sum so that we only need to iterate through the list once.

This is similar to the stock selling problem.
"""


class Solution:
    def maximumDifferenceSlow(self, nums: list[int]) -> int:
        n = len(nums)

        res = -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])

        return res

    def maximumDifference(self, nums: list[int]) -> int:
        n = len(nums)

        res = -1
        prefix_min = nums[0]

        for j in range(1, n):
            prefix_min = min(prefix_min, nums[j])

            if nums[j] > prefix_min:
                res = max(res, nums[j] - prefix_min)

        return res


if __name__ == "__main__":
    test_case_1 = [7, 1, 5, 4]  # 4
    test_case_2 = [9, 4, 3, 2]  # -1

    cls = Solution()
    ans = cls.maximumDifference(test_case_2)
    print("------")
    print(ans)
