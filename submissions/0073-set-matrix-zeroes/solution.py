class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        firstRowZero, firstColZero = False, False
        
        if 0 in matrix[0]:
            firstRowZero = True
        
        for i in range(rowCount):
            if matrix[i][0]==0:
                firstColZero = True
                break
            
        for i in range(1, rowCount):
            for j in range(1, colCount):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, rowCount):
            for j in range(1, colCount):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if firstRowZero:
            matrix[0] = [0]*colCount
        
        if firstColZero:
            for i in range(rowCount):
                matrix[i][0] = 0
        
