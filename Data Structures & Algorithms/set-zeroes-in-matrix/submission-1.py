class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        col1 = 1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if j == 0:
                        col1 = 0
                        matrix[i][0] = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
            
        if col1 == 0:
            for i in range(row):
                matrix[i][0] = 0

        
        