class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        def bfs():
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    queue.append((r, c))
                    islands += 1
                    bfs()
        return islands

        