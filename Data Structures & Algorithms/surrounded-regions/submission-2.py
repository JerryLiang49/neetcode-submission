class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
        queue = deque(boundary)
        while queue:
            r, c = queue.popleft()
            if (r, c) not in visited:
                visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == "O" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        
        return
