class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
            
        result = 0
        visited = set()
        minHeap = [(0, 0)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            result += cost
            visited.add(node)
            for neiCost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
                
        return result