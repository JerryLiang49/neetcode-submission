# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""
        def dfs(root):
            nonlocal result

            if not root:
                result += "x,"
                return
            
            result += str(root.val) + ","
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        gPointer = 0
        array = data.split(",")

        def dfs():
            nonlocal gPointer, array

            if array[gPointer] == "x":
                gPointer += 1
                return None
            
            node = TreeNode(array[gPointer])
            gPointer += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()







