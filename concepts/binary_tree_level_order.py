# https://leetcode.com/problems/binary-tree-preorder-traversal
"""
Demonstrates how to do a traversal of a binary tree level by level

Note, won't work running from here until I setup the top level package
"""

from typing import List, Optional

from utils.binary_tree.create import create_binary_tree
from utils.binary_tree.tree_node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


if __name__ == "__main__":
    # test_case = [1, None, 2, 3]
    test_case = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

    cls = Solution()
    ans = cls.preorderTraversal(root=create_binary_tree(test_case))

    print("-----")
    print(ans)
