class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])

        row=[False]*(m)
        col=[False]*(n)

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        
        #Now We have to update the matrix now

        for i in range(m):
            for j in range(n):
                if row[i]==True or col[j]==True:
                    matrix[i][j]=0
        return matrix


        