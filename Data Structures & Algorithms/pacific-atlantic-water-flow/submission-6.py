class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()

        def dfs(r, c, s, prevHeight):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            
            if heights[r][c] < prevHeight:
                return
            
            if (r, c) not in s:
                s.add((r, c))
            else:
                return
            
            dfs(r + 1, c, s, heights[r][c])
            dfs(r - 1, c, s, heights[r][c])
            dfs(r, c - 1, s, heights[r][c])
            dfs(r, c + 1, s, heights[r][c])

        pacific = []
        atlantic = []
        for r in range(len(heights)):
            pacific.append((r, 0))
            atlantic.append((r, len(heights[0]) - 1))
        
        for c in range(len(heights[0])):
            pacific.append((0, c))
            atlantic.append((len(heights) - 1, c))
        
        for r, c in pacific:
            dfs(r, c, pSet, heights[r][c])
        for r, c in atlantic:
            dfs(r, c, aSet, heights[r][c])
        
        result = []
        for r, c in pSet:
            if (r, c) in aSet:
                result.append([r, c])
            
        return result