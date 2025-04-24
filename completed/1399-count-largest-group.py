# https://leetcode.com/problems/count-largest-group
'''
Faily straightforward problem where we need to keep track of the calculated lengths. The
hardest part was using the while loop to get each digit to sum up.
'''
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        # The key is the sum of the digits and value is the number
        obj: dict[int, list[int]] = defaultdict(list)

        for val in range(1, n + 1):
            curr_sum = 0
            curr = int(val)

            while curr > 0:
                curr_sum += curr % 10
                curr //= 10

            obj[curr_sum].append(val)

        # Iterate through the object and count the sums that have the most values
        longest = 0
        res = 0
        for _, vals in obj.items():
            if len(vals) > longest:
                longest = len(vals)
                res = 1
            elif len(vals) == longest:
                res += 1

        return res


if __name__ == "__main__":
    test_case_1 = 13  # 4

    cls = Solution()
    ans = cls.countLargestGroup(test_case_1)
    print("------")
    print(ans)
