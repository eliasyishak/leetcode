# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence
from typing import Optional


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        def next_index(curr_index: int, curr_list: list[Optional[int]]) -> int:
            while curr_index < len(curr_list) and curr_list[curr_index] is not None:
                curr_index += 1
            return curr_index

        def backtrack(index: int, curr: list[Optional[int]], added: set[int]) -> None:
            if len(res) > 0:
                return

            if index == len(curr):
                if None not in curr:
                    res.append([val for val in curr if val is not None])
                return

            for val in range(n, 0, -1):
                if val > 1:
                    if index + val >= len(curr):
                        continue
                    if (
                        val not in added
                        and curr[index] is None
                        and curr[index + val] is None
                    ):
                        added.add(val)
                        curr[index] = val
                        curr[index + val] = val
                        backtrack(
                            index=next_index(index, curr),
                            curr=curr,
                            added=added,
                        )
                        curr[index] = None
                        curr[index + val] = None
                        added.remove(val)
                else:
                    if val not in added and curr[index] is None:
                        added.add(val)
                        curr[index] = val
                        backtrack(
                            index=next_index(index, curr),
                            curr=curr,
                            added=added,
                        )
                        curr[index] = None
                        added.remove(val)

        res: list[list[int]] = []
        backtrack(
            index=0,
            curr=[None] * (2 * (n - 1) + 1),
            added=set(),
        )

        # The problem states that there will always be one valid answer
        return res[0]


if __name__ == "__main__":
    test_case_1 = 3  # [3,1,2,3,2]
    test_case_2 = 5  # [5,3,1,4,3,5,2,4,2]
    test_case_3 = 4  # [4,2,3,2,4,3,1]
    test_case_4 = 12

    cls = Solution()
    ans = cls.constructDistancedSequence(test_case_4)
    print("-----")
    print(ans)
