class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        queue = deque()
    
        def bfs():
            nonlocal time, fresh

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    grid[r][c] = 2
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                fresh -= 1
                                queue.append((nr, nc))
                if not queue:
                    return
                time += 1

        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if not fresh: return 0
        bfs()
        return time if not fresh else -1