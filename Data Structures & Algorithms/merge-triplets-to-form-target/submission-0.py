class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr0, curr1, curr2 = 0, 0, 0
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            curr0 = max(curr0, t[0])
            curr1 = max(curr1, t[1])
            curr2 = max(curr2, t[2])
        
        return curr0 == target[0] and curr1 == target[1] and curr2 == target[2]