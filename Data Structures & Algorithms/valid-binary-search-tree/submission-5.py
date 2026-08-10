# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], low: Optional[TreeNode], high: Optional[TreeNode]):
        if not node:
            return True
        if low and node.val <= low.val:
            return False
        if high and node.val >= high.val:
            return False
        return self.dfs(node.left, low, node) and self.dfs(node.right, node, high)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, None, None)
        