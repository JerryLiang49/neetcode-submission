class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * (len(edges) + 1)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        queue = deque()
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                queue.append(i)
            
        while queue:
            node = queue.popleft()
            indegree[node] -=1 
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)
                
        for a, b in reversed(edges):
            if indegree[a] > 0 and indegree[b] > 0:
                return [a, b]
            
        return []