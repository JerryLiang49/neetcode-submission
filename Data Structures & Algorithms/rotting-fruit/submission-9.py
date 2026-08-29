class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minutes = 0
        fresh = 0

        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                
        if not fresh: return 0
                
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        
        return minutes - 1 if not fresh else -1 