# https://leetcode.com/problems/bitwise-xor-of-all-pairings
"""
This was kind of a tricky question, you have to be able to understand
bitwise operations and how the XOR operation is similar to multipication

Assume I have this input
nums1 = [a, b, c]
nums2 = [x, y]

Pairing everything and taking the XOR looks as follows
[a^x, a^y,  b^x, b^y,  c^x, c^y]

Once you have the above, you then take the XOR of each of the elements
in that new list

(a^x) ^ (a^y) ^ (b^x) ^ (b^y) ^ (c^x) ^ (c^y)

And like multipication, we can move around our numbers we are XOR'ing

(a ^ b ^ c) ^ (a ^ b ^ c)   ^   (x ^ y) ^ (x ^ y) ^ (x ^ y)

So if you have xor1 = (a ^ b ^ c) and xor2 = (x ^ y) you can use the below
XOR properties along with the length of nums1 and nums2 to get the answer

SAME VALUE ALWAYS RETURNS 0
1 ^ 1 = 0

ANYTHING XOR'ed WITH A 0 IS THAT VALUE (equivalent to multipling by 1)
1 ^ 0 = 1
12 ^ 0 = 12
x ^ 0 = x
"""

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        if n % 2 == 0 and m % 2 == 0:
            return 0

        xor1 = 0
        for val1 in nums1:
            xor1 ^= val1

        xor2 = 0
        for val2 in nums2:
            xor2 ^= val2

        # If one of the inputs list is a zero, then
        # the other xor value is going to be 0
        if n % 2 == 1 and m % 2 == 1:
            return xor1 ^ xor2
        elif n % 2 == 1:
            return xor2
        else:
            return xor1


if __name__ == "__main__":
    test_case_1 = {
        "nums1": [2, 1, 3],
        "nums2": [10, 2, 5, 0],
    }  # 13

    cls = Solution()
    ans = cls.xorAllNums(**test_case_1)
    print("-----")
    print(ans)
