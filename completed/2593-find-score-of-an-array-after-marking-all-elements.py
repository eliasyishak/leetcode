# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements
"""
Not a bad heap problem, the tricky part was to make sure you are not adding
indices that are outside of the allowed ranges since my top while loop exits
once we have the correct number of marked indices
"""

from typing import List
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        queue = [(val, index) for index, val in enumerate(nums)]
        heapq.heapify(queue)
        marked = set()
        score = 0

        while len(marked) < len(nums):
            while queue and queue[0][1] in marked:
                heapq.heappop(queue)

            if len(queue) > 0:
                current, index = heapq.heappop(queue)
                score += current
                marked.add(index)
                if 0 <= index - 1:
                    marked.add(index - 1)
                if index + 1 < len(nums):
                    marked.add(index + 1)

        return score


if __name__ == "__main__":
    test_case_1 = [
        2,
        1,
        3,
        4,
        5,
        2,
    ]  # 7
    test_case_2 = [
        2,
        3,
        5,
        1,
        3,
        2,
    ]  # 5

    cls = Solution()
    ans = cls.findScore(nums=test_case_2)
    print("----")
    print(ans)
