class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
        
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True
        
        visited = set()
    
        return dfs(0, -1) and len(visited) == n