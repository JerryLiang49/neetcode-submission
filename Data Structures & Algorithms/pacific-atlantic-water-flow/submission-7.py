class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(ocean, s):
            queue = deque(ocean)
            while queue:
                r, c = queue.popleft()
                if (r, c) not in s:
                    s.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                        if heights[nr][nc] >= heights[r][c] and (nr, nc) not in s:
                            queue.append((nr, nc)) 

        pacific = []
        atlantic = []
        for r in range(len(heights)):
            pacific.append((r, 0))
            atlantic.append((r, len(heights[0]) - 1))
        
        for c in range(len(heights[0])):
            pacific.append((0, c))
            atlantic.append((len(heights) - 1, c))
        
        bfs(pacific, pSet)
        bfs(atlantic, aSet)

        result = []
        for r, c in pSet:
            if (r, c) in aSet:
                result.append([r, c])
            
        return result