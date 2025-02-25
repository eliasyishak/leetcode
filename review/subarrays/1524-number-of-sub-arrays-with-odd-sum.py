# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum
"""
Tough one to understand but the basic understanding is that the difference
between two prefix sums in an array will give you the number of odd
subarrays between the two.

Also very important to understand that you are looking for the number of
subarrays ENDING at the current value in the for loop.

So for [1, 3, 5]
@ i = 0; we have 1 odd subarray, 0 even subarray
@ i = 1; we have 2 odd subarray, 1 even subarray
@ i = 2; current sum is 9, which means to get more odds, we need subarrays
    that are even which is 1... and we have already encountered 2 odd subarrays
    before BUT we need the even subarrays to determine how many subarrays end at
    i=2
"""


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        curr_sum = odds = evens = res = 0
        for val in arr:
            curr_sum += val

            if curr_sum % 2 == 1:
                res += 1 + evens
                odds += 1
            else:
                evens += 1
                res += odds

        return res


if __name__ == "__main__":
    test_case_1 = [1, 3, 5]  # 4
    test_case_2 = [2, 4, 6]  # 0
    test_case_3 = [1, 2, 3, 4, 5, 6, 7]  # 16

    cls = Solution()
    ans = cls.numOfSubarrays(test_case_1)
    print("-----")
    print(ans)
