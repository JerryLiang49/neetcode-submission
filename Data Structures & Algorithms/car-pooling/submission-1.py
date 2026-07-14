class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for passenger, start, end in trips:
            points.append((start, passenger))
            points.append((end, -passenger))
        
        points.sort()
        currPeople = 0
        for point, passenger in points:
            currPeople += passenger
            if currPeople > capacity:
                return False
            
        return True