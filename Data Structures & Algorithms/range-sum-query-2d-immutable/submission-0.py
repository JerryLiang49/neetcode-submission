class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                above = self.mat[r][c + 1]
                self.mat[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.mat[row2][col2]
        above = self.mat[row1 - 1][col2]
        left = self.mat[row2][col1 - 1]
        add = self.mat[row1 - 1][col1 - 1]
        return bottomRight - above - left + add
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)