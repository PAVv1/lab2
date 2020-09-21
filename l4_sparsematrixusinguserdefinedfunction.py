#sparsematrix with user defined function
#121910313015_chakrapani anisetti
#defining a function
def displaymatrix(matrix):
    for r in matrix:
        for c in r:
            print(c,end=" ")
        print()


#convertion of normal matrix to sparse matrix
def converttosparse(matrix):
    #creating an empty list
     sparsematrix=[]
     for i in range(len(matrix)):
         for j in range(len(matrix[2])):
             if matrix[i][j]!=0:
                 temp=[]
                 temp.append(i)
                 temp.append(j)
                 temp.append(matrix[i][j])
                 sparsematrix.append(temp)

     print("\nsparsematrix")
     displaymatrix(sparsematrix)


normalmatrix=[[1,0,0,0],
              [0,2,0,0],
              [0,0,3,0],
              [0,0,0,4]]


displaymatrix(normalmatrix)
converttosparse(normalmatrix)
