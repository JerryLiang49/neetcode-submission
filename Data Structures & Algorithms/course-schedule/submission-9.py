class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
            
        taken = 0
            
        while queue:
            taken += 1
            course = queue.popleft()
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return True if taken == numCourses else False
