# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
"""
A backtracking problem that has either add the current character or
check the next one.

The only tough part is ensuring that we don't repeat characters and ensure
we are creating our words list in sorted order so we don't need to sort
the list again after creating it.

Once we are sure we are creating the list in sorted order, we can
further optimize by exiting the recursion once we have found the kth
element in the sorted array.
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        words: list[str] = []

        def backtrack(curr: str):
            if len(curr) == n:
                words.append(curr)
                return

            # Early exit if we have reached k
            if len(words) == k:
                return

            for char in "abc":
                if len(curr) == 0:
                    curr += char
                    backtrack(curr)
                    curr = curr[:-1]

                elif curr[-1] != char:
                    curr += char

                    backtrack(curr)
                    curr = curr[:-1]

            return

        backtrack("")
        return words[k - 1] if k - 1 < len(words) else ""


if __name__ == "__main__":
    test_case_1 = {
        "n": 1,
        "k": 3,
    }  # "c"

    test_case_2 = {
        "n": 1,
        "k": 4,
    }  # ""

    test_case_3 = {
        "n": 3,
        "k": 9,
    }  # "cab"

    cls = Solution()
    ans = cls.getHappyString(**test_case_3)
    print("-----")
    print(ans)
