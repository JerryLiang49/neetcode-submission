class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def topo_sort(graph):
            nonlocal result, indegree
            queue = deque()

            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)

            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        
        result = []
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        topo_sort(graph)
        return len(result) == numCourses