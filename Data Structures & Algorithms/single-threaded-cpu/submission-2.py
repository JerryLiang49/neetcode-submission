class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])
        
        result = []
        minHeap = []

        curr_time = tasks[0][0]
        i = 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and curr_time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not minHeap:
                curr_time = tasks[i][0]
            else:
                processT, index = heapq.heappop(minHeap)
                curr_time += processT
                result.append(index)
                    
        return result
