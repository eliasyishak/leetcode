# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i
"""
The trick to this problem is to understand that you can approach this
in a greedy way. Consider the first element in the array, if it is a
0, then you have no choice but to flip the first 3 elements. Then you
continue to do this as you iterate through the whole list

You have a valid array if at the end, the last two elements in the array
are also 1
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        # Iterate through every item except the last two elements in the list
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0

                res += 1

        return res if sum(nums[-2:]) == 2 else -1


if __name__ == "__main__":
    test_case_1 = [0, 1, 1, 1, 0, 0]  # 3

    cls = Solution()
    ans = cls.minOperations(test_case_1)
    print("-------")
    print(ans)
