class Solution:
    def solve(self, board: List[List[str]]) -> None:
    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(boundary, visited):
            queue = deque(boundary)

            while queue:
                r, c = queue.popleft()
                if (r, c) not in visited:
                    visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                        if (nr, nc) not in visited and board[nr][nc] == "O":
                            queue.append((nr, nc))

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
        
        visited = set()

        bfs(boundary, visited)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited and board[r][c] != "X":
                    board[r][c] = "X"
            


