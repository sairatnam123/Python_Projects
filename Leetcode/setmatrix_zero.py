"""Given an m x n integer matrix, if an element is 0, set its entire row
 and column to 0's. You must do it in place"""

def set_matrix_zeroes(matrix_table,matrix_rows,matrix_cols):
    jth_index=[]
    for i in range(matrix_rows):
        k=0
        for j in range(matrix_cols):
            if matrix_table[i][j]==0:
                k=k+1
                matrix_table[i]=[0 for i in range(matrix_cols)]
                if k==1:
                    jth_index.append(j)
    for i in range(matrix_rows):
        for j in range(len(jth_index)):
            index=jth_index[j]
            matrix_table[i][index]=0
    return matrix_table

rows=int(input("Enter a number of matrix rows:"))
cols=int(input("Enter a number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input("enter a value"))
        row.append(element)
    matrix.append(row)
result_matrix=set_matrix_zeroes(matrix,rows,cols)

for i in result_matrix:
    for j in i:
        print(j,end=" ")
    print()






