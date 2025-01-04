# https://leetcode.com/problems/unique-length-3-palindromic-subsequences
"""
Simple problem since the palindrome is limited to only 3 characters. We
only need to find the first and last index for a character that appears
more than once and then we can get all the valid palindromes by iterating
between the first and last index for that substring.

We can further optimize the code to only doing one for loop as the editorial
suggests below

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans
```

This approach uses built in methods to find the first and last index instead
of a separate for loop to preprocess.
"""

from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        obj = defaultdict(list)
        for i, char in enumerate(s):
            if len(obj[char]) <= 1:
                obj[char].append(i)
            else:
                obj[char][-1] = i

        res = 0
        for char, indices in obj.items():
            if len(indices) == 2:
                palindromes = set()
                left, right = indices

                # We need to iterate between the left and right bounds and not
                # include the boundary itself
                for j in range(left + 1, right):
                    curr = f"{char}{s[j]}{char}"
                    if curr not in palindromes:
                        print(curr)
                        res += 1
                    palindromes.add(curr)

        return res


if __name__ == "__main__":
    test_case_1 = "aabca"  # 3
    test_case_2 = "bbcbaba"  # 4

    cls = Solution()
    ans = cls.countPalindromicSubsequence(test_case_2)
    print("-----")
    print(ans)
