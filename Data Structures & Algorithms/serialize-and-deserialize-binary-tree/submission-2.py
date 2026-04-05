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

        def dfs(node):
            nonlocal result

            if not node:
                result += "x,"
                return result
            
            result += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        array = data.split(",")

        def dfs():
            nonlocal i, array

            if array[i] == "x":
                i += 1
                return None

            root = TreeNode(int(array[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()




