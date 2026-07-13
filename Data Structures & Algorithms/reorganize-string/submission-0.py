class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""
        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        maxHeap = [(-f, char) for char, f in freq.items()]
        heapq.heapify(maxHeap)
        
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            freq, char = heapq.heappop(maxHeap)
            freq += 1
            result += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if freq < 0:
                prev = (freq, char)

        return result