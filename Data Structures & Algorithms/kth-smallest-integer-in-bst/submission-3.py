# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = 0

        def dfs(root):
            nonlocal count, result

            if not root:
                return
        
            dfs(root.left)

            count -= 1
            if not count:
                result = root.val

            dfs(root.right)
        
        dfs(root)
        return result