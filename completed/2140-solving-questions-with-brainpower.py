# https://leetcode.com/problems/solving-questions-with-brainpower
"""
A spin on a classic dynamic problem with backtracking. You simulate what it would
look like selecting one option and then recurse further with the opposite choice
"""


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        cache: dict[int, int] = {}

        def helper(i: int) -> int:
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            points, cost = questions[i]

            # If we selected the current score
            selected = points + helper(i + cost + 1)
            skipped = helper(i + 1)

            val = max(selected, skipped)
            cache[i] = val
            return cache[i]

        return helper(0)


if __name__ == "__main__":
    test_case_1 = [[3, 2], [4, 3], [4, 4], [2, 5]]  # 5

    cls = Solution()
    ans = cls.mostPoints(test_case_1)
    print("------")
    print(ans)
