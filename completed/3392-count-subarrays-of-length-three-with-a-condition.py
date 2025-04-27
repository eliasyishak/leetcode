# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition
"""
Easy one today, subarray being continuous makes it easy
"""


class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n - 1):
            if nums[i - 1] + nums[i + 1] == nums[i] / 2:
                res += 1

        return res


if __name__ == "__main__":
    test_case_1 = [1, 2, 1, 4, 1]  # 1
    test_case_2 = [1, 1, 1]  # 0

    cls = Solution()
    ans = cls.countSubarrays(test_case_1)
    print("------")
    print(ans)
