class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prev = [1]

        for row in range(rowIndex+1):

            curr = [0] * (row+1)
            curr[0], curr[row] = 1, 1

            for col in range(1, row):
                curr[col] = prev[col-1] + prev[col]
            
            prev = curr
        
        return prev

