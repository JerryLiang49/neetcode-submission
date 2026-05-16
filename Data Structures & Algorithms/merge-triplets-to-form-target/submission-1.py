class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr0, curr1, curr2 = False, False, False
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                curr0 = True
            if t[1] == target[1]:
                curr1 = True
            if t[2] == target[2]:
                curr2 = True
            if curr0 and curr1 and curr2:
                return True
        
        return False