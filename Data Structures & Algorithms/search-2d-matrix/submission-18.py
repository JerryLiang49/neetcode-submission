class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                row = mid
                break
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1
        
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
            