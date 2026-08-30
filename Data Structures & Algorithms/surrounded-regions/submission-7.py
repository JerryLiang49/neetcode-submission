class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        visited = set()

        for r in range(len(board)):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][len(board[0]) - 1] == "O":
                queue.append((r, len(board[0]) - 1))

        for c in range(len(board[0])):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[len(board) - 1][c] == "O":
                queue.append((len(board) - 1, c))
        
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue
                
                if board[nr][nc] == "O" and (nr, nc) not in visited:
                    queue.append((nr, nc))
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"


