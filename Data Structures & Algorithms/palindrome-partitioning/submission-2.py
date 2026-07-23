class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(s):
            return s == s[::-1]
        
        def dfs(index, path):
            if index == len(s):
                result.append(path.copy())
                return
            
            for i in range(index, len(s)):
                if is_palindrome(s[index:i+1]):
                    path.append(s[index:i+1])
                    dfs(i + 1, path)
                    path.pop()
                
        dfs(0, [])
        return result