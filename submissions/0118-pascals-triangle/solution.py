class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for i in range(numRows):
            row_list = []
            for j in range(i+1):
                if j==0 or j==i:
                    row_list.append(1)
                else:
                    row_list.append(pascal_triangle[i-1][j-1]+pascal_triangle[i-1][j])
            pascal_triangle.append(row_list)
        return pascal_triangle
