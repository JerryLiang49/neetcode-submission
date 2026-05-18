class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQ = sorted(queries)

        minHeap = []
        result = dict()
        i = 0
        
        for q in sortedQ:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            result[q] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]