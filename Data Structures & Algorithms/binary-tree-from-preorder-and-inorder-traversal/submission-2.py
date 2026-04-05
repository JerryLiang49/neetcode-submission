# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderDict = dict()
        for i, n in enumerate(inorder):
            inorderDict[n] = i
        
        self.root_index = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.root_index])
            self.root_index += 1

            mid = inorderDict[root.val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)