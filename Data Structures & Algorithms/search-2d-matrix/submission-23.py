class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        row = 0
        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][-1] < target:
                t = mid + 1
            else:
                row = mid
                break
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
            
        return False