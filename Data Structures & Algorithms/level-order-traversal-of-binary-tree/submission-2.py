# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            n = len(queue)
            new_level = []

            for _ in range(n):
                node = queue.popleft()
                if node:
                    new_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if new_level:   
                result.append(new_level)
        return result