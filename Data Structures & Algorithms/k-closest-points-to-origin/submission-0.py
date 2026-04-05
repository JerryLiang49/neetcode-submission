class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            heapq.heappush(minheap, (point[0]**2 + point[1]**2, point[0], point[1]))

        result = []
        while len(result) < k:
            _, x, y = heapq.heappop(minheap)
            result.append([x, y])

        return result
