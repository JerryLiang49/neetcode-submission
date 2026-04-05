class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal area
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == 0:
                return
            
            area += 1
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = 0
                if grid[r][c] == 1:
                    dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea