class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        courses = 0
        
        def topo_sort(graph):
            nonlocal indegree, courses
            queue = deque()

            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
                
            while queue:
                n = queue.popleft()
                courses += 1
                for neighbor in graph[n]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        
        topo_sort(graph)
        return courses == numCourses