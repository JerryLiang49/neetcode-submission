class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
                
        hold = None
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            count += 1 
            result += char

            if hold:
                heapq.heappush(maxHeap, hold)
                hold = None

            if count < 0:
                if result[-2:] == char * 2:
                    hold = (count, char)
                else:
                    heapq.heappush(maxHeap, (count, char))
            
        return result
