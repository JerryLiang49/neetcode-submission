class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
    
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == -1 or grid[nr][nc] == 0:
                    continue
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc)) 