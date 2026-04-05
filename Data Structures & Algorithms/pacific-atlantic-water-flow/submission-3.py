class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited:
                return
            
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return

            if heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        for r, c in pacific:
            dfs(r, c, pac, heights[r][c])
        for r, c in atlantic:
            dfs(r, c, atl, heights[r][c])

        res = []
        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        return res