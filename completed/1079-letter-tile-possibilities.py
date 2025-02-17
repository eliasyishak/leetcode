# https://leetcode.com/problems/letter-tile-possibilities
"""
Classic backtracking problem with recursion. You just have to consider
all possible strings that can be created with the provided characters.

The key is to perform an action and continue with the recursion, once that
finishes, undo the action you performed and continue with the next case.

Also important to know that you don't need to pass in a unique copy of counts
for each recursive call. You can pass by reference.

To check if it's the same object, you can use the id(...) function to check
the memory address of the obect... id(counts) --> if passing by reference, then this address
                                                  will be the same for all calls
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def get_counts() -> dict[str, int]:
            counts: dict[str, int] = {}
            for char in tiles:
                if char not in counts:
                    counts[char] = 0

                counts[char] += 1
            return counts

        def backtrack(curr: str, counts: dict[str, int]):
            if len(curr) > 0:
                res.add(curr)

            exit_now = True
            for _, count in counts.items():
                if count > 0:
                    exit_now = False

            if exit_now:
                return

            for char, count in counts.items():
                for _ in range(count):
                    # Add to the current string and decrement the count
                    curr += char
                    counts[char] -= 1

                    backtrack(curr, counts)

                    curr = curr[:-1]
                    counts[char] += 1

            return

        counts = get_counts()
        res: set[str] = set()

        backtrack("", counts)

        return len(res)


if __name__ == "__main__":
    test_case_1 = "AAB"  # 8
    test_case_2 = "AAABBC"  # 188
    test_case_3 = "V"  # 1

    cls = Solution()
    ans = cls.numTilePossibilities(test_case_2)
    print("------")
    print(ans)
