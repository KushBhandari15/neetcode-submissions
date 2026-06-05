import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix[:] = np.transpose(matrix)
        matrix[:] = [row[::-1] for row in matrix]