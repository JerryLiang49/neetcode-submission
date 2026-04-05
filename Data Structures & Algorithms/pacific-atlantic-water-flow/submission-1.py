class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        queue = deque()
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        result = []
        for c in range(len(heights[0])):
            queue.append((0, c))
        for r in range(len(heights)):
            queue.append((r, 0))
        while queue:
            r, c = queue.popleft()
            if (r, c) not in pacific:
                pacific.add((r, c))
            for i in range(4):
                nrow, ncol = r + drow[i], c + dcol[i]
                if 0 <= nrow < len(heights) and 0 <= ncol < len(heights[0]):
                    if heights[nrow][ncol] >= heights[r][c] and (nrow, ncol) not in pacific:
                        queue.append((nrow, ncol))

        for c in range(len(heights[0])):
            queue.append((len(heights) - 1, c))
        for r in range(len(heights)):
            queue.append((r, len(heights[0]) - 1))
        while queue:
            r, c = queue.popleft()
            if (r, c) not in atlantic:
                atlantic.add((r, c))
            for i in range(4):
                nrow, ncol = r + drow[i], c + dcol[i]
                if 0 <= nrow < len(heights) and 0 <= ncol < len(heights[0]) and (nrow, ncol) not in atlantic:
                    if heights[nrow][ncol] >= heights[r][c]:
                        queue.append((nrow, ncol))

        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])

        return result