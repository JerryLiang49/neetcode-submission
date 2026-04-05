class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0 

        queue = deque()

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

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
                for i in range(4):
                    nrow, ncol = r + drow[i], c + dcol[i]
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        if grid[nrow][ncol] == 1:
                            grid[nrow][ncol] = 2
                            fresh -= 1
                            queue.append((nrow, ncol))
            time += 1
        return time - 1 if not fresh else -1