# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p = deque([p])
        q = deque([q])

        while p and q:
            pN = p.popleft()
            qN = q.popleft()

            if not pN and not qN:
                continue
            if pN and not qN or not pN and qN or pN.val != qN.val:
                return False
            
            p.append(pN.left)
            p.append(pN.right)
            q.append(qN.left)
            q.append(qN.right)
        
        return not p and not q