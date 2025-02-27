# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence
"""
There is probably a more optimized approach to this problem but this one made
the most sense to me. To handle this, we begin by first getting a dictionary
to map each value to the index it is at. We then use this in a recursive helper
to go seek out the third element in x1 + x2 == x3.

[1, 2, 3, 4, 5, 6, 7, 8]

We take, x1=1, x2=2 and use the seen dictionary to find where 1 + 2 = 3 is and use
that as the second input for the recursive helper

Also instead of doing this with a recursive stack, we can use a while loop that terminates
when it doesn't find the next value; solution below

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_set = set(arr)
        res = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    res = max(res, length)
        return res
"""


class Solution:
    def __init__(self):
        self.res = 0

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        seen = {val: i for i, val in enumerate(arr)}

        def dfs(x1: int, x2: int, curr_len: int):
            if x2 > n:
                return

            self.res = max(self.res, curr_len)

            if arr[x1] + arr[x2] in seen:
                # If we are initializing the curr_len for the first time
                if curr_len == 0:
                    curr_len = 2

                dfs(x1=x2, x2=seen[arr[x1] + arr[x2]], curr_len=curr_len + 1)

        for i in range(n):
            for j in range(i + 1, n):
                dfs(x1=i, x2=j, curr_len=0)

        return self.res


if __name__ == "__main__":
    test_case_1 = [1, 2, 3, 4, 5, 6, 7, 8]  # 5 length with arr [1,2,3,5,8]
    test_case_2 = [1, 3, 7, 11, 12, 14, 18]  # 3

    # 5 length with [4, 14, 18, 32, 50]
    test_case_3 = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]

    cls = Solution()
    ans = cls.lenLongestFibSubseq(test_case_3)
    print("-----")
    print(ans)
