# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        
        queue = deque([(root, float("-inf"))])
        while queue:
            node, currMax = queue.popleft()
            if node.val >= currMax:
                answer += 1
            if node.left:
                queue.append((node.left, max(currMax, node.val)))
            if node.right:
                queue.append((node.right, max(currMax, node.val)))
            
        return answer