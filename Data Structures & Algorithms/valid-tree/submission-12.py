class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([(0, -1)])
        visited = set()
        while queue:
            node, parent = queue.popleft()

            visited.add(node)

            for neighbor in graph[node]:
                if parent == neighbor:
                    continue
                if neighbor in visited:
                    return False
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                
        return len(visited) == n