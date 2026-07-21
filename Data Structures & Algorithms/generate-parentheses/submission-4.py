class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(op, closed, n, path):
            if op == closed == n:
                result.append("".join(path))
                return

            if op < n:
                path.append("(")
                dfs(op + 1, closed, n, path)
                path.pop()
            if closed < op:
                path.append(")")
                dfs(op, closed + 1, n, path)
                path.pop()
        
        dfs(0, 0, n, [])
        return result