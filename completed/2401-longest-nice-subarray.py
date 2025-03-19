# https://leetcode.com/problems/longest-nice-subarray
"""
Interesting sliding window problem that uses bitwise operations to
increase and decrease the window size.

To solve this problem, we use the AND operator to check that the
current substring ending at the right index is valid

If it is not valid, we unset the bits from the left end using the XOR
operator until the while condition is satisifed.

Once we have a valid substring, we use the OR operator to set the bits
from the right side of the window.

Then we check for how long this valid substring is by using the right and left
bounds to calculate the length.
"""


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        left = curr = 0
        for right in range(n):
            # Condition for shrinking the window from the left
            while curr & nums[right]:
                # The XOR operation will remove the left
                # most bits from current
                curr = curr ^ nums[left]
                left += 1

            # Taking the OR operation with nums right adds the
            # current right value into curr
            curr = curr | nums[right]
            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    test_case_1 = [1, 3, 8, 48, 10]  # 3 -> [3, 8, 48]
    test_case_2 = [3, 1, 5, 11, 13]  # 1

    cls = Solution()
    ans = cls.longestNiceSubarray(test_case_2)
    print("------")
    print(ans)
