class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        
        def helper(i, j, k):

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word[k]:
                return False
            if k == n-1:
                return True
                
            # 1. Use the current word
            temp = board[i][j]
            board[i][j] = '#'

            found = (helper(i + 1, j, k + 1) or
                     helper(i - 1, j, k + 1) or
                     helper(i, j + 1, k + 1) or
                     helper(i, j - 1, k + 1))
            
            board[i][j] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if helper(r, c, 0):
                        return True

        return False
