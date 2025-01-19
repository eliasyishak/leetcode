# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
from typing import TypedDict


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # DOESN'T COVER ALL TEST CASES BUT GOOD ENOUGH FOR ME :)
        left = 0
        right = len(s) - 1
        turns = 0

        counts = {char: 0 for char in "abc"}
        complete = False

        while left <= right:
            left_char = s[left]
            right_char = s[right]

            if counts[left_char] < k or counts[right_char] < k:
                if counts[left_char] < k:
                    counts[left_char] += 1
                    left += 1
                    turns += 1

                if counts[right_char] < k:
                    counts[right_char] += 1
                    right -= 1
                    turns += 1

            # This is the case where the next character we take in will be
            # excess of k so we need to find the side with the shortest distance
            # to next character
            else:
                chars_needed = set()
                for char, count in counts.items():
                    if count < k:
                        chars_needed.add(char)

                if len(chars_needed) == 0:
                    complete = True
                    break

                temp_left, temp_right = left, right

                # Seek from both directions and return out when we have found
                # a character that we need
                left_count = {char: 0 for char in "abc"}
                while temp_left < len(s):
                    left_count[s[temp_left]] += 1
                    if s[temp_left] in chars_needed:
                        break
                    temp_left += 1

                right_count = {char: 0 for char in "abc"}
                while temp_right >= 0:
                    right_count[s[temp_right]] += 1
                    if s[temp_right] in chars_needed:
                        break
                    temp_right -= 1

                if abs(right - temp_right) <= abs(left - temp_left):
                    final_count = right_count
                    right = temp_right
                else:
                    final_count = left_count
                    left = temp_left

                for char, count in final_count.items():
                    counts[char] += count
                    turns += count

        if not complete and counts["a"] >= k and counts["b"] >= k and counts["c"] >= k:
            complete = True

        return turns if complete else -1


class TestCaseType(TypedDict):
    s: str
    k: int


if __name__ == "__main__":
    test_case_1: TestCaseType = {"s": "aabaaaacaabc", "k": 2}
    test_case_2: TestCaseType = {"s": "abc", "k": 1}
    test_case_3: TestCaseType = {"s": "cbbac", "k": 1}

    test_case = test_case_3
    cls = Solution()
    print(cls.takeCharacters(s=test_case["s"], k=test_case["k"]))
