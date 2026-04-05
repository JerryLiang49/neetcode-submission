class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            nonlocal visited
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components