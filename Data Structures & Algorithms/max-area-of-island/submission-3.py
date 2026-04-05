class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currArea = 0

        def dfs(r, c):
            nonlocal currArea

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 0
                currArea += 1
            else:
                return
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    maxArea = max(maxArea, currArea)
                    currArea = 0
                
        return maxArea
