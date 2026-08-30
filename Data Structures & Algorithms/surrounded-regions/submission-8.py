class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            if board[r][c] == "O":
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

 
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][len(board[0]) - 1] == "O":
                dfs(r, len(board[0]) - 1)

        for c in range(len(board[0])):
            if board[0][c] == "O":
                dfs(0, c)
            if board[len(board) - 1][c] == "O":
                dfs(len(board) - 1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited:
                    board[r][c] = "X"