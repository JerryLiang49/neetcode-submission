# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0

            leftH = dfs(root.left)
            rightH = dfs(root.right)

            if leftH == -1 or rightH == -1:
                return -1

            if abs(leftH - rightH) > 1:
                return -1
            
            return 1 + max(leftH, rightH)
        
        result = dfs(root) 
        return result != -1