
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        leftValue = self.minDepth(root.left)
        rightValue = self.minDepth(root.right)
        
        return min(leftValue,rightValue) + 1


