# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            n = len(queue)
            rightNode = None

            for _ in range(n):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightNode:
                result.append(rightNode.val)

        return result