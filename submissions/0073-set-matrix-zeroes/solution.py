class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = [], []
        rowCount = len(matrix)
        colCount = len(matrix[0])
        for i in range(rowCount):
            if 0 not in matrix[i]:
                continue
            row_entry = matrix[i]
            r.append(i)
            for j in range(colCount):
                if row_entry[j]==0:
                    if j not in c:
                        c.append(j)
        
        for element in r:
            matrix[element] = [0]*colCount
            
        for element in c:
            for i in range(rowCount):
                matrix[i][element] = 0
          
        # print(matrix)
        
