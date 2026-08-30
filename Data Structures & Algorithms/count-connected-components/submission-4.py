class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0

        visited = set()

        def bfs(i):
            queue = deque([i])
            while queue:
                node = queue.popleft()
                visited.add(node)

                for neighbor in graph[node]:                    
                    if neighbor not in visited:
                        queue.append(neighbor)
                    
        for i in range(n):
            if i not in visited:
                bfs(i)
                components += 1

        return components