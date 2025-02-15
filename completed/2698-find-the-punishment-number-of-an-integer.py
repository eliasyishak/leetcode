# https://leetcode.com/problems/find-the-punishment-number-of-an-integer
"""
This problem was a tricky one, one of the first problems that has taught me
backtracking effectively.

To solve this problem, the most straightforward approach is a brute force approach
since having the constraint the numbers have to be contiguous removes any clever
tricks with sorting and counting.

Simply put, the way to think about this problem is to recursively check each integer
in the list, for example with 36, we have 36^2 = 1296, which means we have the integers
[1, 2, 9, 6]

We need to go index by index and either concatenate the next integer at the index OR we
append it to the list

At index=0, we have no choice but to append ONLY since there is nothing
[1]

At index=1, we have two choices, we can either append OR combine
[1, 2]  OR  [12]

At index=2
( [1, 2, 9] or [1, 29] )   OR   ( [12, 9]  or  [129]  )

at index=3
[1, 2, 9, 6]-[1, 2, 96]  or  [1, 29, 6]-[1, 296]  or  [12, 9, 6]-[12, 96]  or  [129, 6]-[1296]

And our answer is [1, 29, 6] because 1 + 29 + 6 = 36 which was our original target we squared.
"""


class Solution:
    def get_ints(self, val: int) -> list[int]:
        ints: list[int] = []
        while val > 0:
            ints.append(val % 10)
            val = val // 10

        return ints[::-1]

    def concat_ints(self, prev: int, new: int) -> int:
        return prev * 10 + new

    def punishmentNumber(self, n: int) -> int:
        def backtrack(i: int, curr: list[int], ints: list[int], target: int) -> bool:
            if i == len(ints):
                return sum(curr) == target

            val = ints[i]

            # Get the response for appending to the last item
            # AND for appending as a new item to the list
            res: set[bool] = set()
            if i == 0:
                res.add(backtrack(i + 1, [val], ints, target))
            else:
                # Combine ints
                res.add(
                    backtrack(
                        i + 1,
                        [
                            *curr[:-1],
                            self.concat_ints(curr[-1], val),
                        ],
                        ints,
                        target,
                    )
                )

                # Append as a new integer
                res.add(backtrack(i + 1, [*curr, val], ints, target))

            return True in res

        res = 0
        for val in range(1, n + 1):
            if backtrack(0, [], self.get_ints(val**2), val):
                res += val**2

        return res


if __name__ == "__main__":
    test_case_1 = 10  # 182
    test_case_2 = 37  # 1478

    cls = Solution()
    ans = cls.punishmentNumber(test_case_1)
    print("-----")
    print(ans)
