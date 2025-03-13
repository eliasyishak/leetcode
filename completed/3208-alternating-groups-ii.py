# https://leetcode.com/problems/alternating-groups-ii


from typing import TypedDict


class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        colors += colors
        res = 0

        left = 0
        # Because this is the right pointer, we will need to allow for
        # it to loop back on itself
        for right in range(1, n + k - 1):
            # We will reset our left pointer if we find that we
            # have two consecutive values
            if colors[right - 1] == colors[right]:
                left = right

            # If we find that the window is bigger than k, we can make
            # it back to smaller by moving the left pointer
            if right - left + 1 > k:
                left += 1

            # If we now have the right size window, that means it is valid
            if right - left + 1 == k:
                res += 1

        return res

    def numberOfAlternatingGroupsSlow(self, colors: list[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors
        res = 0

        for left in range(n):
            right = left + 1

            while colors[right - 1] != colors[right] and right - left + 1 <= k:
                right += 1

            if right - left == k:
                res += 1

        return res


class TestCaseType(TypedDict):
    colors: list[int]
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "colors": [0, 1, 0, 1, 0],
        "k": 3,
    }  # 3

    cls = Solution()
    ans = cls.numberOfAlternatingGroups(**test_case_1)
    print("------")
    print(ans)
