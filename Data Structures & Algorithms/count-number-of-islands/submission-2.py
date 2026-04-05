class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if len(grid) <= r or r < 0 or len(grid[0]) <= c or c < 0:
                return
            
            if int(grid[r][c]) == 0:
                return

            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r, c - 1)
            dfs(r-1, c)
            dfs(r, c+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) == 1:
                    dfs(i, j)
                    count += 1
        return count
