class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs():
            drow = [-1, 0, 1, 0]
            dcol = [0, -1, 0, 1]

            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    nrow = r + drow[i]
                    ncol = c + dcol[i]
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        if grid[nrow][ncol] == 2147483647:
                            grid[nrow][ncol] = grid[r][c] + 1
                            queue.append((nrow, ncol))

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        bfs()
        
