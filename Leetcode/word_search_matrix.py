"""Given an m x n grid of characters board and a string word, return
 true if the word exists in the grid.
 The word can be constructed from letters of sequentially adjacent
 cells, where adjacent cells are horizontally or vertically
 neighboring. The same letter cell may not be used more than once"""

def find(matrix_table,word,row,col,i=0):
    if i==len(word):
        return True
    if row >= len(matrix_table) or col>=len(matrix_table[0]) or row<0 or col<0 or word[i]!=matrix_table[row][col]:
        return False
    matrix_table[row][col]='*'
    result_character=find(matrix_table,word,row+1,col,i+1) or find(matrix_table,word,row,col+1,i+1) or find(matrix_table,word,row-1,col,i+1) or find(matrix_table,word,row,col-1,i+1)
    matrix_table[row][col]=word[i]
    return result_character

def word_search(matrix_table,matrix_rows,matrix_cols,word):
    for i in range (matrix_rows):
        for j in range(matrix_cols):
            if word[0]==matrix_table[i][j]:
               if find(matrix_table,word,i,j):
                   return True
    return False


rows=int(input("Enter a number of matrix rows:"))
cols=int(input("Enter a number of columns:"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        element=input("enter a value")
        row.append(element)
    matrix.append(row)
search_string=input("enter a search word")
if word_search(matrix,rows,cols,search_string):
    print("The given word is found in board")
else:
    print("The given word is not found in board")