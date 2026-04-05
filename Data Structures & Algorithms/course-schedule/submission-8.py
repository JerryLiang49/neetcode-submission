class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        visited = set()
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(c):
            if c in visited:
                return False
            
            if graph[c] == []:
                return True
            
            visited.add(c)
            for neighbor in graph[c]:
                if not dfs(neighbor):
                    return False
                
            visited.remove(c)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True