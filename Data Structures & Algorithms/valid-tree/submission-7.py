class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs(a):
            while queue:
                node, parent = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return False    
                    queue.append((neighbor, node))
                    visited.add(neighbor)
            return True

        visited = set()
        visited.add(0)
        queue = deque([(0, -1)])
        
        if not bfs(0):
            return False

        return len(visited) == n
