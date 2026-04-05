class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def find_neighbors(r, c):
            result = []
            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]
            for i in range(4):
                newr = r + drow[i]
                newc = c + dcol[i]
                if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]):
                    result.append((newr, newc))
            return result

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = 0
            while queue:
                row, col = queue.popleft()
                for neighbor in find_neighbors(row, col):
                    nrow, ncol = neighbor
                    if int(grid[nrow][ncol]) == 1:
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) == 1:
                    bfs(i, j)
                    count += 1
                else:
                    continue
        return count
