class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(i):
            if i in visited: # cycle detected
                return False
            
            if graph[i] == []: # no more prereqs - can take this class
                return True
            
            visited.add(i)

            for prereq in graph[i]:
                if not dfs(prereq):
                    return False

            visited.remove(i)

            #ægraph[i] = [] # clear its prereq list

            return True
        
        visited = set()
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b) # b is a prerequisite for a
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True