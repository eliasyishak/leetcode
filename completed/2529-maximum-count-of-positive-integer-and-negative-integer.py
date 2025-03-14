# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer
"""
Good practice for binary search but really easy to solve if you
are okay with a linear time solution.
"""


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        # Try to find the last negative number
        last_negative_index = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2

            # We found a negative value but there may be more
            # to the right
            if nums[mid] < 0:
                last_negative_index = mid
                left = mid + 1
            else:
                right = mid - 1

        # Try to find the first positive number
        first_positive_index = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # If we found a positive number, there may be more
            # to the left of this position, so search the left space
            if nums[mid] > 0:
                first_positive_index = mid
                right = mid - 1
            else:
                left = mid + 1

        pos = len(nums) - first_positive_index if first_positive_index != -1 else 0
        neg = last_negative_index + 1 if last_negative_index != -1 else 0

        return max(pos, neg)


if __name__ == "__main__":
    test_case_1 = [-2, -1, -1, 1, 2, 3]  # 3
    test_case_2 = [5, 20, 66, 1314]  # 4

    cls = Solution()
    ans = cls.maximumCount(test_case_2)
    print("------")
    print(ans)
