class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        visited = set()
        ans = 0
        minHeap = [(0, k)]

        while minHeap:
            weight, nei = heapq.heappop(minHeap)
            if nei in visited:
                continue
            visited.add(nei)
            time = weight

            for neighbbor, w in graph[nei]:
                if neighbbor not in visited:
                    heapq.heappush(minHeap, (weight + w, neighbbor))

        return time if len(visited) == n else -1
