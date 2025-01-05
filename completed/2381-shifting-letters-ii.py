# https://leetcode.com/problems/shifting-letters-ii
"""
Prefix sum problem that can be really optimized when you understand that you
don't need to set each of the indexes in all_shifts array for the range in
shifts array

For example, if we had [1, 3, 1] we could do the following:
- Assumption: s is 5 characters long

If we set each index, then our all_shifts array would be: [0, 1, 1, 1, 0],
this would require that we have a nested for loop

OR we could do the following [0, 1, 0, 0, -1] -- this is equivalent to the above
but we don't need to use a nest for loop to set each index, we instead use one extra
variable to keep track of previous shifts
"""

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        abc = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        all_shifts = [0] * n

        for left, right, direction in shifts:
            calculated_direction = 1 if direction == 1 else -1

            # Instead of doing the above which can be time consuming, we can simply
            # keep track of the indexes where the updates are being made and use a
            # variable to keep track of previous shifts
            #
            # This prevents the additional for loop within this for loop and reduces
            # time complexity
            all_shifts[left] += calculated_direction
            if right + 1 < n:
                # We need to go one index to the right of the "right" because
                # we need to "undo" the operation
                all_shifts[right + 1] += -calculated_direction

        # Use a variable to keep track of previous shifts; implementing the
        # prefix sum approach
        curr_shift = 0
        res = ""
        for j in range(n):
            curr_shift = (curr_shift + all_shifts[j]) % len(abc)
            new_char = chr((ord(s[j]) - ord("a") + curr_shift) % 26 + ord("a"))
            res += new_char

        return res

    def shiftingLetters_nestedForLoops(self, s: str, shifts: List[List[int]]) -> str:
        """
        This was my first pass, it has been further optimized above.
        """
        abc = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        all_shifts = [0] * n

        for left, right, direction in shifts:
            calculated_direction = 1 if direction == 1 else -1
            for i in range(left, right + 1):
                all_shifts[i] += calculated_direction

        res = ""
        for j, char in enumerate(s):
            new_char_index = (ord(char) - ord("a") + all_shifts[j]) % len(abc)
            res += abc[new_char_index]

        return res


if __name__ == "__main__":
    test_case_1 = {
        "s": "abc",
        "shifts": [[0, 1, 0], [1, 2, 1], [0, 2, 1]],
    }  # ace

    test_case_2 = {
        "s": "dztz",
        "shifts": [[0, 0, 0], [1, 1, 1]],
    }  # catz

    cls = Solution()
    ans = cls.shiftingLetters(**test_case_2)
    print("----")
    print(ans)
