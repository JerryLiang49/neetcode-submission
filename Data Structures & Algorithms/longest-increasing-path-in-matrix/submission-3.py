class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(r, c, prev):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= prev:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
        
            best = 1
            best = max(best, 1 + dfs(r + 1, c, matrix[r][c]))
            best = max(best, 1 + dfs(r - 1, c, matrix[r][c]))
            best = max(best, 1 + dfs(r, c + 1, matrix[r][c]))
            best = max(best, 1 + dfs(r, c - 1, matrix[r][c]))

            memo[r][c] = best
            return memo[r][c]
    
        answer = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                answer = max(answer, dfs(r, c, float("-inf")))
        return answer
