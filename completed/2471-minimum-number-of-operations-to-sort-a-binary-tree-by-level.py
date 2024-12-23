# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level
"""
Fun problem to think through with tree data structures and level order traversal.
The BFS is fairly trivial to do, the challenge was understanding how to sort each
of the levels to minimize the number of swaps that need to be made.

To do this, we implement a "Cycle Sort" where we use extra space to store a sorted
array for each level along with a dictionary to lookup each of the values positions.

The key insight here was that each value in the tree is unique so the lookup
dictionary allowsus to confidentally store each value and their index without having
a conflict clash.
"""

from collections import deque
from typing import Optional

from utils.binary_tree.create import create_binary_tree
from utils.binary_tree.tree_node import TreeNode


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swaps = 0
        queue = deque([root])
        while queue:
            q_len = len(queue)
            level = []
            for _ in range(q_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            swaps += self.swap_count(level_nodes=level)

        return swaps

    def swap_count(self, level_nodes) -> int:
        """
        Helper function to take in the a levels nodes and returning
        the minimum number of swaps that need to be made to sort that list
        """

        current_swaps = 0

        # Create a lookup dictionary that will map each of the values in the level
        # to their current index -- we can do this and have no clashes among the keys
        # because in the problem statement, it tells us that all of the values in
        # tree will be UNIQUE
        lookup = {val: index for index, val in enumerate(level_nodes)}

        sorted_level = sorted(level_nodes)

        # Iterate through the indices for the list and check each position
        # against the sorted array and make the necessary swaps in the original
        # array as needed
        for i, _ in enumerate(level_nodes):
            if level_nodes[i] != sorted_level[i]:
                current_swaps += 1

                current_value = int(level_nodes[i])
                correct_value = int(sorted_level[i])

                correct_value_index = lookup[correct_value]

                # Perform the swap
                level_nodes[i] = correct_value
                level_nodes[correct_value_index] = current_value

                # Perform the swap as necessary in the lookup object as well
                lookup[current_value] = correct_value_index
                lookup[correct_value] = i

        return current_swaps


if __name__ == "__main__":
    test_case_1 = create_binary_tree(
        nodes=[1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
    )  # 3

    cls = Solution()
    ans = cls.minimumOperations(root=test_case_1)
    print("-----")
    print(ans)
