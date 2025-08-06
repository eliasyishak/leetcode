# https://leetcode.com/problems/rearranging-fruits
"""
Good long problem, it helps to actually do the exercise on paper.
Great video tutorial though: https://www.youtube.com/watch?v=7tyRitV6sO8&ab_channel=Techdose
"""

from collections import defaultdict


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        # Create a frequency object to count each unique
        # number from both lists, basket1 will increment the count
        # and basket2 will decrement
        freq: dict[int, int] = defaultdict(int)
        for val in basket1:
            freq[val] += 1
        for val in basket2:
            freq[val] -= 1

        # If any of the value frequencies are odd, then there
        # is no possible solution
        for _, count in freq.items():
            if count % 2:
                return -1

        # Create a list of numbers that will be transfered, anything
        # that doesn't have a 0 frequency will be transfered
        transfers: list[int] = []
        for val, count in freq.items():
            if count != 0:
                transfers += [val] * (abs(count) // 2)

        # We only need the first half of the sorted transfers list since
        # the cost of a transfer is the minimum between the swapped values
        transfers.sort()
        res = 0
        min_value = min(freq)
        for transfer_val in transfers[0 : (len(transfers)) // 2]:
            # We look at the first half value of the transfer values after
            # being sorted -- then we take the minimum of that value or 2 times
            # the minimum value
            #
            # We do this because using the smallest value may cost less than the actual
            # value we intend to transfer. We have 2x the cost because it moves once
            # and needs to return to its original basket
            res += min(transfer_val, 2 * min_value)

        return res


if __name__ == "__main__":
    test_case_1 = {
        "basket1": [4, 2, 2, 2],
        "basket2": [1, 4, 1, 2],
    }  # 1

    test_case_2 = {
        "basket1": [2, 3, 4, 1],
        "basket2": [3, 2, 5, 1],
    }  # -1

    test_case_3 = {
        "basket1": [84, 80, 43, 8, 80, 88, 43, 14, 100, 88],
        "basket2": [32, 32, 42, 68, 68, 100, 42, 84, 14, 8],
    }  # 48

    cls = Solution()
    ans = cls.minCost(**test_case_3)
    print("------")
    print(ans)
