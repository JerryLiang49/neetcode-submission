class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 dafult dictionary sets
        rset = defaultdict(set)
        cset = defaultdict(set)
        sset = defaultdict(set)
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == '.':
                    continue
                if curr in rset[r] or curr in cset[c] or curr in sset[(r//3, c//3)]:
                    return False
                rset[r].add(curr)
                cset[c].add(curr)
                sset[(r//3, c//3)].add(curr)
        return True