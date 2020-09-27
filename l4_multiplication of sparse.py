#multiplication of sparse matrices
#121910313015_chakrapanianisetti
#defining a function represent Sparse Matrix
# Program to Multiply Sparse Matrices

def sparsematrix(a):
    res = []
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                res.append([i,j,a[i][j]])
    return res

#defining a function for multiplication of two sparse matrices
def mul(a1,a2):
    row1 = len(a1)
    row2 = len(a2)
    col2 = len(a2[0])
    res = [[0 for _ in range(col2)] for __ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                res[i][j] += a1[i][k]*a2[k][j]
    sparse1 = sparsematrix(res)
    return sparse1

# defining a function to print martix
def display(a):
    if a==[]: print('EMPTY MATRIX')
    for i in a:
        print(*i)

# defining a Function to take input
def input_matrix(row):
    a = [] # Declaring the matrix
    i = 0
    while i<row:
        temp = list(map(int,input().split()))
        a.append(temp)
        i += 1
    return a

row1 = int(input("Enter the number of rows in first matrix : "))
col1 = int(input("Enter the number of columns in first matrix : "))
row2 = int(input("Enter the number of rows in second matrix : "))
col2 = int(input("Enter the number of columns in second matrix : "))
if col1!=row2:
    print('You cannot multiply these matrices')
    exit()
print("Enter Martix 1")
a1 = input_matrix(row1)
print("Enter Martix 2")
a2 = input_matrix(row2)

print("The Original Matrices are")
print("Matrix 1")
display(a1)
print("Matrix 2")
display(a2)
print()

print("The Sparse Matrices are")
s1 = sparsematrix(a1)
s2 = sparsematrix(a2)
print("Sparse Matrix 1")
display(s1)
print("Sparse Matrix 2")
display(s2)
print()

print("Multiplication of 2 Sparse Matrices")
result = mul(a1,a2)
display(result)