from typing import List, Optional

from utils.binary_tree.tree_node import TreeNode


def create_binary_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if len(nodes) == 0 or nodes[0] is None:
        print("Cannot create this!")
        return None

    root = TreeNode(val=nodes[0])
    internal_queue = [root]
    i = 1
    while internal_queue:
        _node = internal_queue.pop(0)

        if i < len(nodes) and nodes[i] is not None:
            _node.left = TreeNode(val=nodes[i])
            internal_queue.append(_node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            _node.right = TreeNode(val=nodes[i])
            internal_queue.append(_node.right)
        i += 1

    return root


if __name__ == "__main__":
    node_inputs = [1, None, 2, None, 3]

    tree = create_binary_tree(nodes=node_inputs)

    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
