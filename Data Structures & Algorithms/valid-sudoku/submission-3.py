class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rDict = defaultdict(set)
        cDict = defaultdict(set)
        bDict = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rDict[r] or curr in cDict[c] or curr in bDict[(r//3, c//3)]:
                    return False
                rDict[r].add(curr)
                cDict[c].add(curr)
                bDict[(r//3, c//3)].add(curr)
        return True