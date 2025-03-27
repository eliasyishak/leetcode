# https://leetcode.com/problems/minimum-index-of-a-valid-split
"""
Good problem for understanding how to count the most frequent item
in an array. Learned how to use a voting algorithm here to find the most
common element.  This only works though because the problem gauarantees that
there will be only ONE dominant element.

Using this voting algorithm makes it more memory efficient since we don't
need keep track of every single element in the list and then finding a max.
"""


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        # Voting algorithm to determine which is the most common
        # number in the nums list
        #
        # We can do this approach because the problem guarantees there
        # is a dominate number in the original array
        count = 0
        most_common = 0  # Initialize to zero but it doesn't matter what we set
        for val in nums:
            if count == 0:
                count = 1
                most_common = val
            elif val == most_common:
                count += 1
            else:
                count -= 1

        # Count how many occurences we have of the most common value
        total_count = 0
        for val in nums:
            if val == most_common:
                total_count += 1

        # Iterate through each index in the array and check for an index that is valid
        left_count = 0
        right_count = total_count
        n = len(nums)
        for i, val in enumerate(nums):
            if val == most_common:
                left_count += 1
                right_count -= 1

                left_length = i + 1
                right_length = n - left_length

                if left_count > left_length / 2 and right_count > right_length / 2:
                    return i

        return -1


if __name__ == "__main__":
    test_case_1 = [1, 2, 2, 2]  # 2
    test_case_2 = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]  # 4
    test_case_3 = [1, 1, 1, 2]  # 0

    cls = Solution()
    ans = cls.minimumIndex(test_case_3)
    print("------")
    print(ans)
