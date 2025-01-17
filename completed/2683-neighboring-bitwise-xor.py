# https://leetcode.com/problems/neighboring-bitwise-xor
"""
Two ways to approach this problem, the first approach is what I naturally
came to, where we need to assume a value for the first item in the array.

The second approach a trick we can implement to finish the algorithm faster.
"""

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        [1, 1, 0]

        derived[0] = original[0] ^ original[1]  --> original[1] = derived[0] ^ original[0]
        derived[1] = original[1] ^ original[2]  --> original[2] = derived[1] ^ original[1]
        derived[2] = original[2] ^ original[0]  --> original[0] = derived[2] ^ original[2]

        To be able to complete this algorithm, we start from derived[0], at this point, we have
        following variables in our equation
            - derived[0]  (known)
            - original[0] (unknown)
            - original[1] (unkown)

        We have 3 variables and 2 unknowns, however, every item in the array is binary so we
        only have 2 options. If we begin by setting original[0] = 1, we can complete all of the
        equations

        derived[0] = original[0] ^ original[1]  --> original[1] = derived[0] ^ original[0]
                                                    original[1] =     1      ^    0
                                                    original[1] =     1

        We complete the algorithm with the assumption of setting original[0] = 0 and see if
        we can produce a valid result
        """

        valid_found = False
        n = len(derived)
        for i in range(2):
            original = [i]

            for j in range(1, n):
                original.append(derived[j - 1] ^ original[j - 1])

        # We have a valid original array if we can correctly produce the
        # last elemenet in the derived array with the assumption we made
        # for original[0]
        if derived[-1] == original[-1] ^ original[0]:
            valid_found = True

        return valid_found

    def doesValidArrayExistFaster(self, derived: List[int]) -> bool:
        """
        Observe the following equations that represent the relationship
        between the elements of the derived and original arrays:

        derived[0] = original[0] XOR original[1]
        derived[1] = original[1] XOR original[2]
        derived[2] = original[2] XOR original[3]
        derived[3] = original[3] XOR original[4]
        ...
        derived[n-1] = original[n-1] XOR original[0]


        Each element in original appears exactly twice in the
        equations: once as original[i] and once as original[i+1].

        For example:

        original[0] appears in derived[0] (original[0] XOR original[1])
        original[0] also appears in derived[n-1] (original[n-1] XOR original[0])
        Since XOR is both commutative and associative, the order doesn’t
        matter. When all occurrences of original[i] are XORed together,
        they cancel each other out:

        original[0] XOR original[0] XOR original[1] XOR original[1] ... = 0

        If the derived array is valid (i.e., it was generated from some original),
        then the XOR of all elements in derived must be 0. This is because all elements
        of original cancel out when XORed.
        """

        XOR = 0
        for element in derived:
            XOR = XOR ^ element
        return XOR == 0


if __name__ == "__main__":
    test_case_1 = [1, 1, 0]  # true
    test_case_2 = [1, 1]  # true
    test_case_3 = [1, 0]  # false

    cls = Solution()
    ans = cls.doesValidArrayExist(test_case_3)
    print("-----")
    print(ans)
