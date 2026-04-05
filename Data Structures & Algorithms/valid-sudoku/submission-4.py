class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = defaultdict(list)
        cset = defaultdict(list)
        bset = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rset[r] or board[r][c] in cset[c] or board[r][c] in bset[(r//3, c//3)]:
                    return False
                rset[r].append(board[r][c])
                cset[c].append(board[r][c])
                bset[(r//3, c//3)].append(board[r][c])
        return True
                
