class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            if board[r][c] != word[index] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            result = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)

            visited.remove((r, c))
            return result
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
            