class Solution:
    def solve(self, board: List[List[str]]) -> None:

        boundary = []
        for r in range(len(board)):
            if board[r][0] == "O":
                boundary.append((r, 0))
            if board[r][len(board[0]) - 1] == "O":
                boundary.append((r, len(board[0]) - 1))
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                boundary.append((0, c))
            if board[len(board) - 1][c] == "O":
                boundary.append((len(board) - 1, c))
            
        def dfs(r, c, visited):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            
            if board[r][c] == "X":
                return
            
            if (r, c) not in visited:
                visited.add((r, c))
            else:
                return
            
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c - 1, visited)
            dfs(r, c + 1, visited)
             
        visited = set()
        for r, c in boundary:
            dfs(r, c, visited)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        
        return
