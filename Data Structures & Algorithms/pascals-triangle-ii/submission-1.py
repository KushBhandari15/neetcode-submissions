class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1] * (rowIndex + 1)

        for row in range(rowIndex+1):

            for col in range(row-1, 0, -1):
                res[col] = res[col-1] + res[col]
            
        return res

