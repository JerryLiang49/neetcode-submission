class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = dict()
        
        def dfs(i, j):
            if j == len(p):
                if i == len(s):
                    return True
                else:
                    return False
            if (i, j) in memo:
                return memo[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                result = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return result
            
            if match:
                result = dfs(i + 1, j + 1)
                return result

            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)