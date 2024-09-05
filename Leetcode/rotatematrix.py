"""You are given an n x n 2D matrix representing an image, rotate the
 image by 90 degrees (clockwise).
 You have to rotate the image in place, which means you have to
 modify the input 2D matrix directly. DO NOT allocate another 2D
 matrix and do the rotation"""

def rotate_matrix(matrix_table,matrix_row,matrix_col):
    new_matrix=[]
    for i in range(matrix_row):
        l=[]
        for j in range(matrix_col-1,-1,-1):
            l.append(matrix_table[j][i])
        new_matrix.append(l)
    return new_matrix


rows=int(input("Enter a number of matrix rows:"))
cols=int(input("Enter a number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input("enter a value"))
        row.append(element)
    matrix.append(row)

result_matrix=rotate_matrix(matrix_table=matrix,matrix_row=rows,matrix_col=cols)

for row in result_matrix:
    for col in row:
        print(col,end=" ")
    print()
