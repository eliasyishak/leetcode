# https://leetcode.com/problems/rabbits-in-forest
"""
This was more of a logic puzzle than a coding problem. Following the logic below shows
how we can come up with the solution. The important step is to iterate through the left
over counter object and ensure that we increment the answer by the answer value + 1
"""

from collections import defaultdict


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        freq: dict[int, int] = defaultdict(int)
        res = 0

        for val in answers:
            # If we ever have 0 as the answer, that means there were no other
            # rabbits that matched so there is only one of that specific rabbit
            if val == 0:
                res += 1
            else:
                freq[val] += 1
                # We have completed the group if this condition is satisified
                if freq[val] == val + 1:
                    res += val + 1
                    del freq[val]

        # Go through the left over frequency counts and if there are any
        # leftover, we will use their counts to increment the res
        for group, _ in freq.items():
            res += group + 1

        return res


if __name__ == "__main__":
    test_case_1 = [1, 1, 2]  # 5
    test_case_2 = [10, 10, 10]  # 11

    cls = Solution()
    ans = cls.numRabbits(test_case_2)
    print("------")
    print(ans)
