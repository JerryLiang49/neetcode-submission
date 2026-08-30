class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        return result if len(result) == numCourses else []