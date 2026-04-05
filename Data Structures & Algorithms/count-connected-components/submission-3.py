class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        componets = 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                componets += 1

        return componets

        