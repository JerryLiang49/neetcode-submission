class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        componets = 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node):
            nonlocal componets
            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        visited = set()
        for i in range(n):
            if i not in visited:
                bfs(i)
                componets += 1

        return componets

        