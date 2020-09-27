#transpose of sparse
#121910313015_chakrapanianisetti
#defining a function represent Sparse Matrix
def sparsematrix1(a):
    spa = []
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                spa.append([i,j,a[i][j]])
    return spa

# Function to find transpose sparse matrix
def transpose1(a):
    res = []
    for i in a:
        res.append([i[1],i[0],i[2]])
    res.sort()
    return res


# Function to print martix
def printmatrix(a):
    if a==[]: print("Empty Matrix")
    for i in a:
        print(*i)

a = []
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
for i in range(r):
    d = list(map(int,input().split()))
    a.append(d)

print("The Original Matrix")
printmatrix(a)

print()

# Printing the sparse matrix
sp= sparsematrix1(a)
print("The Sparse Matrix")
printmatrix(sp)

# Printing the transpose of a sparse matrix
transpose = transpose1(sp)
print("The Transpose of the Sparse Matrix")
printmatrix(transpose)