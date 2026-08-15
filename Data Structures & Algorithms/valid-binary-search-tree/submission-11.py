# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, left, curr, right):
        if not curr:
            return True
        if left and left.val >= curr.val:
            return False
        if right and right.val <= curr.val:
            return False
        return self.dfs(left, curr.left, curr) and self.dfs(curr, curr.right, right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(None, root, None)
        