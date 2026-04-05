class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def bfs(node):
            nonlocal visited
            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                components += 1

        return components