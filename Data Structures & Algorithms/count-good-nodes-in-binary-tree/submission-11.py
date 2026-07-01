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
            currMax = max(currMax, node.val)
            if node.left:
                queue.append((node.left, currMax))
            if node.right:
                queue.append((node.right, currMax))
            
        return answer