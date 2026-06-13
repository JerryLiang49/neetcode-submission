class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        
        i = 0
        j = len(arr) - 1
        while i < j:
            if (j - i + 1) == k:
                break
            diff1 = abs(arr[i] - x)
            diff2 = abs(arr[j] - x)
            if diff1 > diff2:
                i += 1
            else:
                j -= 1
            
        return arr[i:j + 1]