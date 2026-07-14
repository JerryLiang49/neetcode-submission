class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        dropoffHeap = []
        currPeople = 0
        
        for passengers, start, end in trips:
            while dropoffHeap and dropoffHeap[0][0] <= start:
                _, people = heapq.heappop(dropoffHeap)
                currPeople -= people
            
            if currPeople + passengers > capacity:
                return False
            
            currPeople += passengers
            heapq.heappush(dropoffHeap, (end, passengers))
        
        return True