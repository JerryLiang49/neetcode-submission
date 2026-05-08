class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
    
        memo = dict()

        def dfs(i, j, k):
            if k >= len(s3):
                if i >= len(s1) and j >= len(s2):
                    return True
                else:
                    return False
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = False
            if i < len(s1) and s3[k] == s1[i]:
                result = dfs(i + 1, j, k + 1)

            if not result and j < len(s2) and s3[k] == s2[j]:
                result = dfs(i, j + 1, k + 1)
                   
            memo[(i, j)] = result
            return memo[(i, j)]
                
        return dfs(0,0,0)