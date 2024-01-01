matrix1=[[1,5,6],[2,5,1],[3,2,4]]
matrix2=[[8,9,0],[3,9,7],[3,2,6]]
result_matrix=[]
for i in range(len(matrix1)):
    row=[]
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j]+matrix2[i][j])
    result_matrix.append(row)
print("result:")
for row in result_matrix:
    print(row)        