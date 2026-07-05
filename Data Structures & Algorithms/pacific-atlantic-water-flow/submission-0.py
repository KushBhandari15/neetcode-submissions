class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(i, j, visited):
            
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                row, col = stack.pop()
                neighbor = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for nei in neighbor:
                    n_row, n_col = row + nei[0], col + nei[1]

                    if 0 <= n_row < rows and 0 <= n_col < cols:
                        if ((n_row, n_col)) not in visited and heights[n_row][n_col] >= heights[row][col]:
                            stack.append((n_row, n_col))
                            visited.add((n_row, n_col))

        pacific = set()
        atlantic = set()
        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows-1, col, atlantic)
        
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols-1, atlantic)
        
        print(pacific)
        print(atlantic)
        res = pacific.intersection(atlantic)
        return list(res)
            

