class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            nonlocal area

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 0
                area += 1
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        maxA = 0
        area = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    maxA = max(maxA, area)
                    area = 0
                
        return maxA

        
