# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree
from collections import deque
from typing import Optional

from utils.binary_tree.create import create_binary_tree
from utils.binary_tree.tree_node import TreeNode


class Solution:
    def reverseOddLevelsBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append((root, 0))
        while queue:
            q_len = len(queue)
            current_level_values = []
            current_level = queue[0][-1]
            for _ in range(q_len):
                node, level = queue.popleft()
                current_level_values.append(node)

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            if current_level % 2 == 1:
                left = 0
                right = len(current_level_values) - 1
                while left < right:
                    current_level_values[left].val, current_level_values[right].val = (
                        current_level_values[right].val,
                        current_level_values[left].val,
                    )
                    left += 1
                    right -= 1

        return root

    def reverseOddLevelsDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_node: TreeNode, right_node: TreeNode, level: int):
            if left_node is None or right_node is None:
                return

            if level % 2 == 1:
                left_node.val, right_node.val = right_node.val, left_node.val

            outer_pair = [left_node.left, right_node.right]
            inner_pair = [left_node.right, right_node.left]

            dfs(left_node=outer_pair[0], right_node=outer_pair[1], level=level + 1)
            dfs(left_node=inner_pair[0], right_node=inner_pair[1], level=level + 1)

        dfs(left_node=root.left, right_node=root.right, level=1)

        return root


if __name__ == "__main__":
    test_case_1 = create_binary_tree(nodes=[2, 3, 5, 8, 13, 21, 34], verbose=True)

    cls = Solution()
    # ans = cls.reverseOddLevelsBFS(root=test_case_1)
    ansv2 = cls.reverseOddLevelsDFS(root=test_case_1)
    print("-----")
    print(ansv2)
