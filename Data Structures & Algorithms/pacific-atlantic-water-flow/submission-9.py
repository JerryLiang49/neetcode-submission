class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()
        pacific = []
        atlantic = []
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(ocean, s):
            queue = deque(ocean)
            while queue:
                r, c = queue.popleft()
                s.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]):
                        continue
                    
                    if (nr, nc) in s:
                        continue
                    
                    if heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
                        s.add((nr, nc))

        for c in range(len(heights[0])):
            pacific.append((0, c))
            atlantic.append((len(heights) - 1, c))
        
        for r in range(len(heights)):
            pacific.append((r, 0))
            atlantic.append((r, len(heights[0]) - 1))

        bfs(pacific, pSet)
        bfs(atlantic, aSet)

        for r, c in pSet:
            if (r, c) in aSet:
                result.append([r, c])
            
        return result