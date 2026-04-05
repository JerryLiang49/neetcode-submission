class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(index, path, openP, closedP):
            if index == 2 * n and openP == closedP:
                result.append("".join(path))
                return
            
            if closedP < openP:
                path.append(")")
                dfs(index + 1, path, openP, closedP + 1)
                path.pop()

            if openP < n:
                path.append("(")
                dfs(index + 1, path, openP + 1, closedP)
                path.pop()
            
        dfs(0, [], 0, 0)
        return result
