# https://leetcode.com/problems/largest-divisible-subset
"""
Good problem to understand backtracking, in this example, instead
of branching at each index i and recursing, we could loop through
each index after i to simulate the skipping.
"""


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        cache: dict[int, int] = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]

            res = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            cache[i] = res
            return res

        # By iterating at each index, we don't need to have a branching
        # structure at each index i, skipping would mean starting at a later
        # point in the iteration
        res: list[int] = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res


if __name__ == "__main__":
    test_case_1 = [1, 2, 5, 15, 45]  # [5, 15, 45]

    cls = Solution()
    ans = cls.largestDivisibleSubset(test_case_1)
    print("------")
    print(ans)
