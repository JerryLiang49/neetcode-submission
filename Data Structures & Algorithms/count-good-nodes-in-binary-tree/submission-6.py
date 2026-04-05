# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        currMax = root.val

        queue = deque([(root, currMax)]) 
        while queue:
            node, currMax = queue.popleft()
            if node.val >= currMax:
                result += 1
            if node.left:
                if node.left.val > currMax:
                    queue.append((node.left, node.left.val))
                else:
                    queue.append((node.left, currMax))
            if node.right:
                if node.right.val > currMax:
                    queue.append((node.right, node.right.val))
                else:
                    queue.append((node.right, currMax))
        
        return result