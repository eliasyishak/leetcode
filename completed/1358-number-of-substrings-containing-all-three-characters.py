# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
"""
Straightforward sliding window problem. The real optimization here is understanding that
once we have a valid window, the number of substrings that start at our left pointer
is equal to the length of the string minus the right pointer since every substring
after right will be valid.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        counts = [0, 0, 0]  # a, b, c counts
        left = 0
        for right in range(n):
            char = s[right]
            index = ord(char) - ord("a")

            counts[index] += 1

            while counts[0] and counts[1] and counts[2]:
                res += n - right

                left_char = s[left]
                left_index = ord(left_char) - ord("a")

                counts[left_index] -= 1

                left += 1

        return res


if __name__ == "__main__":
    test_case_1 = "abcabc"  # 10

    cls = Solution()
    ans = cls.numberOfSubstrings(test_case_1)
    print("-----")
    print(ans)
