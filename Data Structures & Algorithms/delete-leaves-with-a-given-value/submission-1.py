# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visit = set()
        parent = {root: None}

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    p = parent[node]
                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visit:
                visit.add(node)
                stack.append(node)
                if node.left:
                    parent[node.left] = node
                    stack.append(node.left)
                if node.right:
                    parent[node.right] = node
                    stack.append(node.right)
                
        return root
                