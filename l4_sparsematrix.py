#sparsematrix
#121910313015_chakrapani anisetti
#defining a function to find transpose
def transpose(matrix, B):
    for i in range(N):
        for j in range(N):
            B[i][j] = matrix[j][i]

        #initialising normal matrix
matrix=[[2,0,0,0],
        [0,4,5,0],
        [0,0,7,0],
        [0,4,0,5]]
for i in matrix:
    for j in i:
        print(j,end=" ")

#take an empty matrix
sparseMatrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j]!=0:
            #create an temporary matrix to store values
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")
for i in sparseMatrix:
    for j in i:
        print(j,end=" ")
    print()