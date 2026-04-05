# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo = min(p.val, q.val)
        hi = max(p.val, q.val)

        if not root:
            return None
        
        if lo < root.val < hi or lo == root.val or hi == root.val:
            return root
        elif lo < root.val and hi < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        

