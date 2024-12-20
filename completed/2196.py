# https://leetcode.com/problems/create-binary-tree-from-descriptions
"""
Good tree problem to understand how to construct using an adjacency list.

We can also solve this simply using a dictionary where each key is a node value
and the value for each node is the TreeNode instance itself. This is shown in the V2
implementation.
"""

from collections import deque
from typing import List, Optional

from utils.binary_tree.tree_node import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adj = {}
        all_nodes = set()
        child_nodes = set()
        for parent, child, is_left in descriptions:
            if parent not in adj:
                adj[parent] = []
            adj[parent].append((child, is_left == 1))
            all_nodes.add(parent)
            all_nodes.add(child)
            child_nodes.add(child)

        nodes_without_parents = all_nodes.difference(child_nodes)
        if len(nodes_without_parents) != 1:
            raise ValueError("Could not find root node")

        # Start from our root node
        root = TreeNode(val=nodes_without_parents.pop())
        queue = deque([root])
        while queue:
            q_length = len(queue)
            for _ in range(q_length):
                node = queue.popleft()

                if node.val not in adj:
                    continue

                for neighbor, is_left in adj[node.val]:
                    if is_left:
                        node.left = TreeNode(val=neighbor)
                        queue.append(node.left)
                    else:
                        node.right = TreeNode(val=neighbor)
                        queue.append(node.right)

        return root

    def createBinaryTreeV2(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        This approach uses only a dictionary for storing refernces to values
        """

        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            for val in [parent, child]:
                if val not in nodes:
                    nodes[val] = TreeNode(val=val)

            children.add(child)
            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        # Find the root node by finding a value that is not in the children set
        for val, node in nodes.items():
            if val not in children:
                return node
        return None


if __name__ == "__main__":
    test_case_1 = [
        [20, 15, 1],
        [20, 17, 0],
        [50, 20, 1],
        [50, 80, 0],
        [80, 19, 1],
    ]

    cls = Solution()
    ans = cls.createBinaryTree(descriptions=test_case_1)
    ans2 = cls.createBinaryTreeV2(descriptions=test_case_1)
    print("-----")
    print(ans, ans2)
