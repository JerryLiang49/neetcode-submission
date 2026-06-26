# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def dfs(node, parent):
            if not node:
                insert = TreeNode(val)
                if val < parent.val:
                    parent.left = insert
                else:
                    parent.right = insert
                return

            if val > node.val:
                dfs(node.right, node)
            else:
                dfs(node.left, node)

        dfs(root, None)
        return root 