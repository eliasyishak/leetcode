# https://leetcode.com/problems/find-largest-value-in-each-tree-row
"""
Simple problem that just requires to iterate through the tree level by level
and keeping track of a maximum value for that level.

Didn't need to solve this in IDE so just saving my code submitted.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res

        queue = deque([root])
        while queue:
            n = len(queue)
            level_max = -float("inf")
            for _ in range(n):
                node = queue.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_max)

        return res
