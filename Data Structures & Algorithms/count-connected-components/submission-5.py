class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0
        visited = set()

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for neighbor in graph[i]:
                dfs(neighbor)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components