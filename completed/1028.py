# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal
"""
This was a fun problem to think through. We are able to use the assumptions
around preorder traversal to know which parent to assign a current node. Looking
forward to more practice with the bianry trees but having a stack used to
determine the depth of the tree is the key insight to this problem.
"""

from typing import Optional

from utils.binary_tree.tree_node import TreeNode


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        # Get the root node value first to initialize the stack
        root_val_str = ""
        while i < len(traversal) and traversal[i].isdigit():
            root_val_str += traversal[i]
            i += 1

        root = TreeNode(val=int(root_val_str), verbose=True)

        stack: list[TreeNode] = [root]
        while i < len(traversal):
            curr_level = 0
            while traversal[i] == "-":
                curr_level += 1
                i += 1

            # Create value we are at
            j = int(i)
            curr_val_str = ""
            while j < len(traversal) and traversal[j].isdigit():
                curr_val_str += traversal[j]
                j += 1

            while len(stack) > curr_level:
                stack.pop()

            curr_val = int(curr_val_str)
            i = j

            # Connect the current with the parent
            curr_node = TreeNode(val=curr_val, verbose=True)

            top_node = stack[-1]
            if top_node.left is None:
                top_node.left = curr_node
            else:
                top_node.right = curr_node

            stack.append(curr_node)

        return root


if __name__ == "__main__":
    # Look at the link to find the answers to the test cases
    test_case_1 = "1-2--3--4-5--6--7"
    test_case_2 = "1-2--3---4-5--6---7"
    test_case_3 = "1-401--349---90--88"
    test_case_4 = "10-7--8"

    cls = Solution()
    ans = cls.recoverFromPreorder(test_case_4)
    print("-----")
    print(ans)
