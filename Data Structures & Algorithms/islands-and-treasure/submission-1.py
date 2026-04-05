class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()

        def bfs():
            while queue:
                row, col = queue.popleft()
                for drow, dcol in directions:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        if grid[nrow][ncol] == 2147483647:
                            grid[nrow][ncol] = grid[row][col] + 1
                            queue.append((nrow, ncol))
                        
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        bfs()
        