# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
"""
Tougher problem than normal but it is important to focus on the objective
and solve the sub problems as we go. We traverse the entire tree looking for
the deepest child and then we attempt to bubble up the LCA as we find it.

Alternatively, we could have solved this with BFS where we maintain a list
of nodes at each level, and then find the common parent for the left and right
most nodes by traversing the parent path until we find the same node value since
every node is unique
"""

from typing import Optional

from utils.binary_tree.create import create_binary_tree
from utils.binary_tree.tree_node import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return None, depth

            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_node, left_depth
            elif left_depth < right_depth:
                return right_node, right_depth

            return node, left_depth

        node, _ = dfs(root, 0)
        return node


if __name__ == "__main__":
    test_case_1 = create_binary_tree(
        nodes=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
    )  # [2, 7, 4]

    test_case_2 = create_binary_tree(
        nodes=[0, 1, 3, None, 2],
    )  # [2]

    cls = Solution()
    ans = cls.lcaDeepestLeaves(test_case_1)
    print("------")
    print(ans)
