class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        result = []
        courses = 0
        def topo_sort(graph):
            nonlocal indegree, result
            
            queue = deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
                
            while queue:
                i = queue.popleft()
                result.append(i)
                for neighbor in graph[i]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        
        topo_sort(graph)
        return [] if len(result) != numCourses else result