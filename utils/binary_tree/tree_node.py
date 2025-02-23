from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
        verbose=True,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.verbose = verbose

    def __str__(self):
        if self.verbose:
            left_val = self.left if self.left is not None else None
            right_val = self.right if self.right is not None else None
        else:
            left_val = self.left.val if self.left is not None else None
            right_val = self.right.val if self.right is not None else None

        return str({"val": self.val, "left": left_val, "right": right_val})

    def __repr__(self):
        return self.__str__()
