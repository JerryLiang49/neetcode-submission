class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        def bfs(r, c):
            area = 1
            queue = deque([(r, c)])
            grid[r][c] = 0
            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    nrow, ncol = r + drow[i], c + dcol[i]
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        if grid[nrow][ncol] == 1:
                            area += 1
                            queue.append((nrow, ncol))
                            grid[nrow][ncol] = 0
            return area

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea