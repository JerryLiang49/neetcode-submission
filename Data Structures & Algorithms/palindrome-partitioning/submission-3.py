class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isP(s):
            return s == s[::-1]
        
        result = []

        def dfs(index, path):
            if index == len(s):
                result.append(path[:])
                return
            
            for i in range(index, len(s)):
                if isP(s[index:i + 1]):
                    path.append(s[index:i + 1])
                
                    dfs(i + 1, path)
                    path.pop()
            
        dfs(0, [])
        return result