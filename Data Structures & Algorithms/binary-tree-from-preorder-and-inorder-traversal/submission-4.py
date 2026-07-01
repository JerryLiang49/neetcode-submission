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
        
        self.rootIndex = 0 

        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.rootIndex])
            self.rootIndex += 1

            split = inorderDict[root.val]

            root.left = dfs(l, split - 1)
            root.right = dfs(split + 1, r)
            return root

        return dfs(0, len(preorder) - 1) 