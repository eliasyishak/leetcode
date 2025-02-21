# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree
"""
This is a tree traversal problem that could have been solved with DFS
or BFS. I normally go for BFS where possible because it makes more sense for
me.
"""

from typing import Optional

from utils.binary_tree.create import create_binary_tree
from utils.binary_tree.tree_node import TreeNode


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.num_set: set[int] = set()

        queue: list[tuple[TreeNode, int]] = []
        if root is not None:
            queue.append((root, 0))

        while queue:
            curr_node, curr_val = queue.pop(0)

            self.num_set.add(curr_val)

            if curr_node.left is not None:
                queue.append((curr_node.left, 2 * curr_val + 1))

            if curr_node.right is not None:
                queue.append((curr_node.right, 2 * curr_val + 2))

    def find(self, target: int) -> bool:
        return target in self.num_set


if __name__ == "__main__":
    test_case_1 = create_binary_tree([-1, None, -1])

    cls = FindElements(test_case_1)
    print("--------")
    print(cls.find(1))  # false
    print(cls.find(2))  # true
