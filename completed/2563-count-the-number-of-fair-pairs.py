# https://leetcode.com/problems/count-the-number-of-fair-pairs
"""
Slightly more challenging version of 2824-count-pairs-whose-sum-is-less-than-target.py

The main takeaway here is that if you are handling a range of values for
the target, you can take the difference of all the pairs that fit under
the upperbound - the lowerbound pairs

We need to use two different methods for calculating the lower and upperbound
pairs because the upper bound pair can sum up to the target

WHILE

the lowerbound pairs cannot sum up the lowerbound. Pairs that would have summed
up to the lowerbound target would have already been accounted for when doing the
upperbound calculation
"""

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        print({"nums": nums, "lower": lower, "upper": upper})

        # Having a hard time understanding why we add one
        upper_bound_pair_count = self.calc_upper_bound_pairs(nums=nums, target=upper)
        lower_bound_pair_count = self.calc_lower_bound_pairs(nums=nums, target=lower)

        return upper_bound_pair_count - lower_bound_pair_count

    def calc_upper_bound_pairs(self, nums, target):
        print("UPPER")
        pairs = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum <= target:
                print(left, right)
                pairs += right - left
                left += 1
            else:
                right -= 1

        return pairs

    def calc_lower_bound_pairs(self, nums, target):
        print("LOWER")
        pairs = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum < target:
                print(left, right)
                pairs += right - left
                left += 1
            else:
                right -= 1

        return pairs


if __name__ == "__main__":
    test_case_1 = {
        "nums": [0, 1, 7, 4, 4, 5],
        "lower": 3,
        "upper": 6,
    }  # 6

    test_case_2 = {
        "nums": [1, 7, 9, 2, 5],
        "lower": 11,
        "upper": 11,
    }  # 1

    cls = Solution()
    ans = cls.countFairPairs(**test_case_2)
    print("----")
    print(ans)
