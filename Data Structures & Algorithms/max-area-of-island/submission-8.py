class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currArea = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            nonlocal currArea
            queue = deque([(r, c)])

            while queue:
                row, col = queue.popleft()
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    currArea += 1
                    for drow, dcol in directions:
                        nrow, ncol = row + drow, col + dcol
                        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                            if grid[nrow][ncol] == 1:
                                queue.append((nrow, ncol))

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    bfs(r, c)
                    maxArea = max(maxArea, currArea)
                    currArea = 0
                
        return maxArea
