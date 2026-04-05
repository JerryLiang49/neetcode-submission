class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        def topo_sort(graph):
            nonlocal indegree, order
            queue = deque()

            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
            
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        order = []

        indegree = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        topo_sort(graph)
        return order if len(order) == numCourses else []