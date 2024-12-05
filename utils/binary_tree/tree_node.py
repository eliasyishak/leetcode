class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        left_val = self.left.val if self.left is not None else None
        right_val = self.right.val if self.right is not None else None

        return str({"val": self.val, "left": left_val, "right": right_val})
