# https://leetcode.com/problems/fruits-into-baskets-ii
"""
The only real way to solve this without making it super complicated
is to just do an O(n^2) solution. The constraints to this problem
are not too restrictive.
"""


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        filled: set[int] = set()
        res = 0
        for fruit_count in fruits:
            for i, basket_capacity in enumerate(baskets):
                if i in filled:
                    continue

                if basket_capacity >= fruit_count:
                    res += 1
                    filled.add(i)
                    break

        return len(fruits) - res


if __name__ == "__main__":
    test_case_1 = {
        "fruits": [4, 2, 5],
        "baskets": [3, 5, 4],
    }  # 1

    cls = Solution()
    ans = cls.numOfUnplacedFruits(**test_case_1)
    print("-------")
    print(ans)
