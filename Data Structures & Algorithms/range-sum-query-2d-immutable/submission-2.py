class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.helper = [[0] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            running_sum = 0
            for c in range(self.cols):
                print(r, c)
                running_sum += matrix[r][c]
                self.helper[r][c] = running_sum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = 0
        for r in range(row1, row2 + 1):
            subtract = 0
            if col1 - 1 >= 0:
                subtract = self.helper[r][col1 - 1]
            res += self.helper[r][col2] - subtract
        
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)