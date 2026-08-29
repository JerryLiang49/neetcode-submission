"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d = dict()
        d[node] = Node(node.val)
        
        def dfs(node):
            if not node:
                return

            for neighbor in node.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val)
                    dfs(neighbor)
                d[node].neighbors.append(d[neighbor])
                
            
        dfs(node)
        return d[node]