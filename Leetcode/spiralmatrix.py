"""
 Given an m x n matrix, return all elements of the matrix in spiral
 order
"""
def spiral_matrix(matrix_table):
    top=0
    bottom=len(matrix_table)-1
    left=0
    right=len(matrix_table[0])-1
    result=[]
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix_table[top][i])
        top=top+1
        for i in range(top,bottom+1):
            result.append(matrix_table[i][right])
        right=right-1
        if top<=bottom and left<=right:
            for i in range(right,left-1,-1):
                result.append(matrix_table[bottom][i])
            bottom= bottom - 1
            for i in range(bottom,top-1,-1):
                result.append(matrix_table[i][left])
            left = left + 1

    return result


rows=int(input("Enter a number of matrix rows:"))
cols=int(input("Enter a number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input("enter a value"))
        row.append(element)
    matrix.append(row)
result_matrix=spiral_matrix(matrix)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

print("spiral traversal of given matrix",result_matrix)