class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        def bfs(a):
            nonlocal visited, queue

            while queue:
                node, parent = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return False
                    visited.add(neighbor)
                    queue.append([neighbor, node])
            return True

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        visited.add(0)
        queue = deque([(0
        , -1)])

        if not bfs(0):
            return False

        return len(visited) == n

