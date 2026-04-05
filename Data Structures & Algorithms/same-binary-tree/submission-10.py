# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1:
            for _ in range(len(p1)):
                pN = p1.popleft()
                qN = q1.popleft()

                if not pN and not qN:
                    continue
                if pN and not qN or not pN and qN or pN.val != qN.val:
                    return False
                
                q1.append(qN.left)
                q1.append(qN.right)
                p1.append(pN.left)
                p1.append(pN.right)

        return not p1 and not q1
                
