# https://leetcode.com/problems/construct-smallest-number-from-di-string
"""
Another backtracking problem where we check numbers in increasing value
since the problem states that we want to find the smallest value possible
when sorted.

Something that tripped me up here is that the string you ultimately return
will be a string that is len(pattern) + 1. The first "I" or "D" applies to the
first value you place in the string.

This could have also been solved with a stack if you considered the conditions
that would require to pop from the stack

```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        num_stack = []

        # Iterate through the pattern
        for index in range(len(pattern) + 1):
            # Push the next number onto the stack
            num_stack.append(index + 1)

            # If 'I' is encountered or we reach the end, pop all stack elements
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))

        return "".join(result)
```
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(curr: str, added: set[int]) -> None:
            if len(res) > 0:
                return

            if len(curr) == len(pattern) + 1:
                res.add(curr)
                return

            index = len(curr) - 1
            for val in range(1, 10):
                # Need to satisfy the following conditions
                #
                # - The current val must not have been used already
                # - If the curr string is empty add whatever value is next
                # - If curr not empty and "I", ensure that value is greater than the last val
                #   - Vice versa for "D"
                if val not in added and (
                    len(curr) == 0
                    or (pattern[index] == "I" and val > int(curr[-1]))
                    or (pattern[index] == "D" and val < int(curr[-1]))
                ):
                    added.add(val)
                    curr += str(val)

                    backtrack(curr, added)

                    added.remove(val)
                    curr = curr[:-1]

        res: set[str] = set()
        backtrack("", set())

        return min(res)


if __name__ == "__main__":
    test_case_1 = "IIID" + "IDDD"  # "123549876"
    test_case_2 = "DDD"  # 4321

    cls = Solution()
    ans = cls.smallestNumber(test_case_2)
    print("-----")
    print(ans)
