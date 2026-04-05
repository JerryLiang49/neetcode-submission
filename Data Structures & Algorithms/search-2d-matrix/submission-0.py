class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0; bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if top > bot:
            return False
        row = (top + bot) // 2
        l = 0; r = len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
