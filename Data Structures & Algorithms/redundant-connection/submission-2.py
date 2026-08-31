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
        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i)
            
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 1:
                    queue.append(neighbor)
        
        print(indegree)
        for a, b in reversed(edges):
            if indegree[a] > 1 and indegree[b] > 1:
                return [a, b]
