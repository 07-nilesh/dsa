
def rotate_matix(matrix):
    n=len(matrix)
    for col in range(len(matrix)):
            for row in range(col+1,len(matrix)):
                matrix[col][row],matrix[row][col]=matrix[row][col],matrix[col][row]
    for rows in range(n):
         for col in range(n//2):
              matrix[rows][col],matrix[rows][n-1-col]=matrix[rows][n-1-col],matrix[rows][col]
        
    return matrix
                     
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matix(matrix))


