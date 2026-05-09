class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = dict()
        
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                result = dfs(i + 1, j + 1)
            else:
                result = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            
            memo[(i, j)] = result
            return result
            
        return dfs(0, 0)
            