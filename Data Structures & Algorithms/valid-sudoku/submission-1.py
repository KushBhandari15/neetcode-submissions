class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for i in range (len(board)):
            for j in range (len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                curr_box = (i//3)*3 + (j//3)
                if curr in rows[i] or curr in cols[j] or curr in boxs[curr_box]:
                    return False
                rows[i].add(curr); cols[j].add(curr); boxs[curr_box].add(curr)
        
        return True