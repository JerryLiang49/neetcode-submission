class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs():
            nonlocal area 

            while queue:
                r, c = queue.popleft()
                area += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

        maxA = 0
        area = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0
                    bfs()
                    maxA = max(maxA, area)
                    area = 0
                
        return maxA

        
