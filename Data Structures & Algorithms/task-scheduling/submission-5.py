class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqDict = dict()
        for t in tasks:
            freqDict[t] = 1 + freqDict.get(t, 0)
        
        maxHeap = [-f for f in freqDict.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        curr_time = 0
        while queue or maxHeap:
            curr_time += 1
            
            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq < 0:
                    queue.append((freq, curr_time + n))

            if queue and queue[0][1] == curr_time:
                freq, time = queue.popleft()
                heapq.heappush(maxHeap, freq)
            
        return curr_time