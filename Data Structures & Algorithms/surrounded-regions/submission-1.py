class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        neig = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                board[i][j] != "O"):
                return
            
            board[i][j] = "T"
            
            for x, y in neig:
                dfs(i + x, j + y)
            
        # Run dfs on borders
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        