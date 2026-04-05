# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0

        def dfs(root, max_value):
            nonlocal answer
            
            if not root:
                return None
            
            if root.val >= max_value:
                answer += 1
            
            dfs(root.left, max(max_value, root.val))
            dfs(root.right, max(max_value, root.val))
        
        dfs(root, root.val)
        return answer