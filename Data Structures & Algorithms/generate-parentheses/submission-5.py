class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
         
        def dfs(o, c, path):
            if o == c == n:
                result.append("".join(path))
                return
            
            if c < o:
                path.append(")")
                dfs(o, c + 1, path)
                path.pop()
            if o < n:
                path.append("(")
                dfs(o + 1, c, path)
                path.pop()
            
        dfs(0, 0, [])
        return result