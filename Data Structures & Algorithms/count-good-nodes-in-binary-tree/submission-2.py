# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        def dfs(root, max_val):
            nonlocal result
            if not root:
                return None
            
            if root.val >= max_val:
                result += 1
            
            dfs(root.left, max(max_val, root.val))
            dfs(root.right, max(max_val, root.val))
        
        dfs(root, root.val)
        return result