# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                result.append("x")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        arr = data.split(",")
        if arr[0] == "x":
            return None

        root = TreeNode(int(arr[i]))
        queue = deque([root])
        
        i = 1
        while i < len(arr):
            node = queue.popleft()
            if arr[i] != "x":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1
            if arr[i] != "x":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                result.append("x")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        arr = data.split(",")
        if arr[0] == "x":
            return None

        root = TreeNode(int(arr[i]))
        queue = deque([root])
        
        i = 1
        while i < len(arr):
            node = queue.popleft()
            if arr[i] != "x":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1
            if arr[i] != "x":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root

        

