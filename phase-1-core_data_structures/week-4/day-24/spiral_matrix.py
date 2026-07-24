def spiral_matrix(matrix):
    if not matrix:
        return []
    res=[]
    top,bottom=0,len(matrix)-1
    right,left=len(matrix[0])-1,0

    while left<=right and top <=bottom:
        for col in range(left,right+1):
            res.append(matrix[top][col])
        top+=1
        for row in range(top,bottom+1):
            res.append(matrix[row][right])
        right-=1
        if not (left<=right and top<=bottom):
            break
        for col in range(right,left-1,-1):
            res.append(matrix[bottom][col])
        bottom-=1
        for row in range(bottom,top-1,-1):
            res.append(matrix[row][left])
        left+=1
    return res
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1], [2], [3]]
print(spiral_matrix(matrix))