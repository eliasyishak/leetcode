# https://leetcode.com/problems/daily-temperatures
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # The stack will a be monotonically decreasing stack where each item in
        # stack has a greater temperature than the one before it
        #
        # Example of a valid stack = [71, 70, 69]
        stack = []
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                _, s_i = stack.pop()

                # Use the stack item's index to calculate how many days passed
                res[s_i] = i - s_i

            stack.append((val, i))

        return res


if __name__ == "__main__":
    test_case_1 = [73, 74, 75, 71, 69, 72, 76, 73]  # [1,1,4,2,1,1,0,0]

    cls = Solution()
    ans = cls.dailyTemperatures(temperatures=test_case_1)
    print("-----")
    print(ans)
