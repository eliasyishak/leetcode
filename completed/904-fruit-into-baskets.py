# https://leetcode.com/problems/fruit-into-baskets
"""
The problem statement can be a little confusing but after rereading,
you can see that this is a longest continuous sequence problem. The gotcha
here was to know to use the dictionary to keep track of the counts of
each fruit that we have encountered.
"""

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        s: set[int] = set()
        counts: dict[int, int] = defaultdict(int)
        res = 0
        for r, fruit in enumerate(fruits):
            s.add(fruit)
            counts[fruit] += 1

            while len(s) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    s.remove(fruits[l])
                l += 1

            res = max(res, r - l + 1)

        return res


if __name__ == "__main__":
    test_case_1 = [1, 2, 3, 2, 2]  # 4
    test_case_2 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]  # 5

    cls = Solution()
    ans = cls.totalFruit(test_case_1)
    print("-----")
    print(ans)
