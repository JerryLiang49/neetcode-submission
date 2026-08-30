class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()
        result = []

        def dfs(r, c, s, prevHeight):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            
            if (r, c) in s:
                return

            currH = heights[r][c]
            if currH >= prevHeight:
                s.add((r, c))

                dfs(r - 1, c, s, currH)
                dfs(r + 1, c, s, currH)
                dfs(r, c - 1, s, currH)
                dfs(r, c + 1, s, currH)

        for c in range(len(heights[0])):
            dfs(0, c, pSet, -1)
            dfs(len(heights)-1, c, aSet, -1)
        
        for r in range(len(heights)):
            dfs(r, 0, pSet, -1)
            dfs(r, len(heights[0]) - 1, aSet, -1)

        for r, c in pSet:
            if (r, c) in aSet:
                result.append([r, c])
            
        return result